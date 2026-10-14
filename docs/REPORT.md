# Pressure Engine — Phase A Diagnostic Report

Generated: **2026-10-14T01:24:13.555199+00:00** · model: **pressure_states_v1** (weights PROVISIONAL EQUAL — not locked, no online learning)

> Shadow-only. No trades. Raw forward-collected telemetry. Numbers without FULL-observation sample sizes are not evidence of edge.

## Runtime coverage (GitHub Actions)

- Runs: **11966** · Observed: **726,285.0s** of expected **1,052,351.0s** → coverage **69.0%**
- Blind gaps recorded: **500**

## Current state by symbol

| Symbol | State | LONG | SHORT | Coverage | OI 1m | CVD 60s | Imb10 | Liquidity | Effort (L/S) | FFP |
|---|---|---|---|---|---|---|---|---|---|---|
| NEAR | NEUTRAL | **38.2** | **18.2** | PARTIAL_TAPE(4832) | 16078356 | 483.0 | -0.41 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/UNKNOWN | 0/0 |
| BTC | NEUTRAL | **50.4** | **24.7** | PARTIAL_TAPE(17529) | 32100 | 3.9 | 0.73 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/UNKNOWN | 0/0 |
| ETH | NEUTRAL | **30.7** | **21.4** | PARTIAL_TAPE(9265) | 742823 | 247.5 | 0.16 | LIQUIDITY_REMOVAL_UNCERTAIN | ABSORPTION/UNKNOWN | 0/0 |
| SOL | LONG_PRESSURE_BUILDING | **38.0** | **20.9** | PARTIAL_TAPE(3586) | 4011449 | 290.1 | -0.00 | CONSUMED_WITH_PRINTS | UNKNOWN/ABSORPTION | 0/0 |
| XRP | NEUTRAL | **42.6** | **18.9** | PARTIAL_TAPE(2481) | 175187502 | 10113.0 | 0.19 | LIQUIDITY_REMOVAL_UNCERTAIN | EXPANSION_/UNKNOWN | 0/0 |

Component status per symbol (latest evaluation):

**NEAR**

- LONG: score **38.2** — location=0.38(swing_high), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.31(FULL), liquidity=0.06(OK), effortresult=1.00(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **18.2** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.54(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)

**BTC**

- LONG: score **50.4** — location=0.77(swing_high), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.44(PARTIAL_TAPE), liquidity=0.60(OK), effortresult=0.67(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **24.7** — location=0.93(swing_low), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(PARTIAL_TAPE), liquidity=0.00(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)

**ETH**

- LONG: score **30.7** — location=0.02(swing_high), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.67(FULL), liquidity=0.40(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **21.4** — location=0.53(swing_low), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.20(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)

**SOL**

- LONG: score **38.0** — location=0.00(swing_high), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.43(FULL), liquidity=0.70(OK), effortresult=0.60(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **20.9** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.70(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

**XRP**

- LONG: score **42.6** — location=0.25(swing_high), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.35(FULL), liquidity=0.41(OK), effortresult=1.00(EXPANSION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **18.9** — location=0.40(swing_low), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.19(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)

## Forward-outcome experiment (cumulative)

- Pressure setups recorded: **591** (active: 0, finalized: 591)

- Valid (FULL) +120s observations: **0** · Partial: **591** · Unobserved windows (excluded, per §14): **0**
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
