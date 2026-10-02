"""Forward-outcome experiment — the critical test (README §15/§16).

There is NO historical tape/OI/depth for Bitget, so nothing here is a
backtest. Setups are recorded live, immutable (append-only
data/experiments.jsonl), and evaluated in two SEPARATE layers:

  A. PRESSURE PREDICTION — did pressure precede a directional move?
     Windows: +10s / +30s / +60s / +120s from setup, evaluated on the
     OBSERVED trade tape only (precise, run-time prints).
       target       = setup price +/- 1.0 x ATR14(1m) at setup   (locked a priori)
       invalidation = setup price -/+ 1.0 x ATR14(1m) at setup   (locked a priori)
     A window that fell inside a known collection gap (no prints, gap
     overlap confirmed) is marked UNOBSERVED_WINDOW and is NOT counted
     as a failed prediction (README §14). A fully-observed window with
     zero prints is a genuinely flat window (status FULL, MFE=MAE=0).

  B. STRATEGY EXECUTION — would the real entry architecture capture it?
     Simulated POST_ONLY retest limit: pullback entry at
     setup_price -/+ 0.5 x ATR, validity 180 min, evaluated on CLOSED
     1m CANDLES (exchange truth — survives runtime gaps without
     fabrication). Conservative SL-first when both levels sit inside
     one candle. If it never fills: PRESSURE_CORRECT / TRADE_NOT_FILLED
     (§16 — not a strategy loss). On fill, the pressure state at fill
     time is recorded from the transition log — or UNOBSERVED_WINDOW if
     the fill fell inside a blind gap (pressure must be re-evaluated at
     fill; if we could not observe it, we say so).

  Sim fee model: maker 0.02% entry + 0.02% exit (the retest/TP legs are
  post-only/maker by design). Target 2 x ATR, stop 1 x ATR.

Definitions are LOCKED before any results exist and are never altered
after seeing outcomes.
"""
import uuid
from datetime import datetime, timezone

from .state import append_jsonl

TARGET_ATR = 1.0
INVALIDATION_ATR = 1.0
RETEST_PULLBACK_ATR = 0.5
RETEST_VALIDITY_MIN = 180
SIM_TP_ATR = 2.0
SIM_SL_ATR = 1.0
MAKER_FEE = 0.0002
HORIZONS_SEC = (10, 30, 60, 120)
SETUP_COOLDOWN_SEC = 300

SETUP_STATES = ("LONG_PRESSURE_CONFIRMED", "SHORT_PRESSURE_CONFIRMED",
                "FORCED_FLOW_PROXY_LONG", "FORCED_FLOW_PROXY_SHORT")


def is_setup_state(state):
    return state in SETUP_STATES


def _dir_of(state):
    return "long" if "LONG" in state else "short"


def maybe_create(state, sym, sym_name, comp, transition, oi_state, funding_ctx, now_ms):
    """Called on every pressure transition. Creates the immutable setup
    record when the new state is a valid setup state (cooldown applies)."""
    if transition is None or not is_setup_state(transition["to"]):
        return None
    direction = _dir_of(transition["to"])
    cooldowns = state.setdefault("cooldowns", {})
    key = f"{sym_name}:{direction}"
    if cooldowns.get(key) and now_ms - cooldowns[key] < SETUP_COOLDOWN_SEC * 1000:
        return None
    price = comp["price"]
    atr = comp.get("atr_1m") or 0.0
    if not price or not atr:
        return None
    d = comp[direction]
    long = direction == "long"
    sgn = 1.0 if long else -1.0

    # atr is ABSOLUTE (price units) — levels are additive, not multiplicative
    def at(base, atr_mult):
        return round(base + sgn * atr_mult * atr, 8)

    retest = round(price - sgn * RETEST_PULLBACK_ATR * atr, 8)
    sim_tp = round(retest + sgn * SIM_TP_ATR * atr, 8)
    sim_sl = round(retest - sgn * SIM_SL_ATR * atr, 8)
    rec = {
        "exp_id": uuid.uuid4().hex[:12],
        "setup_ts": now_ms,
        "setup_iso": datetime.now(timezone.utc).isoformat(),
        "symbol": sym_name,
        "direction": direction,
        "pressure_state": transition["to"],
        "pressure_score": d["score"],
        "components": d,
        "opposite_score": comp["short" if long else "long"]["score"],
        "data_coverage": comp["data_coverage"],
        "location_levels": sym["location"][f"levels_{direction}"][:4],
        "atr_1m": atr,
        "oi_state": oi_state,
        "funding_state": funding_ctx,
        "cvd": round(sym["tape"]["cvd"], 4),
        "cvd_60": round(_window_delta(sym, now_ms, 60_000), 4),
        "book_imb_10": sym["book"]["last"]["imb_10"] if sym["book"]["last"] else None,
        "liquidity_last_event": sym["book"]["last_event"],
        "effort_state": comp[f"effort_state_{direction}"],
        "price_at_setup": price,
        # A. prediction targets (locked a priori)
        "target_price": at(price, TARGET_ATR),
        "invalidation_price": at(price, -INVALIDATION_ATR),
        # B. execution sim (locked a priori)
        "sim_retest_price": retest,
        "sim_tp_price": sim_tp,
        "sim_sl_price": sim_sl,
        "sim_validity_ms": now_ms + RETEST_VALIDITY_MIN * 60_000,
        "outcomes": {},
        "observation": "PENDING",
        "sim": {"status": "WAITING_FILL"},
    }
    cooldowns[key] = now_ms
    return rec


