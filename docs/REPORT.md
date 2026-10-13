# Pressure Engine — Phase A Diagnostic Report

Generated: **2026-10-13T02:23:42.828797+00:00** · model: **pressure_states_v1** (weights PROVISIONAL EQUAL — not locked, no online learning)

> Shadow-only. No trades. Raw forward-collected telemetry. Numbers without FULL-observation sample sizes are not evidence of edge.

## Runtime coverage (GitHub Actions)

- Runs: **10970** · Observed: **665,549.0s** of expected **969,520.0s** → coverage **68.6%**
- Blind gaps recorded: **500**

## Current state by symbol

| Symbol | State | LONG | SHORT | Coverage | OI 1m | CVD 60s | Imb10 | Liquidity | Effort (L/S) | FFP |
|---|---|---|---|---|---|---|---|---|---|---|
| NEAR | NEUTRAL | **38.6** | **24.5** | PARTIAL_TAPE(4445) | 15830334 | 11754.0 | -0.36 | CONSUMED_WITH_PRINTS | EXPANSION_/UNKNOWN | 0/0 |
| BTC | NEUTRAL | **37.8** | **12.3** | PARTIAL_TAPE(15571) | 33746 | 0.3 | 0.20 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/UNKNOWN | 0/0 |
| ETH | NEUTRAL | **30.8** | **24.9** | PARTIAL_TAPE(8253) | 752354 | 1641.0 | -0.41 | LIQUIDITY_REMOVAL_UNCERTAIN | ABSORPTION/ABSORPTION | 0/0 |
| SOL | NEUTRAL | **23.3** | **25.8** | PARTIAL_TAPE(3224) | 4031666 | 779.6 | -0.78 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/ABSORPTION | 0/0 |
| XRP | LONG_PRESSURE_BUILDING | **46.5** | **11.1** | PARTIAL_TAPE(2309) | 174057679 | 50478.0 | 0.30 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/UNKNOWN | 0/0 |

Component status per symbol (latest evaluation):

**NEAR**

- LONG: score **38.6** — location=0.00(NO_LEVEL_NEAR), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.49(PARTIAL_TAPE), liquidity=0.48(OK), effortresult=0.79(EXPANSION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **24.5** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(PARTIAL_TAPE), liquidity=0.92(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)

**BTC**

- LONG: score **37.8** — location=0.00(swing_high), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.30(PARTIAL_TAPE), liquidity=0.42(OK), effortresult=1.00(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **12.3** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(PARTIAL_TAPE), liquidity=0.18(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)

**ETH**

- LONG: score **30.8** — location=0.25(session_high), positioning=0.35(NO_POSITIONING_INFO), flow=1.00(PARTIAL_TAPE), liquidity=0.05(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **24.9** — location=0.00(NO_LEVEL_NEAR), positioning=0.75(COUNTER_POSITIONS_UNWINDING), flow=0.00(PARTIAL_TAPE), liquidity=0.55(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

**SOL**

- LONG: score **23.3** — location=0.24(session_high), positioning=0.35(NO_POSITIONING_INFO), flow=0.46(PARTIAL_TAPE), liquidity=0.00(OK), effortresult=0.35(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **25.8** — location=0.00(NO_LEVEL_NEAR), positioning=0.75(COUNTER_POSITIONS_UNWINDING), flow=0.00(PARTIAL_TAPE), liquidity=0.60(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

**XRP**

- LONG: score **46.5** — location=0.39(session_high), positioning=0.85(PRICE_WITH_DIR_OI_RISING), flow=0.49(FULL), liquidity=0.48(OK), effortresult=0.58(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **11.1** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.12(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)

## Forward-outcome experiment (cumulative)

- Pressure setups recorded: **557** (active: 0, finalized: 557)

- Valid (FULL) +120s observations: **0** · Partial: **557** · Unobserved windows (excluded, per §14): **0**
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
