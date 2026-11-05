# Pressure Engine — Phase A Diagnostic Report

Generated: **2026-11-05T15:11:04.015288+00:00** · model: **pressure_states_v1** (weights PROVISIONAL EQUAL — not locked, no online learning)

> Shadow-only. No trades. Raw forward-collected telemetry. Numbers without FULL-observation sample sizes are not evidence of edge.

## Runtime coverage (GitHub Actions)

- Runs: **33384** · Observed: **2,025,837.0s** of expected **3,002,761.0s** → coverage **67.5%**
- Blind gaps recorded: **500**

## Current state by symbol

| Symbol | State | LONG | SHORT | Coverage | OI 1m | CVD 60s | Imb10 | Liquidity | Effort (L/S) | FFP |
|---|---|---|---|---|---|---|---|---|---|---|
| NEAR | NEUTRAL | **16.9** | **42.8** | PARTIAL_TAPE(10079) | 16835668 | -71685.0 | -0.40 | LIQUIDITY_REMOVAL_UNCERTAIN | ABSORPTION/ABSORPTION | 0/0 |
| BTC | SHORT_PRESSURE_BUILDING | **22.5** | **50.3** | PARTIAL_TAPE | 36766 | -14.5 | -0.80 | CONSUMED_WITH_PRINTS | ABSORPTION/UNKNOWN | 0/0 |
| ETH | NEUTRAL | **22.5** | **46.5** | PARTIAL_TAPE | 774120 | -275.9 | -0.87 | CONSUMED_WITH_PRINTS | ABSORPTION/UNKNOWN | 0/0 |
| SOL | SHORT_PRESSURE_BUILDING | **31.4** | **36.9** | PARTIAL_TAPE(10430) | 4328616 | 930.6 | -0.61 | CONSUMED_WITH_PRINTS | ABSORPTION/UNKNOWN | 0/0 |
| XRP | SHORT_PRESSURE_BUILDING | **22.6** | **36.1** | PARTIAL_TAPE(6362) | 192551305 | -117186.0 | 0.18 | LIQUIDITY_REMOVAL_UNCERTAIN | ABSORPTION/UNKNOWN | 0/0 |

Component status per symbol (latest evaluation):

**NEAR**

- LONG: score **16.9** — location=0.00(NO_LEVEL_NEAR), positioning=0.75(COUNTER_POSITIONS_UNWINDING), flow=0.00(PARTIAL_TAPE), liquidity=0.06(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **42.8** — location=0.48(session_low), positioning=0.35(NO_POSITIONING_INFO), flow=1.00(PARTIAL_TAPE), liquidity=0.54(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

**BTC**

- LONG: score **22.5** — location=0.00(NO_LEVEL_NEAR), positioning=0.75(COUNTER_POSITIONS_UNWINDING), flow=0.00(PARTIAL_TAPE), liquidity=0.40(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **50.3** — location=0.68(session_low), positioning=0.35(NO_POSITIONING_INFO), flow=0.71(PARTIAL_TAPE), liquidity=1.00(OK), effortresult=0.28(UNKNOWN), forcedflowproxy=0.00(OK)

**ETH**

- LONG: score **22.5** — location=0.00(NO_LEVEL_NEAR), positioning=0.75(COUNTER_POSITIONS_UNWINDING), flow=0.00(PARTIAL_TAPE), liquidity=0.40(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **46.5** — location=0.38(session_low), positioning=0.35(NO_POSITIONING_INFO), flow=0.58(PARTIAL_TAPE), liquidity=1.00(OK), effortresult=0.48(UNKNOWN), forcedflowproxy=0.00(OK)

**SOL**

- LONG: score **31.4** — location=0.00(NO_LEVEL_NEAR), positioning=0.75(COUNTER_POSITIONS_UNWINDING), flow=0.53(PARTIAL_TAPE), liquidity=0.40(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **36.9** — location=0.40(session_low), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(PARTIAL_TAPE), liquidity=1.00(OK), effortresult=0.46(UNKNOWN), forcedflowproxy=0.00(OK)

**XRP**

- LONG: score **22.6** — location=0.00(NO_LEVEL_NEAR), positioning=0.75(COUNTER_POSITIONS_UNWINDING), flow=0.00(PARTIAL_TAPE), liquidity=0.41(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **36.1** — location=0.66(session_low), positioning=0.35(NO_POSITIONING_INFO), flow=0.73(PARTIAL_TAPE), liquidity=0.19(OK), effortresult=0.23(UNKNOWN), forcedflowproxy=0.00(OK)

## Forward-outcome experiment (cumulative)

- Pressure setups recorded: **1412** (active: 2, finalized: 1410)

- Valid (FULL) +120s observations: **0** · Partial: **1410** · Unobserved windows (excluded, per §14): **0**
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
