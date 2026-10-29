# Pressure Engine — Phase A Diagnostic Report

Generated: **2026-10-29T01:29:48.059113+00:00** · model: **pressure_states_v1** (weights PROVISIONAL EQUAL — not locked, no online learning)

> Shadow-only. No trades. Raw forward-collected telemetry. Numbers without FULL-observation sample sizes are not evidence of edge.

## Runtime coverage (GitHub Actions)

- Runs: **26656** · Observed: **1,617,707.0s** of expected **2,348,686.0s** → coverage **68.9%**
- Blind gaps recorded: **500**

## Current state by symbol

| Symbol | State | LONG | SHORT | Coverage | OI 1m | CVD 60s | Imb10 | Liquidity | Effort (L/S) | FFP |
|---|---|---|---|---|---|---|---|---|---|---|
| NEAR | SHORT_PRESSURE_BUILDING | **36.1** | **47.9** | PARTIAL_TAPE(8603) | 16538043 | -11927.0 | 0.43 | CONSUMED_WITH_PRINTS | UNKNOWN/UNKNOWN | 0/0 |
| BTC | NEUTRAL | **20.9** | **48.2** | PARTIAL_TAPE(41506) | 35918 | 1.0 | -0.61 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/UNKNOWN | 0/0 |
| ETH | NEUTRAL | **30.6** | **41.5** | PARTIAL_TAPE(29207) | 776882 | -22.9 | -0.61 | CONSUMED_WITH_PRINTS | UNKNOWN/UNKNOWN | 0/0 |
| SOL | NEUTRAL | **18.2** | **31.4** | PARTIAL_TAPE(8129) | 4240305 | -241.9 | -0.01 | LIQUIDITY_REMOVAL_UNCERTAIN | ABSORPTION/UNKNOWN | 0/0 |
| XRP | NEUTRAL | **34.4** | **29.1** | PARTIAL_TAPE(5142) | 183668083 | 5746.0 | 0.18 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/UNKNOWN | 0/0 |

Component status per symbol (latest evaluation):

**NEAR**

- LONG: score **36.1** — location=0.66(swing_high), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.96(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **47.9** — location=0.85(swing_low), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.75(FULL), liquidity=0.44(OK), effortresult=0.28(UNKNOWN), forcedflowproxy=0.00(OK)

**BTC**

- LONG: score **20.9** — location=0.36(swing_high), positioning=0.35(NO_POSITIONING_INFO), flow=0.34(FULL), liquidity=0.00(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **48.2** — location=0.75(swing_low), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.00(FULL), liquidity=0.60(OK), effortresult=0.99(UNKNOWN), forcedflowproxy=0.00(OK)

**ETH**

- LONG: score **30.6** — location=0.69(swing_high), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.00(FULL), liquidity=0.40(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **41.5** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.33(FULL), liquidity=1.00(OK), effortresult=0.81(UNKNOWN), forcedflowproxy=0.00(OK)

**SOL**

- LONG: score **18.2** — location=0.25(swing_high), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.29(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **31.4** — location=0.00(NO_LEVEL_NEAR), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.38(FULL), liquidity=0.31(OK), effortresult=0.64(UNKNOWN), forcedflowproxy=0.00(OK)

**XRP**

- LONG: score **34.4** — location=0.78(swing_high), positioning=0.35(NO_POSITIONING_INFO), flow=0.33(FULL), liquidity=0.41(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **29.1** — location=0.00(NO_LEVEL_NEAR), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.00(FULL), liquidity=0.19(OK), effortresult=1.00(UNKNOWN), forcedflowproxy=0.00(OK)

## Forward-outcome experiment (cumulative)

- Pressure setups recorded: **1167** (active: 0, finalized: 1167)

- Valid (FULL) +120s observations: **0** · Partial: **1167** · Unobserved windows (excluded, per §14): **0**
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
