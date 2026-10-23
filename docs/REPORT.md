# Pressure Engine — Phase A Diagnostic Report

Generated: **2026-10-23T19:56:01.695597+00:00** · model: **pressure_states_v1** (weights PROVISIONAL EQUAL — not locked, no online learning)

> Shadow-only. No trades. Raw forward-collected telemetry. Numbers without FULL-observation sample sizes are not evidence of edge.

## Runtime coverage (GitHub Actions)

- Runs: **21553** · Observed: **1,308,155.0s** of expected **1,896,659.0s** → coverage **69.0%**
- Blind gaps recorded: **500**

## Current state by symbol

| Symbol | State | LONG | SHORT | Coverage | OI 1m | CVD 60s | Imb10 | Liquidity | Effort (L/S) | FFP |
|---|---|---|---|---|---|---|---|---|---|---|
| NEAR | NEUTRAL | **20.0** | **33.7** | PARTIAL_TAPE(7683) | 16480974 | -237.0 | -0.08 | CONSUMED_WITH_PRINTS | UNKNOWN/UNKNOWN | 0/0 |
| BTC | NEUTRAL | **9.7** | **42.5** | PARTIAL_TAPE(33848) | 36200 | -2.6 | -0.45 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/ABSORPTION | 0/0 |
| ETH | NEUTRAL | **14.5** | **41.8** | PARTIAL_TAPE(21950) | 759966 | -3.0 | -0.63 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/UNKNOWN | 0/0 |
| SOL | NEUTRAL | **17.9** | **19.4** | PARTIAL_TAPE(6945) | 4117866 | -147.0 | 0.38 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/UNKNOWN | 0/0 |
| XRP | NEUTRAL | **15.4** | **31.9** | PARTIAL_TAPE(4515) | 174810500 | -7121.0 | 0.12 | LIQUIDITY_REMOVAL_UNCERTAIN | ABSORPTION/UNKNOWN | 0/0 |

Component status per symbol (latest evaluation):

**NEAR**

- LONG: score **20.0** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.65(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **33.7** — location=0.00(NO_LEVEL_NEAR), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.30(FULL), liquidity=0.75(OK), effortresult=0.42(UNKNOWN), forcedflowproxy=0.00(OK)

**BTC**

- LONG: score **9.7** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(PARTIAL_TAPE), liquidity=0.03(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **42.5** — location=0.84(swing_low), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.39(PARTIAL_TAPE), liquidity=0.57(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

**ETH**

- LONG: score **14.5** — location=0.30(swing_high), positioning=0.35(NO_POSITIONING_INFO), flow=0.02(PARTIAL_TAPE), liquidity=0.00(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **41.8** — location=0.86(swing_low), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.30(PARTIAL_TAPE), liquidity=0.60(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)

**SOL**

- LONG: score **17.9** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.53(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **19.4** — location=0.00(session_low), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.33(FULL), liquidity=0.07(OK), effortresult=0.21(UNKNOWN), forcedflowproxy=0.00(OK)

**XRP**

- LONG: score **15.4** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.37(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **31.9** — location=0.52(swing_low), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.33(FULL), liquidity=0.23(OK), effortresult=0.29(UNKNOWN), forcedflowproxy=0.00(OK)

## Forward-outcome experiment (cumulative)

- Pressure setups recorded: **992** (active: 0, finalized: 992)

- Valid (FULL) +120s observations: **0** · Partial: **992** · Unobserved windows (excluded, per §14): **0**
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
