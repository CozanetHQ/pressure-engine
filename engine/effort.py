"""Effort vs result — absorption/expansion observation.

  effort  = aggressive volume in the evaluation interval (directional side)
  result  = price displacement in the same interval
  efficiency = displacement / effort

Raw efficiency is symbol-specific -> normalized against a rolling median
of the SAME direction's historical efficiency (per symbol). Until
>= 50 prior observations exist: INSUFFICIENT_HISTORY, value 0.5 neutral.

Interpretation (stored, NOT traded):
  high effort + high normalized efficiency -> EXPANSION_CANDIDATE
  high effort + low normalized efficiency  -> ABSORPTION_CANDIDATE
"""
EFF_MIN_OBS = 50
EFF_HISTORY_CAP = 600


def _median(xs):
    xs = sorted(xs)
    n = len(xs)
    mid = n // 2
    return xs[mid] if n % 2 else (xs[mid - 1] + xs[mid]) / 2


def evaluate(sym, now_ms, window_ms=60_000):
    """Returns dict with per-direction efficiency + interpretation."""
    out = {"window_ms": window_ms, "status": "INSUFFICIENT_HISTORY",
           "long": None, "short": None, "interpretation_long": "UNKNOWN",
           "interpretation_short": "UNKNOWN"}
    deltas = sym["tape"]["deltas"]
    prices = sym["prices"]
    since = now_ms - window_ms
    dv = [(ts, d, b, s, q) for ts, d, b, s, q in deltas if ts > since]
    px = [(ts, p) for ts, p in prices if ts > since]
    if not px:
        return out
    p0, p1 = px[0][1], px[-1][1]
    disp_up = (p1 - p0) / p0
    disp_abs = abs(disp_up)
    buy_eff = sum(b for _t, _d, b, _s, _q in dv)
    sell_eff = sum(s for _t, _d, _b, s, _q in dv)
    eff_long = (disp_up / buy_eff) if buy_eff > 0 else None      # up-move per aggressive buy
    eff_short = (-disp_up / sell_eff) if sell_eff > 0 else None  # down-move per aggressive sell

    eff = sym["effort"]
    for name, raw in (("long", eff_long), ("short", eff_short)):
        hist = eff[f"eff_history_{name}"]
        norm = None
        if raw is not None and raw >= 0:
            hist.append([now_ms, raw])
            if len(hist) > EFF_HISTORY_CAP:
                del hist[: len(hist) - EFF_HISTORY_CAP]
        prior = [v for _t, v in hist[:-1]]
        if raw is not None and len(prior) >= EFF_MIN_OBS:
            med = _median(prior[-300:])
            norm = raw / med if med > 0 else None
        out[name] = {"raw": raw, "normalized": norm}
        out["status"] = "OK" if norm is not None else out["status"]

    # interpretation — effort high relative to prior 60s buckets (>= 20 buckets)
    cur_buy = buy_eff
    cur_sell = sell_eff
    hist = sym["tape"]["delta_60_history"]
    prior_buy = [b[2] for b in hist[:-1]] if len(hist) > 1 else []
    prior_sell = [b[3] for b in hist[:-1]] if len(hist) > 1 else []
    buy_high = _effort_high(cur_buy, prior_buy)
    sell_high = _effort_high(cur_sell, prior_sell)
    nl = out["long"]["normalized"] if out["long"] else None
    ns = out["short"]["normalized"] if out["short"] else None
    if buy_high:
        if nl is not None and nl >= 1.5:
            out["interpretation_long"] = "EXPANSION_CANDIDATE"
        elif nl is not None and nl <= 0.5:
            out["interpretation_long"] = "ABSORPTION_CANDIDATE"
    if sell_high:
        if ns is not None and ns >= 1.5:
            out["interpretation_short"] = "EXPANSION_CANDIDATE"
        elif ns is not None and ns <= 0.5:
            out["interpretation_short"] = "ABSORPTION_CANDIDATE"
    return out


def _effort_high(cur, prior):
    """Effort is 'high' when the current 60s side volume >= 1.5x the median
    of prior 60s buckets (>= 20 buckets of history required)."""
    if cur is None or cur <= 0 or len(prior) < 20:
        return False
    med = _median(prior[-180:])
    return med > 0 and cur >= 1.5 * med


def effort_component(eff_state, direction):
    """0..1 from directional normalized efficiency:
    norm >= 2 -> 1.0;  norm <= 0.5 -> 0.2 (blocked/absorbed); linear between.
    INSUFFICIENT_HISTORY -> 0.5 neutral."""
    d = eff_state.get(direction)
    if not d or d.get("normalized") is None:
        return 0.5, "INSUFFICIENT_HISTORY"
    n = d["normalized"]
    if n >= 2.0:
        v = 1.0
    elif n <= 0.5:
        v = 0.2
    else:
        v = 0.2 + (n - 0.5) / 1.5 * 0.8
    interp = eff_state.get(f"interpretation_{direction}", "UNKNOWN")
    return round(v, 4), interp
