#!/usr/bin/env python3
"""Pressure Engine — Phase A shadow collector (README §2).

Runtime: GitHub Actions (free tier). Each run:
  initialize → collect continuously for COLLECT_SECONDS (default 60s)
  → persist all state to state/state.json + append-only data/*.jsonl
  → exit. The workflow chains the next run and commits everything.

The system MEASURES ITS OWN COVERAGE — gaps between runs are recorded,
never pretended away (README §14).
"""
import os
import time
from datetime import datetime, timezone

from engine import bitget, coverage, experiments, location as LOC, oi as OI
from engine import book as BOOK, tape as TAPE, effort as EFF, funding as FUND
from engine import pressure as PRESS, report as REPORT
from engine.state import (load, save, fresh_symbol_state, cap_all,
                          append_jsonl, MAX_EXPERIMENTS_ACTIVE)

PAIRS = [p.strip().upper() for p in os.environ.get(
    "PAIRS", "NEARUSDT,BTCUSDT,ETHUSDT,SOLUSDT,XRPUSDT").split(",") if p.strip()]
COLLECT_SECONDS = float(os.environ.get("COLLECT_SECONDS", "60"))
CYCLE_SEC = float(os.environ.get("CYCLE_SEC", "2"))
OI_EVERY_SEC = 10
LOCATION_EVERY_SEC = 60
FUNDING_EVERY_SEC = 300


def log(msg):
    print(f"[{datetime.now(timezone.utc).isoformat()}] {msg}", flush=True)


def price_60s_ago(sym, now_ms):
    """Price observed closest to 60s ago (None if no prints that old)."""
    target = now_ms - 60_000
    best = None
    for ts, p in sym["prices"]:
        if ts <= target:
            best = p
        else:
            break
    return best


def current_price(sym, now_ms):
    if sym["prices"]:
        return sym["prices"][-1][1]
    b = sym["book"]["last"]
    if b and b.get("best_bid") and b.get("best_ask"):
        return round((b["best_bid"] + b["best_ask"]) / 2, 8)
    return None


def quality_flags(sym, state, now_ms):
    """README §13 — data quality is part of the signal."""
    flags = []
    q = sym["tape"].get("last_quality")
    if q == "PARTIAL_TAPE":
        flags.append("PARTIAL_TAPE")
    elif q == "ERROR":
        flags.append("TAPE_ERROR")
    oist = OI.evaluate(sym, now_ms)
    if oist["stale"]:
        flags.append("STALE_OI")
    if oist["current"] is None or oist["change_1m"] is None:
        flags.append("INSUFFICIENT_OI_HISTORY")
    b = sym["book"]["last"]
    if b is None or now_ms - b["ts"] > 15_000:
        flags.append("DEPTH_GAP")
    # SESSION_GAP: early in a run when the previous blind gap is recent
    lr = state["coverage"].get("last_run_end")
    if lr and now_ms - lr > 15_000 and now_ms - state["run"]["run_start"] < 20_000:
        flags.append("SESSION_GAP")
    if not flags:
        flags.append("FULL")
    return flags


def evaluate_symbol(state, name, sym, candles_1m, now_ms):
    """Full pressure evaluation for one symbol. Returns (transition, exp)."""
    price = current_price(sym, now_ms)
    if price is None or sym["location"]["atr_1m"] is None:
        return None, None
    atr = sym["location"]["atr_1m"]
    p60 = price_60s_ago(sym, now_ms)
    disp_60_abs = (price - p60) if p60 else 0.0
    disp_60_atr = disp_60_abs / max(atr, 1e-9)   # price units / ATR units
    dz = TAPE.delta_z(sym, now_ms)
    wins = TAPE.window_sums(sym, now_ms)
    cvd_60 = wins["60s"]["delta"]
    oi_state = OI.evaluate(sym, now_ms)
    eff_state = EFF.evaluate(sym, now_ms)
    flow_status = "INSUFFICIENT_HISTORY" if dz is None else wins["quality"]

    ctx = {
        "delta_z": dz, "cvd_60": cvd_60, "disp_60_atr": disp_60_atr,
        "price_slope_60": 1 if disp_60_abs > 0 else (-1 if disp_60_abs < 0 else 0),
        "oi_state": oi_state, "effort_state": eff_state,
        "flow_status": flow_status, "quality_flags": quality_flags(sym, state, now_ms),
    }
    comp = PRESS.build_snapshot(sym, now_ms, price, ctx)
    new_state, transition = PRESS.evaluate_state(sym, comp, now_ms)

    exp = None
    if transition is not None:
        fund_ctx = FUND.context(sym)
        exp = experiments.maybe_create(state, sym, name, comp, transition,
                                      oi_state, fund_ctx, now_ms)
        log(f"{name} state: {transition['from']} -> {transition['to']} ({transition['reason']})"
            + (f" | SETUP {exp['direction']} score={exp['pressure_score']}" if exp else ""))
    state["run"]["calculations"] = state["run"].get("calculations", 0) + 13
    return transition, exp


