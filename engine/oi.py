"""Open interest — self-built history from live snapshots.

Bitget has NO OI history endpoint (verified 404). Every successful snapshot
is persisted to data/oi_history.jsonl AND kept in state for the fast windows.
Percentiles/z-scores are NEVER manufactured: they appear only once enough
observations exist (hourly samples >= 24 => ~1 day), else OI_HISTORY_STATUS
stays INSUFFICIENT_DATA.
"""
import os
from datetime import datetime, timezone

from . import bitget
from .state import append_jsonl, MAX_OI_SNAPSHOTS, MAX_OI_HOURLY

OI_POLL_SEC = 10        # snapshot cadence during a run
OI_STALE_SEC = 45       # older than this at evaluation time -> STALE_OI


def snapshot(symbol, sym, now_ms):
    size, err = bitget.fetch_open_interest(symbol)
    if size is None:
        return None, err
    oi = sym["oi"]
    oi["last"] = {"ts": now_ms, "size": size}
    oi["snapshots"].append([now_ms, size])
    _cap_list(oi["snapshots"], MAX_OI_SNAPSHOTS)
    append_jsonl("oi_history.jsonl", {"symbol": symbol, "ts": now_ms,
                                      "iso": datetime.now(timezone.utc).isoformat(),
                                      "size": size})
    _update_hourly(oi, now_ms, size)
    return size, None


def _cap_list(lst, cap):
    if len(lst) > cap:
        del lst[: len(lst) - cap]


def _update_hourly(oi, now_ms, size):
    hour_ms = (now_ms // 3_600_000) * 3_600_000
    if oi["hourly"] and oi["hourly"][-1][0] == hour_ms:
        oi["hourly"][-1][1] = size
    else:
        oi["hourly"].append([hour_ms, size])
    _cap_list(oi["hourly"], MAX_OI_HOURLY)
    # percentile becomes available only with >= 24 hourly samples (~1 day)
    oi["history_status"] = "OK" if len(oi["hourly"]) >= 24 else "INSUFFICIENT_DATA"


def _size_at(sym, now_ms, window_ms):
    """Nearest snapshot at-or-before (now - window). None if history too short."""
    snaps = sym["oi"]["snapshots"]
    target = now_ms - window_ms
    best = None
    for ts, size in snaps:
        if ts <= target and (best is None or ts > best[0]):
            best = (ts, size)
    return best


def evaluate(sym, now_ms):
    """OI state dict: current, changes 1m/3m/5m, percentile, staleness."""
    oi = sym["oi"]
    out = {
        "current": None, "change_1m": None, "change_pct_1m": None,
        "change_3m": None, "change_pct_3m": None,
        "change_5m": None, "change_pct_5m": None,
        "percentile": None, "status": oi["history_status"],
        "stale": False,
    }
    last = oi["last"]
    if last is None:
        out["status"] = "INSUFFICIENT_DATA"
        return out
    if now_ms - last["ts"] > OI_STALE_SEC * 1000:
        out["stale"] = True
        out["status"] = "STALE_OI"
    cur = last["size"]
    out["current"] = cur
    for w in (60_000, 180_000, 300_000):
        b = _size_at(sym, now_ms, w)
        if b is None:
            continue    # INSUFFICIENT_DATA for this window — never fabricated
        ch = cur - b[1]
        out[f"change_{w//60000}m"] = round(ch, 4)
        out[f"change_pct_{w//60000}m"] = round(ch / b[1] * 100, 4) if b[1] else None
    # percentile over hourly samples, only when >= 24 samples exist
    hourly = oi["hourly"]
    if oi["history_status"] == "OK" and len(hourly) >= 24:
        vals = sorted(s for _t, s in hourly)
        rank = sum(1 for v in vals if v <= cur)
        out["percentile"] = round(rank / len(vals), 4)
    return out


def positioning_component(oi_state, price_slope_sign):
    """Positioning component (0..1) for the direction implied by
    price_slope_sign (+1 evaluating longs, -1 shorts).

    A priori state table (pressure_states_v1):
      price with dir + OI rising   -> new directional participation (0.85)
      price flat  + OI rising      -> positioning building (0.60)
      price with dir + OI flat     -> mild (0.55)
      price against dir + OI falling -> unwinding AGAINST the trade is
                                    profitable for the squeeze (0.75)
      anything else                -> 0.35 (no positioning information)
      INSUFFICIENT/STALE          -> 0.5 neutral, status flags carry it
    """
    if oi_state["current"] is None or oi_state["change_1m"] is None:
        return 0.5, "INSUFFICIENT_DATA"
    ch1 = oi_state["change_1m"]
    status = "OK"
    if oi_state["stale"]:
        return 0.5, "STALE_OI"
    rising = ch1 > 0.0005 * max(oi_state["current"], 1e-9)
    falling = ch1 < -0.0005 * max(oi_state["current"], 1e-9)
    flat = not rising and not falling
    with_dir = price_slope_sign > 0
    if with_dir and rising:
        v, status = 0.85, "PRICE_WITH_DIR_OI_RISING"
    elif flat and rising:
        v, status = 0.60, "OI_RISING_PRICE_FLAT"
    elif with_dir and flat:
        v, status = 0.55, "PRICE_WITH_DIR_OI_FLAT"
    elif (not with_dir) and falling:
        v, status = 0.75, "COUNTER_POSITIONS_UNWINDING"
    else:
        v, status = 0.35, "NO_POSITIONING_INFO"
    return v, status
