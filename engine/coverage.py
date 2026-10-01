"""Coverage — the experiment measures its own blind spots (README §14).

The GitHub Actions runtime has gaps between runs by construction. Every
run records its telemetry; a window of time covered by NO run is a known
blind gap, and experiment evaluation windows that fall inside a blind gap
are marked UNOBSERVED_WINDOW — never counted as failed predictions.
"""
import time
from datetime import datetime, timezone

from .state import append_jsonl, MAX_GAPS


def run_start(state, now_ms=None):
    """Bookkeeping at the top of every run."""
    now_ms = now_ms or int(time.time() * 1000)
    cov = state["coverage"]
    if state["experiment_start"] is None:
        state["experiment_start"] = now_ms
    rec = {
        "run_start": now_ms,
        "run_start_iso": datetime.now(timezone.utc).isoformat(),
        "previous_run_end": cov["last_run_end"],
        "gap_duration_ms": (now_ms - cov["last_run_end"]) if cov["last_run_end"] else None,
    }
    if cov["last_run_end"] and now_ms > cov["last_run_end"]:
        cov["gaps"].append([cov["last_run_end"], now_ms])
        if len(cov["gaps"]) > MAX_GAPS:
            del cov["gaps"][: len(cov["gaps"]) - MAX_GAPS]
    cov["runs"] += 1
    state["run"] = rec
    state["run"]["trades_received"] = 0
    state["run"]["calculations"] = 0
    state["run"]["started_observed"] = now_ms
    return rec


def run_end(state, now_ms=None):
    """Bookkeeping at the end of every run. Returns the run telemetry rec."""
    now_ms = now_ms or int(time.time() * 1000)
    r = state["run"]
    cov = state["coverage"]
    r["run_end"] = now_ms
    r["run_end_iso"] = datetime.now(timezone.utc).isoformat()
    duration_s = (now_ms - r["run_start"]) / 1000.0
    # collection duration = time actually inside the poll loop
    r["actual_collection_duration_s"] = round(r.get("collection_duration_s", duration_s), 2)
    r["last_successful_data_ts"] = r.get("last_data_ts")
    r["expected_next_window"] = datetime.fromtimestamp(
        (now_ms + 45_000) / 1000, timezone.utc).isoformat()   # chain queue hint
    cov["observed_seconds"] += r.get("collection_duration_s", duration_s)
    cov["last_run_end"] = now_ms
    # cumulative coverage
    expected_s = (now_ms - state["experiment_start"]) / 1000.0
    cov["expected_seconds"] = round(expected_s, 1)
    cov["coverage_pct"] = round(cov["observed_seconds"] / expected_s * 100, 1) if expected_s > 0 else None
    r["trades_received"] = r.get("trades_received", 0)
    r["calculations"] = r.get("calculations", 0)
    r["data_lost_events"] = r.get("data_lost_events", 0)
    append_jsonl("runs.jsonl", r)
    return r


def in_gap(gaps, since_ms, until_ms):
    """True if [since, until] overlaps any known blind gap."""
    for gs, ge in gaps:
        if since_ms < ge and until_ms > gs:
            return True
    return False
