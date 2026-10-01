"""Diagnostic report — regenerated to docs/REPORT.md at the end of every run.

Per README §19: raw experiment telemetry, NOT a win rate. Observation
counts and rules are printed alongside every statistic so a number can
never masquerade as evidence without its sample size.
"""
import json
import os
from datetime import datetime, timezone

from .experiments import HORIZONS_SEC

_REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _fmt(v, nd=2):
    if v is None:
        return "—"
    if isinstance(v, float):
        return f"{v:.{nd}f}"
    return str(v)


def _pct(x):
    return "—" if x is None else f"{x:.1f}%"


def generate(state, cooldowns, live_experiments, finalized_count):
    lines = []
    a = lines.append
    now = datetime.now(timezone.utc)
    a(f"# Pressure Engine — Phase A Diagnostic Report")
    a("")
    a(f"Generated: **{now.isoformat()}** · model: **{state['model_version']}** "
       f"(weights PROVISIONAL EQUAL — not locked, no online learning)")
    a("")
    a("> Shadow-only. No trades. Raw forward-collected telemetry. "
      "Numbers without FULL-observation sample sizes are not evidence of edge.")
    a("")

    # — runtime coverage —
    cov = state["coverage"]
    a("## Runtime coverage (GitHub Actions)")
    a("")
    a(f"- Runs: **{cov['runs']}** · Observed: **{round(cov['observed_seconds'],0):,}s** "
       f"of expected **{round(cov.get('expected_seconds') or 0,0):,}s** → "
       f"coverage **{_pct(cov.get('coverage_pct'))}**")
    a(f"- Blind gaps recorded: **{len(cov['gaps'])}**")
    a("")

    # — per-symbol snapshot —
    a("## Current state by symbol")
    a("")
    a("| Symbol | State | LONG | SHORT | Coverage | OI 1m | CVD 60s | Imb10 | Liquidity | Effort (L/S) | FFP |")
    a("|---|---|---|---|---|---|---|---|---|---|---|")
    for name, sym in state["symbols"].items():
        p = sym["pressure"]
        ls = p.get("last_scores")
        if not ls:
            a(f"| {name.replace('USDT','')} | {p['state']} | — | — | INIT | — | — | — | — | — | — |")
            continue
        t = sym["tape"]
        cov_flags = ",".join(ls.get("data_coverage") or ["FULL"])
        if t["polls_partial"]:
            cov_flags = f"PARTIAL_TAPE({t['polls_partial']})" if "FULL" in cov_flags else cov_flags
        oi = sym["oi"]
        oi_s = "—" if not oi["last"] else f"{_fmt(oi['last']['size'],0)}"
        cvd60 = sum(d for ts, d, _b, _s, _q in t["deltas"] if ts > (now.timestamp()*1000 - 60_000))
        imb = _fmt(sym["book"]["last"]["imb_10"]) if sym["book"]["last"] else "—"
        liq_ev = (sym["book"]["last_event"] or {}).get("kind", "—")
        effl = sym["effort"]
        a(f"| {name.replace('USDT','')} | {p['state']} "
          f"| **{_fmt(ls['long']['score'],1)}** | **{_fmt(ls['short']['score'],1)}** "
          f"| {cov_flags} | {oi_s} | {_fmt(cvd60,1)} | {imb} | {liq_ev} "
          f"| {ls.get('effort_state_long','—')[:10]}/{ls.get('effort_state_short','—')[:10]} "
          f"| {_fmt(ls['long']['forcedflowproxy']['value'],0)}/{_fmt(ls['short']['forcedflowproxy']['value'],0)} |")
    a("")
    a("Component status per symbol (latest evaluation):")
    a("")
    for name, sym in state["symbols"].items():
        ls = sym["pressure"].get("last_scores")
        if not ls:
            continue
        a(f"**{name.replace('USDT','')}**")
        a("")
        for d in ("long", "short"):
            a(f"- {d.upper()}: score **{_fmt(ls[d]['score'],1)}** — " +
              ", ".join(f"{k}={_fmt(ls[d][k]['value'],2)}({ls[d][k]['status']})"
                        for k in ls[d] if k in ("location", "positioning", "flow",
                                                "liquidity", "effortresult", "forcedflowproxy")))
        a("")

    # — experiment statistics —
    a("## Forward-outcome experiment (cumulative)")
    a("")
    total = finalized_count + len(live_experiments)
    a(f"- Pressure setups recorded: **{total}** (active: {len(live_experiments)}, finalized: {finalized_count})")
    a("")
    # finalized = deduped records with terminal sim states
    final = [e for e in _read_finalized()
             if e.get("sim", {}).get("status") not in (None, "WAITING_FILL", "OPEN")]
    full_obs = []
    partial_obs = 0
    unobserved = 0
    for e in final:
        o = e.get("outcomes", {}).get("+120s", {})
        st = o.get("status")
        if st == "FULL":
            full_obs.append(e)
        elif st == "UNOBSERVED_WINDOW":
            unobserved += 1
        elif st == "PARTIAL":
            partial_obs += 1
    a(f"- Valid (FULL) +120s observations: **{len(full_obs)}** · "
      f"Partial: **{partial_obs}** · Unobserved windows (excluded, per §14): **{unobserved}**")
    longs = [e for e in full_obs if e["direction"] == "long"]
    shorts = [e for e in full_obs if e["direction"] == "short"]
    a(f"- Long setups (FULL): **{len(longs)}** · Short setups (FULL): **{len(shorts)}**")
    a("")
    if full_obs:
        tgt = sum(1 for e in full_obs if e["outcomes"]["+120s"]["first"] == "TARGET")
        inv = sum(1 for e in full_obs if e["outcomes"]["+120s"]["first"] == "INVALIDATION")
        neither = len(full_obs) - tgt - inv
        a(f"- +120s target reached first: **{tgt}** · invalidation first: **{inv}** · "
          f"neither: **{neither}** (of {len(full_obs)} FULL observations)")
        mfes = sorted(e["outcomes"]["+120s"]["mfe_pct"] for e in full_obs)
        maes = sorted(e["outcomes"]["+120s"]["mae_pct"] for e in full_obs)
        med = lambda xs: xs[len(xs)//2] if xs else None
        a(f"- MFE avg **{_fmt(sum(mfes)/len(mfes))}%** median **{_fmt(med(mfes))}%** · "
          f"MAE avg **{_fmt(sum(maes)/len(maes))}%** median **{_fmt(med(maes))}%**")
        # pressure->move correlation over FULL observations
        corr = _corr([(e["pressure_score"], e["outcomes"]["+120s"]["mfe_pct"] - e["outcomes"]["+120s"]["mae_pct"]) for e in full_obs])
        a(f"- Pressure score → signed +120s displacement correlation: **{_fmt(corr,3)}** "
          f"(n={len(full_obs)} FULL)")
        # horizon table
        a("")
        a("### By horizon (FULL observations only)")
        a("")
        a("| Horizon | n | avg MFE % | avg MAE % | target first | inval first |")
        a("|---|---|---|---|---|---|")
        for h in HORIZONS_SEC:
            key = f"+{h}s"
            rows = [e for e in final if e.get("outcomes", {}).get(key, {}).get("status") == "FULL"]
            if not rows:
                a(f"| {key} | 0 | — | — | — | — |")
                continue
            t = sum(1 for e in rows if e["outcomes"][key]["first"] == "TARGET")
            i2 = sum(1 for e in rows if e["outcomes"][key]["first"] == "INVALIDATION")
            m = sum(e["outcomes"][key]["mfe_pct"] for e in rows) / len(rows)
            n2 = sum(e["outcomes"][key]["mae_pct"] for e in rows) / len(rows)
            a(f"| {key} | {len(rows)} | {_fmt(m)} | {_fmt(n2)} | {t} | {i2} |")
        # sim stats
        a("")
        a("### Strategy-execution sim (§16 — pressure prediction and fill are reported separately)")
        a("")
        fills = [e for e in full_obs if e["sim"]["status"].startswith("CLOSED")]
        nf = sum(1 for e in full_obs if e["sim"]["status"] == "EXPIRED_UNFILLED")
        press_correct_unfilled = sum(1 for e in full_obs
                                     if e["sim"]["status"] == "EXPIRED_UNFILLED"
                                     and e["outcomes"]["+120s"]["first"] == "TARGET")
        a(f"- Retest filled: **{len(fills)}** · expired unfilled: **{nf}** "
          f"(of which pressure still correct at +120s: **{press_correct_unfilled}** → "
          f"PRESSURE_CORRECT / TRADE_NOT_FILLED)")
        if fills:
            tps = sum(1 for e in fills if e["sim"]["status"] == "CLOSED_TP")
            a(f"- Sim closed TP: **{tps}** · SL: **{len(fills)-tps}** · "
              f"avg net after maker fees: **{_fmt(sum(e['sim']['net_pnl_pct'] for e in fills)/len(fills))}%**")
    else:
        a("_No finalized FULL observations yet — Phase A is still accumulating._")
    a("")
    a("### No win rate is reported")
    a("")
    a("A win rate requires (a) a defined sample-size rule, (b) FULL observation of the "
      "evaluation window, (c) a fixed model version. Until the forward dataset meets "
      "those conditions, the counts above are raw telemetry only.")
    a("")
    a("### Observation rules (locked a priori)")
    a("")
    a("- target = ±1.0×ATR14(1m) at setup · invalidation = ∓1.0×ATR14(1m)")
    a("- +10s/+30s/+60s/+120s windows from setup, evaluated on OBSERVED prints only")
    a("- UNOBSERVED_WINDOW (collection gap) is excluded from prediction counts")
    a("- Sim entry: POST_ONLY retest at setup∓0.5×ATR, 180 min validity, TP 2×ATR / SL 1×ATR, maker fees")
    a("- State defs: `pressure_states_v1` — a priori, changed only offline with a version bump")

    out = os.path.join(_REPO, "docs", "REPORT.md")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w") as f:
        f.write("\n".join(lines) + "\n")
    return out


def _read_finalized():
    """All flushed experiment records, deduped by exp_id (latest flush wins:
    each setup is flushed once at creation — observation PENDING — and once
    at completion)."""
    path = os.path.join(_REPO, "data", "experiments.jsonl")
    by_id = {}
    if os.path.exists(path):
        with open(path) as f:
            for line in f:
                try:
                    rec = json.loads(line)
                    by_id[rec["exp_id"]] = rec
                except ValueError:
                    continue
    return [by_id[k] for k in sorted(by_id, key=lambda k: by_id[k].get("setup_ts", 0))]


def _corr(pairs):
    xs = [p[0] for p in pairs]
    ys = [p[1] for p in pairs]
    n = len(xs)
    if n < 3:
        return None
    mx, my = sum(xs) / n, sum(ys) / n
    cov = sum((x - mx) * (y - my) for x, y in pairs)
    vx = sum((x - mx) ** 2 for x in xs)
    vy = sum((y - my) ** 2 for y in ys)
    if vx <= 0 or vy <= 0:
        return None
    return cov / (vx ** 0.5 * vy ** 0.5)