def _window_delta(sym, now_ms, window_ms):
    since = now_ms - window_ms
    return sum(d for ts, d, _b, _s, _q in sym["tape"]["deltas"] if ts > since)


# ── A. pressure prediction — tape-based ────────────────────────────────────
def evaluate(exp, sym, now_ms, gaps):
    """Advance the +10/30/60/120s windows on OBSERVED prints only."""
    direction = exp["direction"]
    sign = 1 if direction == "long" else -1
    p0 = exp["price_at_setup"]

    def observed_prices(since_ms, until_ms):
        return [(ts, p) for ts, p in sym["prices"] if since_ms < ts <= until_ms]

    def gap_overlap(since_ms, until_ms):
        for gs, ge in gaps:
            if since_ms < ge and until_ms > gs:
                return True
        return False

    changed = False
    for h in HORIZONS_SEC:
        key = f"+{h}s"
        if key in exp["outcomes"]:
            continue
        end_ms = exp["setup_ts"] + h * 1000
        if now_ms < end_ms:
            continue
        pxs = observed_prices(exp["setup_ts"], end_ms)
        overlapped = gap_overlap(exp["setup_ts"], end_ms)
        if overlapped and not pxs:
            exp["outcomes"][key] = {"status": "UNOBSERVED_WINDOW"}
            changed = True
            continue
        if overlapped:
            exp["outcomes"][key] = {"status": "PARTIAL"}   # some prints, gap-influenced
            # still record what was seen, flagged as PARTIAL
        mfe = mae = 0.0
        t_mfe = t_mae = None
        tgt_hit = inv_hit = False
        tgt_ts = inv_ts = None
        for ts, p in pxs:
            fav = (p - p0) * sign
            if fav > mfe:
                mfe, t_mfe = fav, ts
            adv = -fav
            if adv > mae:
                mae, t_mae = adv, ts
            if not tgt_hit and ((sign > 0 and p >= exp["target_price"]) or (sign < 0 and p <= exp["target_price"])):
                tgt_hit, tgt_ts = True, ts
            if not inv_hit and ((sign > 0 and p <= exp["invalidation_price"]) or (sign < 0 and p >= exp["invalidation_price"])):
                inv_hit, inv_ts = True, ts
        exp["outcomes"][key] = {
            "status": "PARTIAL" if overlapped else "FULL",
            "mfe_pct": round(mfe / p0 * 100, 4),
            "mae_pct": round(mae / p0 * 100, 4),
            "time_to_mfe_ms": (t_mfe - exp["setup_ts"]) if t_mfe else None,
            "time_to_mae_ms": (t_mae - exp["setup_ts"]) if t_mae else None,
            "target_hit": tgt_hit, "invalidation_hit": inv_hit,
            "first": ("TARGET" if tgt_ts and (not inv_ts or tgt_ts <= inv_ts)
                      else ("INVALIDATION" if inv_ts else "NEITHER")),
        }
        changed = True
    return changed


