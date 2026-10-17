# Pressure Engine — Phase A Diagnostic Report

Generated: **2026-10-17T13:21:27.455394+00:00** · model: **pressure_states_v1** (weights PROVISIONAL EQUAL — not locked, no online learning)

> Shadow-only. No trades. Raw forward-collected telemetry. Numbers without FULL-observation sample sizes are not evidence of edge.

## Runtime coverage (GitHub Actions)

- Runs: **15381** · Observed: **933,904.0s** of expected **1,354,585.0s** → coverage **68.9%**
- Blind gaps recorded: **500**

## Current state by symbol

| Symbol | State | LONG | SHORT | Coverage | OI 1m | CVD 60s | Imb10 | Liquidity | Effort (L/S) | FFP |
|---|---|---|---|---|---|---|---|---|---|---|
| NEAR | NEUTRAL | **28.6** | **33.6** | PARTIAL_TAPE(6100) | 16434734 | 12519.0 | -0.39 | LIQUIDITY_REMOVAL_UNCERTAIN | ABSORPTION/UNKNOWN | 0/0 |
| BTC | NEUTRAL | **35.2** | **21.2** | PARTIAL_TAPE(24373) | 34553 | 3.7 | 0.24 | CONSUMED_WITH_PRINTS | ABSORPTION/UNKNOWN | 0/0 |
| ETH | NEUTRAL | **31.2** | **48.3** | PARTIAL_TAPE(13201) | 790779 | 56.0 | -0.11 | LIQUIDITY_REMOVAL_UNCERTAIN | ABSORPTION/UNKNOWN | 0/0 |
| SOL | NEUTRAL | **34.7** | **28.6** | PARTIAL_TAPE(5069) | 4190976 | 102.1 | 0.42 | CONSUMED_WITH_PRINTS | ABSORPTION/UNKNOWN | 0/0 |
| XRP | NEUTRAL | **27.9** | **26.9** | PARTIAL_TAPE(3317) | 179688570 | 73369.0 | 0.06 | LIQUIDITY_REMOVAL_UNCERTAIN | ABSORPTION/UNKNOWN | 0/0 |

Component status per symbol (latest evaluation):

**NEAR**

- LONG: score **28.6** — location=0.00(NO_LEVEL_NEAR), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.90(FULL), liquidity=0.06(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **33.6** — location=0.79(swing_low), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.54(OK), effortresult=0.34(UNKNOWN), forcedflowproxy=0.00(OK)

**BTC**

- LONG: score **35.2** — location=0.00(NO_LEVEL_NEAR), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.52(FULL), liquidity=0.84(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **21.2** — location=0.16(swing_low), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.56(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)

**ETH**

- LONG: score **31.2** — location=0.69(swing_high), positioning=0.35(NO_POSITIONING_INFO), flow=0.39(PARTIAL_TAPE), liquidity=0.23(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **48.3** — location=0.98(swing_low), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.00(PARTIAL_TAPE), liquidity=0.37(OK), effortresult=1.00(UNKNOWN), forcedflowproxy=0.00(OK)

**SOL**

- LONG: score **34.7** — location=0.00(NO_LEVEL_NEAR), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.38(FULL), liquidity=0.95(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **28.6** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.45(OK), effortresult=0.92(UNKNOWN), forcedflowproxy=0.00(OK)

**XRP**

- LONG: score **27.9** — location=0.00(NO_LEVEL_NEAR), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.59(FULL), liquidity=0.33(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **26.9** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.27(OK), effortresult=1.00(UNKNOWN), forcedflowproxy=0.00(OK)

## Forward-outcome experiment (cumulative)

- Pressure setups recorded: **751** (active: 2, finalized: 749)

- Valid (FULL) +120s observations: **0** · Partial: **749** · Unobserved windows (excluded, per §14): **0**
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
