"""Location engine — where is price relative to liquidity that matters?

Uses the standard market-structure primitives (fractal swings, session
extremes, equal highs/lows clustering) on CLOSED candles only. Distances
are ATR-normalized: distance_in_ATR = |price - level| / ATR.

Per the spec, NO speculative liquidation maps are used as data. If one is
ever added it must be labeled ESTIMATED and kept separate from observed
exchange data.

Direction semantics:
  LONG pressure  -> vulnerability concentrates where trapped shorts sit:
                    ABOVE price (swing highs, equal highs, session high).
  SHORT pressure -> BELOW price (swing lows, equal lows, session low).
"""
from . import bitget

FRACTAL_K = 2
EQ_TOL = 0.0005          # 0.05% tolerance for "equal" highs/lows
CLOSE_ATR = 1.5          # beyond this many ATR a level is irrelevant (score 0)
SESSION_LOOKBACK_1M = 480  # 8h of 1m candles for session extremes


def atr14(candles):
    """Simple ATR14 on closed candles."""
    cl = candles[:-1]
    if len(cl) < 15:
        return None
    trs = []
    for i in range(1, len(cl)):
        c, p = cl[i], cl[i - 1]
        trs.append(max(c["high"] - c["low"], abs(c["high"] - p["close"]),
                       abs(c["low"] - p["close"])))
    return sum(trs[-14:]) / 14


def fractal_levels(candles, k=FRACTAL_K):
    """Confirmed swing highs/lows from closed candles (oldest->newest)."""
    cl = candles[:-1]  # drop forming candle
    highs, lows = [], []
    for i in range(k, len(cl) - k):
        h, l = cl[i]["high"], cl[i]["low"]
        if all(h > cl[j]["high"] for j in range(i - k, i + k + 1) if j != i):
            highs.append({"price": h, "ts": cl[i]["ts"]})
        if all(l < cl[j]["low"] for j in range(i - k, i + k + 1) if j != i):
            lows.append({"price": l, "ts": cl[i]["ts"]})
    return highs, lows


def _equal_clusters(levels):
    """Cluster levels within EQ_TOL -> equal-high/lows (count >= 2)."""
    out = []
    for lv in levels:
        placed = False
        for c in out:
            if abs(c["price"] - lv["price"]) / max(c["price"], 1e-9) <= EQ_TOL:
                c["count"] += 1
                c["price"] = max(c["price"], lv["price"]) if c.get("_max") else lv["price"]
                placed = True
                break
        if not placed:
            out.append({"price": lv["price"], "count": 1})
    return [c for c in out if c["count"] >= 2]


def refresh(symbol, sym, now_ms):
    """Fetch candles, rebuild level sets. Called once per run + every 60s."""
    c1m, e1 = bitget.fetch_candles(symbol, "1m", 240)
    c15m, e2 = bitget.fetch_candles(symbol, "15m", 120)
    if c1m is None or c15m is None or len(c1m) < 30 or len(c15m) < 15:
        return None, e1 or e2
    price = c1m[-1]["close"]
    atr1 = atr14(c1m)
    atr15 = atr15_ = atr14(c15m)
    if not atr1:
        return None, None

    sh, sl = fractal_levels(c15m)
    eqh = _equal_clusters(sh)
    eql = _equal_clusters(sl)

    # session extremes = current UTC day from 1m candles
    day_start = None
    import datetime as _dt
    day_start = int(_dt.datetime.now(_dt.timezone.utc).replace(hour=0, minute=0, second=0, microsecond=0).timestamp() * 1000)
    sess = [c for c in c1m if c["ts"] >= day_start]
    sess_high = max((c["high"] for c in sess), default=None)
    sess_low = min((c["low"] for c in sess), default=None)

    def level_rows(levels, kinds, ref_price):
        rows = []
        for lv in levels:
            dist = abs(ref_price - lv["price"]) / max(atr1, 1e-9)
            rows.append({"kind": kinds, "price": lv["price"], "dist_atr": round(dist, 3)})
        return rows

    # LONG: overhead liquidity ABOVE price (shorts' stops live above highs)
    overhead = ([{"kind": "swing_high", **{"price": x["price"]}} for x in sh if x["price"] > price]
                + [{"kind": "equal_high", "price": x["price"], "count": x["count"]} for x in eqh if x["price"] > price])
    if sess_high and sess_high > price:
        overhead.append({"kind": "session_high", "price": sess_high})
    # SHORT: downside liquidity BELOW price
    below = ([{"kind": "swing_low", "price": x["price"]} for x in sl if x["price"] < price]
             + [{"kind": "equal_low", "price": x["price"], "count": x["count"]} for x in eql if x["price"] < price])
    if sess_low and sess_low < price:
        below.append({"kind": "session_low", "price": sess_low})

    def with_dist(levels, price):
        out = []
        for lv in levels:
            d = abs(price - lv["price"]) / max(atr1, 1e-9)
            out.append({**lv, "dist_atr": round(d, 3)})
        out.sort(key=lambda r: r["dist_atr"])
        return out[:8]

    loc = sym["location"]
    loc["atr_1m"] = atr1
    loc["atr_15m"] = atr15_
    loc["fetched_at"] = now_ms
    loc["levels_long"] = with_dist(overhead, price)
    loc["levels_short"] = with_dist(below, price)
    loc["session_high"] = sess_high
    loc["session_low"] = sess_low
    return {"price": price, "atr_1m": atr1, "candles_1m": c1m, "candles_15m": c15m}, None


def location_component(sym, price, direction):
    """0..1 via the spec formula: score = clamp(1 - distance/ATR).
    0.10 ATR away -> very close (0.9); 1.5 ATR -> irrelevant (0)."""
    loc = sym["location"]
    if loc["atr_1m"] is None:
        return 0.0, "INSUFFICIENT_HISTORY"
    levels = loc["levels_long"] if direction == "long" else loc["levels_short"]
    relevant = [lv for lv in levels if lv["dist_atr"] <= CLOSE_ATR]
    if not relevant:
        return 0.0, "NO_LEVEL_NEAR"
    d = min(lv["dist_atr"] for lv in relevant)
    score = max(0.0, 1.0 - d)
    status = relevant[0]["kind"]
    return round(score, 4), status
