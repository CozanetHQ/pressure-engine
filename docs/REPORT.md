# Pressure Engine — Phase A Diagnostic Report

Generated: **2026-11-06T11:46:53.298981+00:00** · model: **pressure_states_v1** (weights PROVISIONAL EQUAL — not locked, no online learning)

> Shadow-only. No trades. Raw forward-collected telemetry. Numbers without FULL-observation sample sizes are not evidence of edge.

## Runtime coverage (GitHub Actions)

- Runs: **33955** · Observed: **2,060,501.0s** of expected **3,076,911.0s** → coverage **67.0%**
- Blind gaps recorded: **500**

## Current state by symbol

| Symbol | State | LONG | SHORT | Coverage | OI 1m | CVD 60s | Imb10 | Liquidity | Effort (L/S) | FFP |
|---|---|---|---|---|---|---|---|---|---|---|
| NEAR | NEUTRAL | **53.1** | **19.5** | PARTIAL_TAPE(10229) | 16902397 | 3342.0 | 0.13 | CONSUMED_WITH_PRINTS | UNKNOWN/UNKNOWN | 0/0 |
| BTC | NEUTRAL | **17.0** | **32.2** | PARTIAL_TAPE(55695) | 37180 | -0.4 | 0.28 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/UNKNOWN | 0/0 |
| ETH | SHORT_PRESSURE_BUILDING | **19.2** | **34.9** | PARTIAL_TAPE(38811) | 794472 | -159.8 | 0.51 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/UNKNOWN | 0/0 |
| SOL | NEUTRAL | **31.0** | **33.9** | PARTIAL_TAPE(10714) | 4328890 | -193.4 | 0.28 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/UNKNOWN | 0/0 |
| XRP | NEUTRAL | **14.6** | **28.9** | PARTIAL_TAPE(6592) | 190404189 | -18889.0 | 0.05 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/UNKNOWN | 0/0 |

Component status per symbol (latest evaluation):

**NEAR**

- LONG: score **53.1** — location=0.83(swing_high), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.49(FULL), liquidity=0.78(OK), effortresult=0.54(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **19.5** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.62(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)

**BTC**

- LONG: score **17.0** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(PARTIAL_TAPE), liquidity=0.47(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **32.2** — location=0.00(NO_LEVEL_NEAR), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.33(PARTIAL_TAPE), liquidity=0.13(OK), effortresult=0.92(UNKNOWN), forcedflowproxy=0.00(OK)

**ETH**

- LONG: score **19.2** — location=0.00(swing_high), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(PARTIAL_TAPE), liquidity=0.60(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **34.9** — location=0.58(swing_low), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.61(PARTIAL_TAPE), liquidity=0.00(OK), effortresult=0.36(UNKNOWN), forcedflowproxy=0.00(OK)

**SOL**

- LONG: score **31.0** — location=0.84(session_high), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.47(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **33.9** — location=0.00(NO_LEVEL_NEAR), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.35(FULL), liquidity=0.13(OK), effortresult=1.00(UNKNOWN), forcedflowproxy=0.00(OK)

**XRP**

- LONG: score **14.6** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.33(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **28.9** — location=0.00(NO_LEVEL_NEAR), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.38(FULL), liquidity=0.27(OK), effortresult=0.54(UNKNOWN), forcedflowproxy=0.00(OK)

## Forward-outcome experiment (cumulative)

- Pressure setups recorded: **1431** (active: 0, finalized: 1431)

- Valid (FULL) +120s observations: **0** · Partial: **1431** · Unobserved windows (excluded, per §14): **0**
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
