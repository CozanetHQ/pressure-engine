# Pressure Engine — Phase A Diagnostic Report

Generated: **2026-10-06T06:00:40.399288+00:00** · model: **pressure_states_v1** (weights PROVISIONAL EQUAL — not locked, no online learning)

> Shadow-only. No trades. Raw forward-collected telemetry. Numbers without FULL-observation sample sizes are not evidence of edge.

## Runtime coverage (GitHub Actions)

- Runs: **4005** · Observed: **242,759.0s** of expected **377,738.0s** → coverage **64.3%**
- Blind gaps recorded: **500**

## Current state by symbol

| Symbol | State | LONG | SHORT | Coverage | OI 1m | CVD 60s | Imb10 | Liquidity | Effort (L/S) | FFP |
|---|---|---|---|---|---|---|---|---|---|---|
| NEAR | NEUTRAL | **23.8** | **37.4** | PARTIAL_TAPE(984) | 14972716 | -1517.0 | 0.30 | CONSUMED_WITH_PRINTS | UNKNOWN/EXPANSION_ | 0/0 |
| BTC | NEUTRAL | **14.1** | **34.4** | PARTIAL_TAPE(4884) | 31226 | -17.3 | -0.01 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/UNKNOWN | 0/0 |
| ETH | NEUTRAL | **12.0** | **39.1** | PARTIAL_TAPE(2113) | 756877 | -38.4 | -0.22 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/EXPANSION_ | 0/0 |
| SOL | NEUTRAL | **17.6** | **37.7** | PARTIAL_TAPE(801) | 3929782 | -464.3 | -0.32 | CONSUMED_WITH_PRINTS | UNKNOWN/UNKNOWN | 0/0 |
| XRP | NEUTRAL | **19.9** | **40.5** | PARTIAL_TAPE(631) | 174953233 | -1352.0 | -0.21 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/EXPANSION_ | 0/0 |

Component status per symbol (latest evaluation):

**NEAR**

- LONG: score **23.8** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.88(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **37.4** — location=0.00(session_low), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.39(FULL), liquidity=0.52(OK), effortresult=0.79(EXPANSION_CANDIDATE), forcedflowproxy=0.00(OK)

**BTC**

- LONG: score **14.1** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.30(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **34.4** — location=0.00(NO_LEVEL_NEAR), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=1.00(FULL), liquidity=0.30(OK), effortresult=0.21(UNKNOWN), forcedflowproxy=0.00(OK)

**ETH**

- LONG: score **12.0** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.17(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **39.1** — location=0.00(NO_LEVEL_NEAR), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.40(FULL), liquidity=0.43(OK), effortresult=0.96(EXPANSION_CANDIDATE), forcedflowproxy=0.00(OK)

**SOL**

- LONG: score **17.6** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.51(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **37.7** — location=0.00(NO_LEVEL_NEAR), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.52(FULL), liquidity=0.89(OK), effortresult=0.29(UNKNOWN), forcedflowproxy=0.00(OK)

**XRP**

- LONG: score **19.9** — location=0.47(swing_high), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.17(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **40.5** — location=0.11(swing_low), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.34(FULL), liquidity=0.43(OK), effortresult=1.00(EXPANSION_CANDIDATE), forcedflowproxy=0.00(OK)

## Forward-outcome experiment (cumulative)

- Pressure setups recorded: **198** (active: 2, finalized: 196)

- Valid (FULL) +120s observations: **0** · Partial: **196** · Unobserved windows (excluded, per §14): **0**
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
