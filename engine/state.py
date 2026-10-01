"""State persistence — the ONLY mutable store is state/state.json (git-committed
every run, same audit pattern as the old paper bot). Append-only ledgers live in
data/*.jsonl and are NEVER rewritten.

State schema (v1) — see README §6 for the full field reference.
"""
import json
import os
import tempfile

_REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATE_FILE = os.environ.get("STATE_FILE", os.path.join(_REPO, "state", "state.json"))
DATA_DIR = os.environ.get("DATA_DIR", os.path.join(_REPO, "data"))

MAX_DELTA_OBS = 1800        # ~30 min of per-poll delta observations per symbol
MAX_IMB_OBS = 900           # ~30 min of depth snapshots per symbol
MAX_OI_SNAPSHOTS = 1440     # ~4h at 10s cadence per symbol
MAX_OI_HOURLY = 168          # 7 days of hourly OI samples per symbol
MAX_PRICE_OBS = 3600         # ~30-60 min of observed prints per symbol
MAX_GAPS = 500
MAX_STATE_HISTORY = 500      # pressure state transition log entries per symbol
MAX_EXPERIMENTS_ACTIVE = 60


def fresh_symbol_state():
    return {
        "tape": {
            "cursor_id": None,          # highest tradeId ever observed
            "cvd": 0.0,                 # cumulative observed delta (base units)
            "obs_volume_buy": 0.0,
            "obs_volume_sell": 0.0,
            "deltas": [],               # [(ts_ms, delta, buy_vol, sell_vol, quality)]
            "delta_60_history": [],     # [(bucket_ts, delta_60)] 60s buckets for z
            "polls_full": 0,
            "polls_partial": 0,
            "last_quality": "INIT",
            "trades_received_run": 0,
            "trades_received_total": 0,
        },
        "prices": [],                    # [(ts_ms, price)] observed prints
        "oi": {
            "last": None,               # {"ts", "size"}
            "snapshots": [],            # [(ts, size)] 10s cadence
            "hourly": [],               # [(ts, size)] for percentile
            "history_status": "INSUFFICIENT_DATA",
        },
        "funding": {
            "current": None, "fetched_at": None,
            "history": [],              # [{rate, ts}] settled 8h points, newest first
            "percentile": None, "zscore": None, "history_status": "INSUFFICIENT_HISTORY",
        },
        "book": {
            "last": None,               # {"imb_5","imb_10","imb_20","bid_5","ask_5",...,"ts"}
            "imb_history": [],          # [(ts, imb_10)]
            "imb_z_stats": {"n": 0, "mean": 0.0, "m2": 0.0},   # Welford
            "consumed_events": 0,
            "removal_uncertain_events": 0,
            "last_event": None,
        },
        "location": {
            "atr_1m": None, "atr_15m": None, "fetched_at": None,
            "levels_long": [],          # [{kind, price, dist_atr}] overhead liquidity
            "levels_short": [],          # downside liquidity
            "session_high": None, "session_low": None,
        },
        "effort": {
            "eff_history_long": [],      # [(ts, efficiency_raw)] for rolling median
            "eff_history_short": [],
        },
        "pressure": {
            "state": "NEUTRAL", "since_ts": None,
            "last_scores": None,         # full component snapshot (last evaluation)
            "transitions": [],           # [{ts, from, to, reason}]
            "states_seen": {},
            "evaluations": 0,
        },
    }


def fresh_state():
    return {
        "schema_version": 1,
        "model_version": "pressure_states_v1",
        "experiment_start": None,
        "symbols": {},
        "experiments": {},              # exp_id -> working record (see experiments.py)
        "coverage": {
            "last_run_end": None,
            "observed_seconds": 0.0,
            "runs": 0,
            "gaps": [],                  # [(start_ms, end_ms)]
        },
        "run": {},
    }


def load():
    if os.path.exists(STATE_FILE):
        try:
            with open(STATE_FILE) as f:
                st = json.load(f)
            # forward-compat guard: missing keys default in
            base = fresh_state()
            for k, v in base.items():
                st.setdefault(k, v)
            return st
        except (ValueError, OSError):
            pass
    return fresh_state()


def save(state):
    os.makedirs(os.path.dirname(STATE_FILE), exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(STATE_FILE))
    try:
        with os.fdopen(fd, "w") as f:
            json.dump(state, f, separators=(",", ":"))
        os.replace(tmp, STATE_FILE)
    finally:
        if os.path.exists(tmp):
            os.remove(tmp)


def append_jsonl(name, records):
    if isinstance(records, dict):
        records = [records]
    if not records:
        return
    os.makedirs(DATA_DIR, exist_ok=True)
    path = os.path.join(DATA_DIR, name)
    with open(path, "a") as f:
        for r in records:
            f.write(json.dumps(r, separators=(",", ":")) + "\n")


def _cap(lst, cap):
    if len(lst) > cap * 2:   # trim hard, keeps commits small
        del lst[: len(lst) - cap]
    return lst


def cap_all(sym):
    """Trim per-symbol rolling buffers to their caps (called at run end)."""
    t = sym["tape"]
    _cap(t["deltas"], MAX_DELTA_OBS)
    _cap(t["delta_60_history"], 480)     # 8h of 60s buckets
    _cap(sym["prices"], MAX_PRICE_OBS)
    _cap(sym["oi"]["snapshots"], MAX_OI_SNAPSHOTS)
    _cap(sym["oi"]["hourly"], MAX_OI_HOURLY)
    _cap(sym["book"]["imb_history"], MAX_IMB_OBS)
    _cap(sym["book"]["imb_history"], MAX_IMB_OBS)
    _cap(sym["effort"]["eff_history_long"], 600)
    _cap(sym["effort"]["eff_history_short"], 600)
    _cap(sym["pressure"]["transitions"], MAX_STATE_HISTORY)
