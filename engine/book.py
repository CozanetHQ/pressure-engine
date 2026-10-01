"""Order book — depth snapshots, imbalance, and the honest consumption rule.

Rule (README §8): a disappearing wall can have been CANCELLED. Depth
snapshots alone prove nothing about consumption. We classify:

  CONSUMED_WITH_PRINTS  — depth dropped AND executed trades on the relevant
                          side/price region were observed in the same interval.
  LIQUIDITY_REMOVAL_UNCERTAIN — depth dropped, no prints support it.

At a 2s REST snapshot cadence this is intentionally conservative.
"""
from . import bitget
from .state import MAX_IMB_OBS

TRACK_RANGES = (5, 10, 20)


def snapshot(symbol, sym, now_ms, new_trades):
    """One depth poll. `new_trades` = the trades observed since the previous
    depth snapshot (may be empty). Returns the book-state dict."""
    book, err = bitget.fetch_depth(symbol)
    if book is None:
        return None, err
    b, a = book["bids"], book["asks"]
    snap = {"ts": now_ms, "best_bid": b[0][0] if b else None,
            "best_ask": a[0][0] if a else None}
    for n in TRACK_RANGES:
        bid_d = sum(s for _p, s in b[:n])
        ask_d = sum(s for _p, s in a[:n])
        snap[f"bid_{n}"] = round(bid_d, 4)
        snap[f"ask_{n}"] = round(ask_d, 4)
        tot = bid_d + ask_d
        snap[f"imb_{n}"] = round((bid_d - ask_d) / tot, 4) if tot > 0 else 0.0

    bk = sym["book"]
    prev = bk["last"]
    if prev is not None:
        classify_consumption(bk, prev, snap, new_trades)
        delta_ms = snap["ts"] - prev["ts"]
        if delta_ms > 0:
            bk["imb_history"].append([snap["ts"], snap["imb_10"]])
            if len(bk["imb_history"]) > MAX_IMB_OBS:
                del bk["imb_history"][: len(bk["imb_history"]) - MAX_IMB_OBS]
            _update_z_stats(bk, snap["imb_10"])
    bk["last"] = snap
    return snap, None


def classify_consumption(bk, prev, snap, trades):
    """Compare ask/bid depth_10 change against prints in the same interval."""
    if not trades:
        return None
    ask_drop = prev["ask_10"] - snap["ask_10"]
    bid_drop = prev["bid_10"] - snap["bid_10"]
    # did price trade through the region the wall sat in?
    max_px = max((t["price"] for t in trades), default=None)
    min_px = min((t["price"] for t in trades), default=None)
    ev = None
    if ask_drop > 0.15 * max(prev["ask_10"], 1e-9):
        buys = [t for t in trades if t["side"] == "buy" and max_px and t["price"] >= snap["best_ask"] - (snap["best_ask"] - prev["best_ask"] or 0)]
        print_vol = sum(t["size"] for t in buys)
        if print_vol >= 0.25 * ask_drop:
            ev = {"ts": snap["ts"], "kind": "CONSUMED_WITH_PRINTS", "side": "ask",
                  "depth_drop": round(ask_drop, 4), "print_volume": round(print_vol, 4)}
            bk["consumed_events"] += 1
        else:
            ev = {"ts": snap["ts"], "kind": "LIQUIDITY_REMOVAL_UNCERTAIN", "side": "ask",
                  "depth_drop": round(ask_drop, 4), "print_volume": round(print_vol, 4)}
            bk["removal_uncertain_events"] += 1
    if bid_drop > 0.15 * max(prev["bid_10"], 1e-9):
        sells = [t for t in trades if t["side"] == "sell" and min_px and t["price"] <= snap["best_bid"] + (prev["best_bid"] - snap["best_bid"] or 0)]
        print_vol = sum(t["size"] for t in sells)
        if print_vol >= 0.25 * bid_drop:
            ev = ev or {"ts": snap["ts"], "kind": "CONSUMED_WITH_PRINTS", "side": "bid",
                        "depth_drop": round(bid_drop, 4), "print_volume": round(print_vol, 4)}
            bk["consumed_events"] += 1
        else:
            ev = ev or {"ts": snap["ts"], "kind": "LIQUIDITY_REMOVAL_UNCERTAIN", "side": "bid",
                        "depth_drop": round(bid_drop, 4), "print_volume": round(print_vol, 4)}
            bk["removal_uncertain_events"] += 1
    if ev:
        bk["last_event"] = ev
    return ev


def _update_z_stats(bk, x):
    """Welford rolling mean/variance of imb_10 for z-scores."""
    st = bk["imb_z_stats"]
    st["n"] += 1
    d = x - st["mean"]
    st["mean"] += d / st["n"]
    st["m2"] += d * (x - st["mean"])


def imb_z(bk):
    st = bk["imb_z_stats"]
    if st["n"] < 50:
        return None
    var = st["m2"] / (st["n"] - 1) if st["n"] > 1 else 0.0
    std = var ** 0.5
    if std <= 1e-12 or bk["last"] is None:
        return None
    return round((bk["last"]["imb_10"] - st["mean"]) / std, 4)


def recent_consumption(bk, now_ms, window_ms=120_000):
    """0.0/1.0 evidence flag: a CONSUMED_WITH_PRINTS event in the window."""
    le = bk["last_event"]
    if le and le["kind"] == "CONSUMED_WITH_PRINTS" and now_ms - le["ts"] <= window_ms:
        return 1.0
    return 0.0


def liquidity_component(bk, direction, now_ms):
    """Liquidity component (0..1) for `direction` ('long'/'short').

    long:  0.6 * normalized positive imb_10  + 0.4 * ask-side consumption evidence
    short: mirrored on bid side / negative imbalance.
    """
    snap = bk["last"]
    if snap is None:
        return 0.5, "INSUFFICIENT_HISTORY"
    imb = snap["imb_10"]
    z = imb_z(bk)
    cons = recent_consumption(bk, now_ms)
    if direction == "long":
        base = max(0.0, min(1.0, (imb + 0.5) / 1.0))       # imb -0.5..+0.5 -> 0..1
        side_ev = cons if (bk.get("last_event") or {}).get("side") == "ask" else cons
    else:
        base = max(0.0, min(1.0, (-imb + 0.5) / 1.0))
        side_ev = cons if (bk.get("last_event") or {}).get("side") == "bid" else cons
    status = "OK" if z is not None else "INSUFFICIENT_HISTORY"
    return round(0.6 * base + 0.4 * side_ev, 4), status