def main():
    now_ms = int(time.time() * 1000)
    state = load()
    coverage.run_start(state, now_ms)
    log(f"run start · pairs={PAIRS} · collect={COLLECT_SECONDS}s · "
        f"run #{state['coverage']['runs']} · gap="
        f"{state['run']['gap_duration_ms']}ms")

    # init symbol states
    for p in PAIRS:
        if p not in state["symbols"]:
            state["symbols"][p] = fresh_symbol_state()
    # drop symbols no longer configured (their data stays in jsonl)
    for p in list(state["symbols"]):
        if p not in PAIRS:
            del state["symbols"][p]

    loop_start = time.time()
    deadline = loop_start + COLLECT_SECONDS
    next_oi = 0.0
    next_loc = 0.0
    next_fund = 0.0
    trades_since_book = {p: [] for p in PAIRS}
    candles_cache = {p: [] for p in PAIRS}
    oi_errors = book_errors = tape_errors = 0

    cycle = 0
    while time.time() < deadline:
        cycle += 1
        now = time.time()
        now_ms = int(now * 1000)

        if now >= next_loc:
            for p in PAIRS:
                res, err = LOC.refresh(p, state["symbols"][p], now_ms)
                if res is not None and res.get("candles_1m"):
                    candles_cache[p] = res["candles_1m"][:-1]   # closed candles for the sim
            next_loc = now + LOCATION_EVERY_SEC

        if now >= next_fund:
            for p in PAIRS:
                FUND.refresh(p, state["symbols"][p], now_ms)
            next_fund = now + FUNDING_EVERY_SEC

        for p in PAIRS:
            sym = state["symbols"][p]
            # — tape —
            new_trades, q = TAPE.poll(p, sym, now_ms)
            if q == "ERROR":
                tape_errors += 1
            if new_trades:
                state["run"]["trades_received"] = state["run"].get("trades_received", 0) + len(new_trades)
                state["run"]["last_data_ts"] = now_ms
                if q == "PARTIAL_TAPE":
                    state["run"]["data_lost_events"] = state["run"].get("data_lost_events", 0) + 1
                trades_since_book[p] = trades_since_book[p] + new_trades
            # — book —
            snap, err = BOOK.snapshot(p, sym, now_ms, trades_since_book[p])
            trades_since_book[p] = []
            if snap is None:
                book_errors += 1
            else:
                state["run"]["last_data_ts"] = now_ms
            # — OI —
            if now >= next_oi:
                size, err = OI.snapshot(p, sym, now_ms)
                if size is None:
                    oi_errors += 1
                else:
                    state["run"]["last_data_ts"] = now_ms
            # — roll 60s delta buckets (for z-scores) —
            TAPE.roll_60s_buckets(sym, now_ms)

        if now >= next_oi:
            next_oi = now + OI_EVERY_SEC

        # — pressure evaluation + experiments every cycle —
        for p in PAIRS:
            sym = state["symbols"][p]
            transition, exp = evaluate_symbol(state, p, sym, candles_cache[p], now_ms)
            if exp:
                state["experiments"][exp["exp_id"]] = exp
                experiments.flush(exp)   # immutable setup record, appended now
                log(f"SETUP recorded: {p} {exp['direction']} score={exp['pressure_score']} exp_id={exp['exp_id']}")

        # — evaluate pending experiments —
        for eid in list(state["experiments"].keys()):
            exp = state["experiments"][eid]
            sym = state["symbols"].get(exp["symbol"])
            if sym is None:
                continue
            changed = experiments.evaluate(exp, sym, now_ms, state["coverage"]["gaps"])
            experiments.advance_sim(exp, sym, candles_cache.get(exp["symbol"], []),
                                   now_ms, state["coverage"]["gaps"])
            if experiments.finalize(exp, now_ms):
                experiments.flush(exp)
                log(f"experiment {eid} finalized: {exp['observation']}")
                del state["experiments"][eid]

        sleep_until = deadline if deadline < time.time() + CYCLE_SEC else time.time() + CYCLE_SEC
        if sleep_until > time.time():
            time.sleep(sleep_until - time.time())

    # — run end bookkeeping —
    state["run"]["collection_duration_s"] = round(time.time() - loop_start, 2)
    end_ms = int(time.time() * 1000)
    r = coverage.run_end(state, end_ms)
    state["run_final"] = {
        "collection_duration_s": r.get("actual_collection_duration_s"),
        "coverage_pct": state["coverage"].get("coverage_pct"),
        "trades_received": r.get("trades_received", 0),
        "calculations": r.get("calculations", 0),
        "tape_partial_polls": {p: state["symbols"][p]["tape"]["polls_partial"] for p in PAIRS},
        "errors": {"tape": tape_errors, "book": book_errors, "oi": oi_errors},
    }
    for p in PAIRS:
        cap_all(state["symbols"][p])
    out = REPORT.generate(state, state.get("cooldowns", {}),
                           state["experiments"],
                           finalized_count=_finalized_count())
    save(state)
    log(f"run complete · collected {r.get('trades_received', 0)} trades · "
        f"coverage {state['coverage'].get('coverage_pct')}% · report at {out}")


def _finalized_count():
    import json
    path = os.path.join(os.environ.get("DATA_DIR",
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")), "experiments.jsonl")
    if not os.path.exists(path):
        return 0
    by_id = {}
    with open(path) as f:
        for line in f:
            try:
                rec = json.loads(line)
                by_id[rec["exp_id"]] = rec
            except ValueError:
                continue
    return sum(1 for r in by_id.values()
               if r.get("sim", {}).get("status") not in (None, "WAITING_FILL", "OPEN"))


if __name__ == "__main__":
    main()
