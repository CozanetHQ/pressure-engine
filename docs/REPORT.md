# Pressure Engine — Phase A Diagnostic Report

Generated: **2026-10-14T06:25:21.714005+00:00** · model: **pressure_states_v1** (weights PROVISIONAL EQUAL — not locked, no online learning)

> Shadow-only. No trades. Raw forward-collected telemetry. Numbers without FULL-observation sample sizes are not evidence of edge.

## Runtime coverage (GitHub Actions)

- Runs: **12188** · Observed: **739,787.0s** of expected **1,070,419.0s** → coverage **69.1%**
- Blind gaps recorded: **500**

## Current state by symbol

| Symbol | State | LONG | SHORT | Coverage | OI 1m | CVD 60s | Imb10 | Liquidity | Effort (L/S) | FFP |
|---|---|---|---|---|---|---|---|---|---|---|
| NEAR | NEUTRAL | **22.6** | **25.8** | PARTIAL_TAPE(4883) | 16247410 | -3046.0 | 0.07 | LIQUIDITY_REMOVAL_UNCERTAIN | ABSORPTION/UNKNOWN | 0/0 |
| BTC | NEUTRAL | **17.5** | **34.5** | PARTIAL_TAPE(17838) | 32201 | -12.6 | -0.53 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/ABSORPTION | 0/0 |
| ETH | NEUTRAL | **27.5** | **40.6** | PARTIAL_TAPE(9385) | 750071 | 141.8 | 0.18 | LIQUIDITY_REMOVAL_UNCERTAIN | ABSORPTION/UNKNOWN | 0/0 |
| SOL | NEUTRAL | **28.8** | **15.0** | PARTIAL_TAPE(3615) | 4015381 | 183.6 | 0.49 | LIQUIDITY_REMOVAL_UNCERTAIN | ABSORPTION/UNKNOWN | 0/0 |
| XRP | LONG_PRESSURE_BUILDING | **31.6** | **20.2** | PARTIAL_TAPE(2511) | 176668195 | -23703.0 | 0.06 | LIQUIDITY_REMOVAL_UNCERTAIN | ABSORPTION/ABSORPTION | 0/0 |

Component status per symbol (latest evaluation):

**NEAR**

- LONG: score **22.6** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.46(FULL), liquidity=0.34(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **25.8** — location=0.00(swing_low), positioning=0.85(PRICE_WITH_DIR_OI_RISING), flow=0.00(FULL), liquidity=0.26(OK), effortresult=0.44(UNKNOWN), forcedflowproxy=0.00(OK)

**BTC**

- LONG: score **17.5** — location=0.00(swing_high), positioning=0.85(PRICE_WITH_DIR_OI_RISING), flow=0.00(PARTIAL_TAPE), liquidity=0.00(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **34.5** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.92(PARTIAL_TAPE), liquidity=0.60(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

**ETH**

- LONG: score **27.5** — location=0.00(NO_LEVEL_NEAR), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.49(PARTIAL_TAPE), liquidity=0.41(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **40.6** — location=0.89(swing_low), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(PARTIAL_TAPE), liquidity=0.19(OK), effortresult=1.00(UNKNOWN), forcedflowproxy=0.00(OK)

**SOL**

- LONG: score **28.8** — location=0.00(NO_LEVEL_NEAR), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.38(PARTIAL_TAPE), liquidity=0.59(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **15.0** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(PARTIAL_TAPE), liquidity=0.01(OK), effortresult=0.54(UNKNOWN), forcedflowproxy=0.00(OK)

**XRP**

- LONG: score **31.6** — location=0.51(swing_high), positioning=0.85(PRICE_WITH_DIR_OI_RISING), flow=0.00(FULL), liquidity=0.34(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **20.2** — location=0.00(swing_low), positioning=0.35(NO_POSITIONING_INFO), flow=0.40(FULL), liquidity=0.26(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

## Forward-outcome experiment (cumulative)

- Pressure setups recorded: **598** (active: 0, finalized: 598)

- Valid (FULL) +120s observations: **0** · Partial: **598** · Unobserved windows (excluded, per §14): **0**
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
