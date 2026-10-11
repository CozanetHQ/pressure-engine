# Pressure Engine — Phase A Diagnostic Report

Generated: **2026-10-11T01:15:59.145425+00:00** · model: **pressure_states_v1** (weights PROVISIONAL EQUAL — not locked, no online learning)

> Shadow-only. No trades. Raw forward-collected telemetry. Numbers without FULL-observation sample sizes are not evidence of edge.

## Runtime coverage (GitHub Actions)

- Runs: **8785** · Observed: **533,002.0s** of expected **792,657.0s** → coverage **67.2%**
- Blind gaps recorded: **500**

## Current state by symbol

| Symbol | State | LONG | SHORT | Coverage | OI 1m | CVD 60s | Imb10 | Liquidity | Effort (L/S) | FFP |
|---|---|---|---|---|---|---|---|---|---|---|
| NEAR | NEUTRAL | **39.1** | **36.7** | PARTIAL_TAPE(3230) | 16563438 | 4121.0 | -0.20 | CONSUMED_WITH_PRINTS | UNKNOWN/ABSORPTION | 0/0 |
| BTC | NEUTRAL | **48.9** | **25.0** | PARTIAL_TAPE(12707) | 34167 | 13.5 | 0.83 | LIQUIDITY_REMOVAL_UNCERTAIN | EXPANSION_/UNKNOWN | 0/0 |
| ETH | NEUTRAL | **40.3** | **24.7** | PARTIAL_TAPE(6331) | 776786 | 8.6 | 0.40 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/UNKNOWN | 0/0 |
| SOL | NEUTRAL | **32.8** | **16.3** | PARTIAL_TAPE(2409) | 4236092 | 108.2 | -0.21 | LIQUIDITY_REMOVAL_UNCERTAIN | ABSORPTION/UNKNOWN | 0/0 |
| XRP | NEUTRAL | **34.2** | **24.2** | PARTIAL_TAPE(1739) | 195060696 | 14834.0 | -0.55 | CONSUMED_WITH_PRINTS | EXPANSION_/UNKNOWN | 0/0 |

Component status per symbol (latest evaluation):

**NEAR**

- LONG: score **39.1** — location=0.32(session_high), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.47(FULL), liquidity=0.58(OK), effortresult=0.43(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **36.7** — location=0.83(swing_low), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.82(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

**BTC**

- LONG: score **48.9** — location=0.00(NO_LEVEL_NEAR), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=1.00(FULL), liquidity=0.60(OK), effortresult=0.78(EXPANSION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **25.0** — location=0.95(swing_low), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.00(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)

**ETH**

- LONG: score **40.3** — location=0.00(NO_LEVEL_NEAR), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.33(FULL), liquidity=0.54(OK), effortresult=1.00(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **24.7** — location=0.87(swing_low), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.06(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)

**SOL**

- LONG: score **32.8** — location=0.69(swing_high), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.36(FULL), liquidity=0.17(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **16.3** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.43(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)

**XRP**

- LONG: score **34.2** — location=0.00(NO_LEVEL_NEAR), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.55(FULL), liquidity=0.00(OK), effortresult=0.95(EXPANSION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **24.2** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.60(OK), effortresult=0.50(INSUFFICIENT_HISTORY), forcedflowproxy=0.00(OK)

## Forward-outcome experiment (cumulative)

- Pressure setups recorded: **441** (active: 0, finalized: 441)

- Valid (FULL) +120s observations: **0** · Partial: **441** · Unobserved windows (excluded, per §14): **0**
- Long setups (FULL): **0** · Short setups (FULL): **0**

_No finalized FULL observations yet — Phase A is still accumulating._

### No win rate is reported

A win rate requires (a) a defined sample-size rule, (b) FULL observation of the evaluation window, (c) a fixed model version. Until the forward dataset meets those conditions, the counts above are raw telemetry only.

### Observation rules (locked a priori)

- target = ±1.0×ATR14(1m) at setup · invalidation = ∓1.0×ATR14(1m)
- +10s/+30s/+60s/+120s windows from setup, evaluated on OBSERVED prints only
- UNOBSERVED_WINDOW (collection gap) is excluded from prediction counts
- Sim entry: POST_ONLY retest at setup∓0.5×ATR, 180 min validity, TP 2×ATR / SL 1×ATR, maker fees
- State defs: `pressure_states_v1` — a priori, changed only offline with a version bump
