# Pressure Engine — Phase A Diagnostic Report

Generated: **2026-10-26T01:06:37.609919+00:00** · model: **pressure_states_v1** (weights PROVISIONAL EQUAL — not locked, no online learning)

> Shadow-only. No trades. Raw forward-collected telemetry. Numbers without FULL-observation sample sizes are not evidence of edge.

## Runtime coverage (GitHub Actions)

- Runs: **23810** · Observed: **1,444,988.0s** of expected **2,088,095.0s** → coverage **69.2%**
- Blind gaps recorded: **500**

## Current state by symbol

| Symbol | State | LONG | SHORT | Coverage | OI 1m | CVD 60s | Imb10 | Liquidity | Effort (L/S) | FFP |
|---|---|---|---|---|---|---|---|---|---|---|
| NEAR | NEUTRAL | **19.2** | **23.6** | PARTIAL_TAPE(8078) | 16749817 | -2165.0 | 0.56 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/UNKNOWN | 0/0 |
| BTC | SHORT_PRESSURE_BUILDING | **10.8** | **44.1** | PARTIAL_TAPE | 36519 | -17.3 | -0.34 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/ABSORPTION | 0/0 |
| ETH | SHORT_PRESSURE_BUILDING | **20.7** | **34.4** | PARTIAL_TAPE | 763616 | -157.4 | -0.01 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/UNKNOWN | 0/0 |
| SOL | NEUTRAL | **17.6** | **50.2** | PARTIAL_TAPE(7421) | 4105699 | 433.9 | -0.91 | LIQUIDITY_REMOVAL_UNCERTAIN | ABSORPTION/EXPANSION_ | 0/0 |
| XRP | NEUTRAL | **20.6** | **38.9** | PARTIAL_TAPE(4732) | 176788123 | -214896.0 | -0.08 | LIQUIDITY_REMOVAL_UNCERTAIN | ABSORPTION/ABSORPTION | 0/0 |

Component status per symbol (latest evaluation):

**NEAR**

- LONG: score **19.2** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.60(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **23.6** — location=0.17(session_low), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.37(FULL), liquidity=0.00(OK), effortresult=0.33(UNKNOWN), forcedflowproxy=0.00(OK)

**BTC**

- LONG: score **10.8** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(PARTIAL_TAPE), liquidity=0.10(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **44.1** — location=0.59(swing_low), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.80(PARTIAL_TAPE), liquidity=0.51(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

**ETH**

- LONG: score **20.7** — location=0.00(NO_LEVEL_NEAR), positioning=0.75(COUNTER_POSITIONS_UNWINDING), flow=0.00(PARTIAL_TAPE), liquidity=0.29(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **34.4** — location=0.60(swing_low), positioning=0.35(NO_POSITIONING_INFO), flow=0.52(PARTIAL_TAPE), liquidity=0.31(OK), effortresult=0.29(UNKNOWN), forcedflowproxy=0.00(OK)

**SOL**

- LONG: score **17.6** — location=0.11(swing_high), positioning=0.35(NO_POSITIONING_INFO), flow=0.40(FULL), liquidity=0.00(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **50.2** — location=0.90(swing_low), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.00(FULL), liquidity=0.60(OK), effortresult=0.96(EXPANSION_CANDIDATE), forcedflowproxy=0.00(OK)

**XRP**

- LONG: score **20.6** — location=0.43(swing_high), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(PARTIAL_TAPE), liquidity=0.25(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **38.9** — location=0.24(swing_low), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=1.00(PARTIAL_TAPE), liquidity=0.35(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

## Forward-outcome experiment (cumulative)

- Pressure setups recorded: **1054** (active: 1, finalized: 1053)

- Valid (FULL) +120s observations: **0** · Partial: **1053** · Unobserved windows (excluded, per §14): **0**
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