# ── B. strategy execution — candle-based ──────────────────────────────────
def advance_sim(exp, sym, candles_1m, now_ms, gaps):
    """POST_ONLY retest simulation on CLOSED 1m candles (exchange truth,
    no fabrication, gap-proof). `candles_1m` = closed candles covering
    [setup, now] (oldest→newest, each with open/high/low/close + ts)."""
    sim = exp["sim"]
    if sim["status"] not in ("WAITING_FILL", "OPEN"):
        return
    direction = exp["direction"]
    long = direction == "long"

    if sim["status"] == "WAITING_FILL" and now_ms > exp["sim_validity_ms"]:
        sim["status"] = "EXPIRED_UNFILLED"
        sim["note"] = "retest never filled within validity — §16: not a strategy loss; " \
                      "prediction layer evaluated separately"
        exp["observation"] = "TRADE_NOT_FILLED"
        return

    for c in candles_1m:
        c_close_ms = c["ts"] + 60_000
        if sim["status"] == "WAITING_FILL":
            if c["ts"] <= exp["setup_ts"]:
                continue
            pulled = (long and c["low"] <= exp["sim_retest_price"]) or \
                     (not long and c["high"] >= exp["sim_retest_price"])
            if pulled:
                sim["status"] = "OPEN"
                sim["fill_ts"] = c_close_ms
                sim["fill_price"] = exp["sim_retest_price"]
                # §16: pressure state at fill time, from the transition log —
                # UNOBSERVED_WINDOW if the fill fell inside a blind gap.
                if _in_gap(gaps, c["ts"], c_close_ms):
                    sim["pressure_at_fill"] = {"state": "UNOBSERVED_WINDOW"}
                else:
                    last_state = _state_at(sym, c_close_ms)
                    sim["pressure_at_fill"] = {"state": last_state,
                                               "note": "from transition log at/nearest fill time"}
            continue
        if sim["status"] == "OPEN":
            if c["ts"] < sim["fill_ts"]:   # skip the fill candle itself + earlier
                continue
            hit_sl = (long and c["low"] <= exp["sim_sl_price"]) or \
                     (not long and c["high"] >= exp["sim_sl_price"])
            hit_tp = (long and c["high"] >= exp["sim_tp_price"]) or \
                     (not long and c["low"] <= exp["sim_tp_price"])
            if hit_sl:      # conservative: SL first when both inside one candle
                _close_sim(exp, "SL", c_close_ms)
                return
            if hit_tp:
                _close_sim(exp, "TP", c_close_ms)
                return


def _in_gap(gaps, since, until):
    for gs, ge in gaps:
        if since < ge and until > gs:
            return True
    return False


def _state_at(sym, ts):
    p = sym["pressure"]
    st = p.get("state")
    for tr in reversed(p.get("transitions") or []):
        if tr["ts"] <= ts:
            return tr["to"]
    return st


def _close_sim(exp, kind, ts):
    sim = exp["sim"]
    fill = sim["fill_price"]
    sign = 1 if exp["direction"] == "long" else -1
    exit_px = exp["sim_tp_price"] if kind == "TP" else exp["sim_sl_price"]
    gross = (exit_px - fill) * sign
    fees = (fill + exit_px) * 2 * MAKER_FEE
    sim["status"] = f"CLOSED_{kind}"
    sim["exit_ts"] = ts
    sim["exit_price"] = exit_px
    sim["gross_pnl_pct"] = round(gross / fill * 100, 4)
    sim["fees_pct"] = round(fees / fill * 100, 4)
    sim["net_pnl_pct"] = round((gross - fees) / fill * 100, 4)
    exp["observation"] = "TRADE_CAPTURED_TP" if kind == "TP" else "TRADE_STOPPED_SL"


def finalize(exp, now_ms):
    """Finished when all prediction windows are evaluated AND the sim is
    terminal. Returns True when the record should be flushed to jsonl."""
    if not all(f"+{h}s" in exp["outcomes"] for h in HORIZONS_SEC):
        return False
    return exp["sim"]["status"] not in ("WAITING_FILL", "OPEN")


def flush(exp):
    append_jsonl("experiments.jsonl", exp)
