# Pressure Engine — Phase A Diagnostic Report

Generated: **2026-11-07T15:23:57.199733+00:00** · model: **pressure_states_v1** (weights PROVISIONAL EQUAL — not locked, no online learning)

> Shadow-only. No trades. Raw forward-collected telemetry. Numbers without FULL-observation sample sizes are not evidence of edge.

## Runtime coverage (GitHub Actions)

- Runs: **34928** · Observed: **2,119,565.0s** of expected **3,176,335.0s** → coverage **66.7%**
- Blind gaps recorded: **500**

## Current state by symbol

| Symbol | State | LONG | SHORT | Coverage | OI 1m | CVD 60s | Imb10 | Liquidity | Effort (L/S) | FFP |
|---|---|---|---|---|---|---|---|---|---|---|
| NEAR | NEUTRAL | **27.6** | **20.5** | PARTIAL_TAPE(10338) | 16913794 | 232.0 | 0.29 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/UNKNOWN | 0/0 |
| BTC | NEUTRAL | **15.0** | **35.8** | PARTIAL_TAPE(56931) | 37978 | -0.1 | -0.54 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/UNKNOWN | 0/0 |
| ETH | NEUTRAL | **34.2** | **41.9** | PARTIAL_TAPE(39553) | 800742 | 2.4 | -0.33 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/UNKNOWN | 0/0 |
| SOL | NEUTRAL | **19.2** | **23.6** | PARTIAL_TAPE(10939) | 4291725 | -273.4 | 0.54 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/ABSORPTION | 0/0 |
| XRP | NEUTRAL | **21.0** | **25.6** | PARTIAL_TAPE(6764) | 193826238 | 1792.0 | 0.17 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/UNKNOWN | 0/0 |

Component status per symbol (latest evaluation):

**NEAR**

- LONG: score **27.6** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.34(FULL), liquidity=0.48(OK), effortresult=0.49(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **20.5** — location=0.36(swing_low), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.00(FULL), liquidity=0.12(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)

**BTC**

- LONG: score **15.0** — location=0.15(swing_high), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.00(FULL), liquidity=0.00(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **35.8** — location=0.67(swing_low), positioning=0.35(NO_POSITIONING_INFO), flow=0.33(FULL), liquidity=0.60(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)

**ETH**

- LONG: score **34.2** — location=0.90(swing_high), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.30(FULL), liquidity=0.10(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **41.9** — location=0.66(swing_low), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.50(OK), effortresult=1.00(UNKNOWN), forcedflowproxy=0.00(OK)

**SOL**

- LONG: score **19.2** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.60(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **23.6** — location=0.27(swing_low), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.39(FULL), liquidity=0.00(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

**XRP**

- LONG: score **21.0** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.31(FULL), liquidity=0.40(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **25.6** — location=0.08(swing_low), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.00(FULL), liquidity=0.20(OK), effortresult=0.71(UNKNOWN), forcedflowproxy=0.00(OK)

## Forward-outcome experiment (cumulative)

- Pressure setups recorded: **1481** (active: 0, finalized: 1481)

- Valid (FULL) +120s observations: **0** · Partial: **1481** · Unobserved windows (excluded, per §14): **0**
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
