# Pressure Engine — Phase A Diagnostic Report

Generated: **2026-10-14T14:50:00.785659+00:00** · model: **pressure_states_v1** (weights PROVISIONAL EQUAL — not locked, no online learning)

> Shadow-only. No trades. Raw forward-collected telemetry. Numbers without FULL-observation sample sizes are not evidence of edge.

## Runtime coverage (GitHub Actions)

- Runs: **12554** · Observed: **762,050.0s** of expected **1,100,698.0s** → coverage **69.2%**
- Blind gaps recorded: **500**

## Current state by symbol

| Symbol | State | LONG | SHORT | Coverage | OI 1m | CVD 60s | Imb10 | Liquidity | Effort (L/S) | FFP |
|---|---|---|---|---|---|---|---|---|---|---|
| NEAR | SHORT_PRESSURE_BUILDING | **13.0** | **48.5** | PARTIAL_TAPE(5075) | 16040022 | -8056.0 | -0.12 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/UNKNOWN | 0/0 |
| BTC | NEUTRAL | **24.9** | **23.6** | PARTIAL_TAPE | 33405 | 3.2 | 0.42 | LIQUIDITY_REMOVAL_UNCERTAIN | ABSORPTION/EXPANSION_ | 0/0 |
| ETH | NEUTRAL | **21.9** | **47.2** | PARTIAL_TAPE | 779255 | -324.3 | 0.10 | CONSUMED_WITH_PRINTS | UNKNOWN/EXPANSION_ | 0/0 |
| SOL | NEUTRAL | **34.2** | **31.8** | PARTIAL_TAPE(3921) | 4025937 | 3873.5 | 0.34 | LIQUIDITY_REMOVAL_UNCERTAIN | ABSORPTION/EXPANSION_ | 0/0 |
| XRP | NEUTRAL | **17.6** | **33.9** | PARTIAL_TAPE(2675) | 176071940 | -29063.0 | 0.35 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/UNKNOWN | 0/0 |

Component status per symbol (latest evaluation):

**NEAR**

- LONG: score **13.0** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(PARTIAL_TAPE), liquidity=0.23(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **48.5** — location=0.92(swing_low), positioning=0.85(PRICE_WITH_DIR_OI_RISING), flow=0.52(PARTIAL_TAPE), liquidity=0.37(OK), effortresult=0.25(UNKNOWN), forcedflowproxy=0.00(OK)

**BTC**

- LONG: score **24.9** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.39(PARTIAL_TAPE), liquidity=0.55(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **23.6** — location=0.00(session_low), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.00(PARTIAL_TAPE), liquidity=0.05(OK), effortresult=0.81(EXPANSION_CANDIDATE), forcedflowproxy=0.00(OK)

**ETH**

- LONG: score **21.9** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(PARTIAL_TAPE), liquidity=0.76(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **47.2** — location=0.00(NO_LEVEL_NEAR), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.64(PARTIAL_TAPE), liquidity=0.64(OK), effortresult=1.00(EXPANSION_CANDIDATE), forcedflowproxy=0.00(OK)

**SOL**

- LONG: score **34.2** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=1.00(PARTIAL_TAPE), liquidity=0.50(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **31.8** — location=0.00(NO_LEVEL_NEAR), positioning=0.85(PRICE_WITH_DIR_OI_RISING), flow=0.00(PARTIAL_TAPE), liquidity=0.10(OK), effortresult=0.96(EXPANSION_CANDIDATE), forcedflowproxy=0.00(OK)

**XRP**

- LONG: score **17.6** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.51(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **33.9** — location=0.00(NO_LEVEL_NEAR), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.39(FULL), liquidity=0.09(OK), effortresult=1.00(UNKNOWN), forcedflowproxy=0.00(OK)

## Forward-outcome experiment (cumulative)

- Pressure setups recorded: **634** (active: 2, finalized: 632)

- Valid (FULL) +120s observations: **0** · Partial: **632** · Unobserved windows (excluded, per §14): **0**
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
