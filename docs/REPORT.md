# Pressure Engine — Phase A Diagnostic Report

Generated: **2026-10-23T14:04:00.746170+00:00** · model: **pressure_states_v1** (weights PROVISIONAL EQUAL — not locked, no online learning)

> Shadow-only. No trades. Raw forward-collected telemetry. Numbers without FULL-observation sample sizes are not evidence of edge.

## Runtime coverage (GitHub Actions)

- Runs: **21334** · Observed: **1,294,816.0s** of expected **1,875,538.0s** → coverage **69.0%**
- Blind gaps recorded: **500**

## Current state by symbol

| Symbol | State | LONG | SHORT | Coverage | OI 1m | CVD 60s | Imb10 | Liquidity | Effort (L/S) | FFP |
|---|---|---|---|---|---|---|---|---|---|---|
| NEAR | NEUTRAL | **46.0** | **32.7** | PARTIAL_TAPE(7626) | 16550140 | -5568.0 | 0.26 | CONSUMED_WITH_PRINTS | UNKNOWN/ABSORPTION | 0/0 |
| BTC | LONG_PRESSURE_BUILDING | **24.6** | **30.8** | PARTIAL_TAPE(33248) | 36522 | -2.8 | -0.94 | LIQUIDITY_REMOVAL_UNCERTAIN | ABSORPTION/UNKNOWN | 0/0 |
| ETH | NEUTRAL | **38.3** | **32.0** | PARTIAL_TAPE(21364) | 760138 | -264.9 | -0.05 | CONSUMED_WITH_PRINTS | UNKNOWN/ABSORPTION | 0/0 |
| SOL | LONG_PRESSURE_BUILDING | **28.3** | **23.4** | PARTIAL_TAPE(6864) | 4119427 | -918.8 | 0.01 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/ABSORPTION | 0/0 |
| XRP | LONG_PRESSURE_BUILDING | **19.8** | **41.6** | PARTIAL_TAPE(4459) | 176560866 | -17484.0 | 0.08 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/UNKNOWN | 0/0 |

Component status per symbol (latest evaluation):

**NEAR**

- LONG: score **46.0** — location=0.89(swing_high), positioning=0.75(COUNTER_POSITIONS_UNWINDING), flow=0.00(FULL), liquidity=0.86(OK), effortresult=0.27(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **32.7** — location=0.32(swing_low), positioning=0.35(NO_POSITIONING_INFO), flow=0.55(FULL), liquidity=0.54(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

**BTC**

- LONG: score **24.6** — location=0.93(swing_high), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(PARTIAL_TAPE), liquidity=0.00(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **30.8** — location=0.00(NO_LEVEL_NEAR), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.39(PARTIAL_TAPE), liquidity=0.60(OK), effortresult=0.31(UNKNOWN), forcedflowproxy=0.00(OK)

**ETH**

- LONG: score **38.3** — location=0.88(swing_high), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.00(PARTIAL_TAPE), liquidity=0.67(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **32.0** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.64(PARTIAL_TAPE), liquidity=0.73(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

**SOL**

- LONG: score **28.3** — location=0.04(session_high), positioning=0.75(COUNTER_POSITIONS_UNWINDING), flow=0.00(PARTIAL_TAPE), liquidity=0.31(OK), effortresult=0.61(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **23.4** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.56(PARTIAL_TAPE), liquidity=0.29(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

**XRP**

- LONG: score **19.8** — location=0.29(swing_high), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.35(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **41.6** — location=0.42(swing_low), positioning=0.85(PRICE_WITH_DIR_OI_RISING), flow=0.42(FULL), liquidity=0.25(OK), effortresult=0.56(UNKNOWN), forcedflowproxy=0.00(OK)

## Forward-outcome experiment (cumulative)

- Pressure setups recorded: **974** (active: 0, finalized: 974)

- Valid (FULL) +120s observations: **0** · Partial: **974** · Unobserved windows (excluded, per §14): **0**
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
