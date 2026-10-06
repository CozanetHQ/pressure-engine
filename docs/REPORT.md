# Pressure Engine — Phase A Diagnostic Report

Generated: **2026-10-06T14:29:39.674420+00:00** · model: **pressure_states_v1** (weights PROVISIONAL EQUAL — not locked, no online learning)

> Shadow-only. No trades. Raw forward-collected telemetry. Numbers without FULL-observation sample sizes are not evidence of edge.

## Runtime coverage (GitHub Actions)

- Runs: **4384** · Observed: **265,696.0s** of expected **408,277.0s** → coverage **65.1%**
- Blind gaps recorded: **500**

## Current state by symbol

| Symbol | State | LONG | SHORT | Coverage | OI 1m | CVD 60s | Imb10 | Liquidity | Effort (L/S) | FFP |
|---|---|---|---|---|---|---|---|---|---|---|
| NEAR | NEUTRAL | **9.2** | **45.7** | PARTIAL_TAPE(1081) | 15779118 | -3604.0 | -0.53 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/UNKNOWN | 0/0 |
| BTC | LONG_PRESSURE_BUILDING | **27.0** | **35.9** | PARTIAL_TAPE(5607) | 31622 | -4.5 | 0.22 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/UNKNOWN | 0/0 |
| ETH | LONG_PRESSURE_BUILDING | **20.4** | **54.7** | PARTIAL_TAPE(2331) | 750064 | -18.0 | -0.43 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/UNKNOWN | 0/0 |
| SOL | NEUTRAL | **37.9** | **37.9** | PARTIAL_TAPE(914) | 3858979 | -757.7 | -0.32 | CONSUMED_WITH_PRINTS | ABSORPTION/UNKNOWN | 0/0 |
| XRP | SHORT_PRESSURE_CONFIRMED | **28.0** | **49.7** | PARTIAL_TAPE(699) | 174237210 | -93384.0 | 0.10 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/UNKNOWN | 0/0 |

Component status per symbol (latest evaluation):

**NEAR**

- LONG: score **9.2** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.00(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **45.7** — location=0.58(session_low), positioning=0.85(PRICE_WITH_DIR_OI_RISING), flow=0.43(FULL), liquidity=0.60(OK), effortresult=0.28(UNKNOWN), forcedflowproxy=0.00(OK)

**BTC**

- LONG: score **27.0** — location=0.64(swing_high), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(PARTIAL_TAPE), liquidity=0.43(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **35.9** — location=0.00(NO_LEVEL_NEAR), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.43(PARTIAL_TAPE), liquidity=0.17(OK), effortresult=1.00(UNKNOWN), forcedflowproxy=0.00(OK)

**ETH**

- LONG: score **20.4** — location=0.63(swing_high), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(PARTIAL_TAPE), liquidity=0.04(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **54.7** — location=0.86(swing_low), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.32(PARTIAL_TAPE), liquidity=0.56(OK), effortresult=1.00(UNKNOWN), forcedflowproxy=0.00(OK)

**SOL**

- LONG: score **37.9** — location=0.81(swing_high), positioning=0.75(COUNTER_POSITIONS_UNWINDING), flow=0.00(PARTIAL_TAPE), liquidity=0.51(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **37.9** — location=0.00(swing_low), positioning=0.35(NO_POSITIONING_INFO), flow=0.53(PARTIAL_TAPE), liquidity=0.89(OK), effortresult=0.51(UNKNOWN), forcedflowproxy=0.00(OK)

**XRP**

- LONG: score **28.0** — location=0.77(swing_high), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.36(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **49.7** — location=0.91(swing_low), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.73(FULL), liquidity=0.24(OK), effortresult=0.55(UNKNOWN), forcedflowproxy=0.00(OK)

## Forward-outcome experiment (cumulative)

- Pressure setups recorded: **233** (active: 1, finalized: 232)

- Valid (FULL) +120s observations: **0** · Partial: **232** · Unobserved windows (excluded, per §14): **0**
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
