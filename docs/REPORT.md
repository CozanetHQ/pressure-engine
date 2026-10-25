# Pressure Engine — Phase A Diagnostic Report

Generated: **2026-10-25T22:15:36.515305+00:00** · model: **pressure_states_v1** (weights PROVISIONAL EQUAL — not locked, no online learning)

> Shadow-only. No trades. Raw forward-collected telemetry. Numbers without FULL-observation sample sizes are not evidence of edge.

## Runtime coverage (GitHub Actions)

- Runs: **23689** · Observed: **1,437,657.0s** of expected **2,077,834.0s** → coverage **69.2%**
- Blind gaps recorded: **500**

## Current state by symbol

| Symbol | State | LONG | SHORT | Coverage | OI 1m | CVD 60s | Imb10 | Liquidity | Effort (L/S) | FFP |
|---|---|---|---|---|---|---|---|---|---|---|
| NEAR | NEUTRAL | **23.9** | **35.6** | PARTIAL_TAPE(8054) | 16607669 | -3937.0 | -0.36 | CONSUMED_WITH_PRINTS | ABSORPTION/ABSORPTION | 0/0 |
| BTC | LONG_PRESSURE_BUILDING | **46.5** | **27.0** | PARTIAL_TAPE | 36023 | 9.5 | 0.97 | LIQUIDITY_REMOVAL_UNCERTAIN | ABSORPTION/ABSORPTION | 0/0 |
| ETH | SHORT_PRESSURE_BUILDING | **24.9** | **34.3** | PARTIAL_TAPE(24740) | 758913 | -89.5 | -0.23 | LIQUIDITY_REMOVAL_UNCERTAIN | ABSORPTION/ABSORPTION | 0/0 |
| SOL | NEUTRAL | **19.1** | **43.2** | PARTIAL_TAPE(7396) | 4112440 | -120.6 | 0.20 | LIQUIDITY_REMOVAL_UNCERTAIN | ABSORPTION/UNKNOWN | 0/0 |
| XRP | NEUTRAL | **15.9** | **50.4** | PARTIAL_TAPE(4714) | 176658620 | -4496.0 | 0.17 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/UNKNOWN | 0/0 |

Component status per symbol (latest evaluation):

**NEAR**

- LONG: score **23.9** — location=0.00(swing_high), positioning=0.75(COUNTER_POSITIONS_UNWINDING), flow=0.00(FULL), liquidity=0.49(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **35.6** — location=0.26(swing_low), positioning=0.35(NO_POSITIONING_INFO), flow=0.41(FULL), liquidity=0.91(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

**BTC**

- LONG: score **46.5** — location=0.92(swing_high), positioning=0.35(NO_POSITIONING_INFO), flow=0.72(PARTIAL_TAPE), liquidity=0.60(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **27.0** — location=0.57(swing_low), positioning=0.85(PRICE_WITH_DIR_OI_RISING), flow=0.00(PARTIAL_TAPE), liquidity=0.00(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

**ETH**

- LONG: score **24.9** — location=0.78(swing_high), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(PARTIAL_TAPE), liquidity=0.16(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **34.3** — location=0.44(swing_low), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.43(PARTIAL_TAPE), liquidity=0.44(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

**SOL**

- LONG: score **19.1** — location=0.17(swing_high), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.42(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **43.2** — location=0.98(swing_low), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.33(FULL), liquidity=0.18(OK), effortresult=0.55(UNKNOWN), forcedflowproxy=0.00(OK)

**XRP**

- LONG: score **15.9** — location=0.00(swing_high), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.40(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **50.4** — location=0.95(swing_low), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.33(FULL), liquidity=0.20(OK), effortresult=1.00(UNKNOWN), forcedflowproxy=0.00(OK)

## Forward-outcome experiment (cumulative)

- Pressure setups recorded: **1046** (active: 0, finalized: 1046)

- Valid (FULL) +120s observations: **0** · Partial: **1046** · Unobserved windows (excluded, per §14): **0**
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
