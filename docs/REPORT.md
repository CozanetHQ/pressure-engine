# Pressure Engine — Phase A Diagnostic Report

Generated: **2026-10-05T00:04:08.704346+00:00** · model: **pressure_states_v1** (weights PROVISIONAL EQUAL — not locked, no online learning)

> Shadow-only. No trades. Raw forward-collected telemetry. Numbers without FULL-observation sample sizes are not evidence of edge.

## Runtime coverage (GitHub Actions)

- Runs: **2958** · Observed: **179,337.0s** of expected **269,946.0s** → coverage **66.4%**
- Blind gaps recorded: **500**

## Current state by symbol

| Symbol | State | LONG | SHORT | Coverage | OI 1m | CVD 60s | Imb10 | Liquidity | Effort (L/S) | FFP |
|---|---|---|---|---|---|---|---|---|---|---|
| NEAR | NEUTRAL | **37.5** | **27.9** | PARTIAL_TAPE(619) | 15111541 | -641.0 | 0.52 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/ABSORPTION | 0/0 |
| BTC | SHORT_PRESSURE_BUILDING | **35.3** | **29.9** | PARTIAL_TAPE(2916) | 31565 | -4.1 | 0.45 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/UNKNOWN | 0/0 |
| ETH | SHORT_PRESSURE_BUILDING | **20.6** | **19.7** | PARTIAL_TAPE(1421) | 740422 | -83.7 | 0.05 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/ABSORPTION | 0/0 |
| SOL | SHORT_PRESSURE_BUILDING | **44.7** | **43.8** | PARTIAL_TAPE(608) | 3960373 | -3452.8 | 0.45 | CONSUMED_WITH_PRINTS | ABSORPTION/ABSORPTION | 0/0 |
| XRP | SHORT_PRESSURE_BUILDING | **33.9** | **29.2** | PARTIAL_TAPE(464) | 171571289 | -26754.0 | 0.35 | LIQUIDITY_REMOVAL_UNCERTAIN | EXPANSION_/ABSORPTION | 0/0 |

Component status per symbol (latest evaluation):

**NEAR**

- LONG: score **37.5** — location=0.65(swing_high), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.00(FULL), liquidity=0.60(OK), effortresult=0.45(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **27.9** — location=0.79(session_low), positioning=0.35(NO_POSITIONING_INFO), flow=0.34(FULL), liquidity=0.00(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

**BTC**

- LONG: score **35.3** — location=0.00(NO_LEVEL_NEAR), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.00(PARTIAL_TAPE), liquidity=0.57(OK), effortresult=1.00(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **29.9** — location=0.80(session_low), positioning=0.35(NO_POSITIONING_INFO), flow=0.42(PARTIAL_TAPE), liquidity=0.03(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)

**ETH**

- LONG: score **20.6** — location=0.00(NO_LEVEL_NEAR), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.00(PARTIAL_TAPE), liquidity=0.33(OK), effortresult=0.36(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **19.7** — location=0.00(session_low), positioning=0.35(NO_POSITIONING_INFO), flow=0.36(PARTIAL_TAPE), liquidity=0.27(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

**SOL**

- LONG: score **44.7** — location=0.96(swing_high), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.00(PARTIAL_TAPE), liquidity=0.97(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **43.8** — location=0.65(session_low), positioning=0.35(NO_POSITIONING_INFO), flow=1.00(PARTIAL_TAPE), liquidity=0.43(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

**XRP**

- LONG: score **33.9** — location=0.00(NO_LEVEL_NEAR), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.00(FULL), liquidity=0.51(OK), effortresult=0.98(EXPANSION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **29.2** — location=0.63(session_low), positioning=0.35(NO_POSITIONING_INFO), flow=0.48(FULL), liquidity=0.09(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

## Forward-outcome experiment (cumulative)

- Pressure setups recorded: **126** (active: 2, finalized: 124)

- Valid (FULL) +120s observations: **0** · Partial: **124** · Unobserved windows (excluded, per §14): **0**
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
