"""Trade tape — delta / CVD with HONEST coverage marking.

Bitget fills return only the newest 100 trades. Coverage detection is
empirical, per poll, using the tradeId cursor:

  - overlap: the fetch contains a tradeId <= cursor  → we can see
    continuously from the cursor forward → FULL for this interval.
  - no overlap AND exactly 100 rows → the 100-trade window slid past our
    cursor between polls → trades were missed → PARTIAL_TAPE.
  - no overlap AND < 100 rows → all trades since the cursor are inside
    this fetch → FULL.

Missing trades are NEVER fabricated: CVD simply accumulates what was
actually observed, and every downstream calculation carries the quality
flag of the polls it was built from.

Aggressor assumption (documented, verifiable from the data itself):
fills `side` is the TAKER direction — side="buy" means an aggressive
buyer lifted the ask (+size into delta), side="sell" means an aggressive
seller hit the bid (−size). The collected record lets us verify this
empirically (signed delta vs price displacement correlation).
"""
from . import bitget


def poll(symbol, sym, now_ms):
    """One fills poll. Returns (new_trades, quality) where quality is
    'FULL', 'PARTIAL_TAPE', or 'ERROR'."""
    rows, err = bitget.fetch_fills(symbol)
    tape = sym["tape"]
    if rows is None:
        tape["last_quality"] = "ERROR"
        return [], "ERROR"

    if not rows:
        return [], tape.get("last_quality") or "FULL"

    cursor = tape["cursor_id"]
    newest_id = int(rows[0]["trade_id"])
    oldest_id = int(rows[-1]["trade_id"])

    if cursor is None:
        # first observation ever: baseline, nothing counted as covered
        new = list(rows)
        quality = "INIT"
    else:
        new = [r for r in rows if int(r["trade_id"]) > cursor]
        overlap = oldest_id <= cursor          # fetch reaches back past cursor
        if overlap:
            quality = "FULL"
        elif len(rows) >= 100:
            quality = "PARTIAL_TAPE"          # window slid past cursor: trades lost
        else:
            quality = "FULL"                  # all trades since cursor are here

    # update accumulators from NEW trades only
    buy_v = sum(r["size"] for r in new if r["side"] == "buy")
    sell_v = sum(r["size"] for r in new if r["side"] == "sell")
    if new:
        delta = buy_v - sell_v
        ts = new[0]["ts"]                     # newest of the batch
        tape["deltas"].append([ts, delta, buy_v, sell_v, quality])
        tape["cvd"] += delta
        tape["obs_volume_buy"] += buy_v
        tape["obs_volume_sell"] += sell_v
        tape["trades_received_run"] += len(new)
        tape["trades_received_total"] += len(new)
        # observed price stream (for MFE/MAE + effort/result)
        for r in new:
            sym["prices"].append([r["ts"], r["price"]])

    if cursor is None or quality != "INIT":
        if quality == "FULL" or quality == "INIT":
            tape["polls_full"] += 1
        elif quality == "PARTIAL_TAPE":
            tape["polls_partial"] += 1
        tape["last_quality"] = quality
    if newest_id and (cursor is None or newest_id > cursor):
        tape["cursor_id"] = newest_id

    return new, quality


def window_quality(sym, since_ms):
    """'PARTIAL_TAPE' if ANY delta observation since `since_ms` was partial
    (or if the tape errored), else 'FULL'."""
    for _ts, _d, _b, _s, q in sym["tape"]["deltas"]:
        if _ts >= since_ms and q == "PARTIAL_TAPE":
            return "PARTIAL_TAPE"
    return "FULL"


def window_sums(sym, now_ms):
    """Aggressive volume/delta over 5s/15s/30s/60s windows (observed only).
    Returns dict of {name: {buy, sell, delta}} plus quality flags."""
    out = {}
    for sec in (5, 15, 30, 60):
        since = now_ms - sec * 1000
        buy = sell = 0.0
        for ts, d, b, s, _q in sym["tape"]["deltas"]:
            if ts >= since:
                buy += b
                sell += s
        out[f"{sec}s"] = {"buy": buy, "sell": sell, "delta": buy - sell}
    out["quality"] = window_quality(sym, now_ms - 60_000)
    return out


def roll_60s_buckets(sym, now_ms):
    """Bucket per-poll deltas into non-overlapping 60s sums (for z-scores).
    Uses the newest 60s bucket boundary <= now."""
    if not sym["tape"]["deltas"]:
        return
    b_end = (now_ms // 60_000) * 60_000          # current bucket start boundary
    hist = sym["tape"]["delta_60_history"]
    last_bucket = hist[-1][0] if hist else None
    if last_bucket == b_end:
        return                                    # still inside current bucket
    # close every completed bucket between last_bucket and b_end
    t = sym["tape"]["deltas"]
    boundary = last_bucket if last_bucket is not None else b_end - 60_000
    while boundary + 60_000 <= b_end:
        s, e = boundary, boundary + 60_000
        obs = [x for x in t if s < x[0] <= e]
        tot = sum(x[1] for x in obs)
        buy = sum(x[2] for x in obs)
        sell = sum(x[3] for x in obs)
        hist.append([e, round(tot, 6), round(buy, 6), round(sell, 6)])
        boundary += 60_000
    # drop stale deltas: keep 60 min back for window calcs
    cutoff = now_ms - 3_600_000
    t[:] = [x for x in t if x[0] >= cutoff]


def delta_z(sym, now_ms, window_ms=60_000):
    """Z-score of the CURRENT 60s delta vs prior 60s-bucket history.
    None until >= 30 prior buckets exist (INSUFFICIENT_HISTORY)."""
    hist = sym["tape"]["delta_60_history"]
    prior = [b[1] for b in hist if b[0] <= (now_ms // 60_000) * 60_000]
    if len(prior) < 30:
        return None
    since = now_ms - window_ms
    cur = sum(d for ts, d, _b, _s, _q in sym["tape"]["deltas"] if ts > since)
    mean = sum(prior) / len(prior)
    var = sum((x - mean) ** 2 for x in prior) / len(prior)
    std = var ** 0.5
    if std <= 1e-12:
        return None
    return (cur - mean) / std
