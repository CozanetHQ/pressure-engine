# Pressure Engine — Phase A Diagnostic Report

Generated: **2026-11-05T08:29:24.354333+00:00** · model: **pressure_states_v1** (weights PROVISIONAL EQUAL — not locked, no online learning)

> Shadow-only. No trades. Raw forward-collected telemetry. Numbers without FULL-observation sample sizes are not evidence of edge.

## Runtime coverage (GitHub Actions)

- Runs: **33123** · Observed: **2,010,011.0s** of expected **2,978,662.0s** → coverage **67.5%**
- Blind gaps recorded: **500**

## Current state by symbol

| Symbol | State | LONG | SHORT | Coverage | OI 1m | CVD 60s | Imb10 | Liquidity | Effort (L/S) | FFP |
|---|---|---|---|---|---|---|---|---|---|---|
| NEAR | NEUTRAL | **31.1** | **30.1** | PARTIAL_TAPE(10030) | 16985500 | 1265.0 | 0.07 | LIQUIDITY_REMOVAL_UNCERTAIN | ABSORPTION/UNKNOWN | 0/0 |
| BTC | NEUTRAL | **9.8** | **40.4** | PARTIAL_TAPE(53279) | 37195 | -1.5 | -0.44 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/UNKNOWN | 0/0 |
| ETH | NEUTRAL | **19.0** | **29.9** | PARTIAL_TAPE(37014) | 794432 | -36.7 | 0.35 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/EXPANSION_ | 0/0 |
| SOL | LONG_PRESSURE_BUILDING | **23.6** | **31.4** | PARTIAL_TAPE(10305) | 4397433 | -843.7 | -0.20 | LIQUIDITY_REMOVAL_UNCERTAIN | ABSORPTION/UNKNOWN | 0/0 |
| XRP | NEUTRAL | **22.4** | **21.0** | PARTIAL_TAPE(6276) | 192040905 | -58.0 | -0.18 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/UNKNOWN | 0/0 |

Component status per symbol (latest evaluation):

**NEAR**

- LONG: score **31.1** — location=0.63(swing_high), positioning=0.35(NO_POSITIONING_INFO), flow=0.34(FULL), liquidity=0.34(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **30.1** — location=0.00(NO_LEVEL_NEAR), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.00(FULL), liquidity=0.26(OK), effortresult=1.00(UNKNOWN), forcedflowproxy=0.00(OK)

**BTC**

- LONG: score **9.8** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(PARTIAL_TAPE), liquidity=0.04(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **40.4** — location=0.00(NO_LEVEL_NEAR), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.33(PARTIAL_TAPE), liquidity=0.56(OK), effortresult=0.98(UNKNOWN), forcedflowproxy=0.00(OK)

**ETH**

- LONG: score **19.0** — location=0.08(swing_high), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(PARTIAL_TAPE), liquidity=0.51(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **29.9** — location=0.00(NO_LEVEL_NEAR), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.36(PARTIAL_TAPE), liquidity=0.09(OK), effortresult=0.80(EXPANSION_CANDIDATE), forcedflowproxy=0.00(OK)

**SOL**

- LONG: score **23.6** — location=0.68(session_high), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(PARTIAL_TAPE), liquidity=0.18(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **31.4** — location=0.00(NO_LEVEL_NEAR), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.56(PARTIAL_TAPE), liquidity=0.42(OK), effortresult=0.35(UNKNOWN), forcedflowproxy=0.00(OK)

**XRP**

- LONG: score **22.4** — location=0.22(session_high), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.01(FULL), liquidity=0.19(OK), effortresult=0.38(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **21.0** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.30(FULL), liquidity=0.41(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)

## Forward-outcome experiment (cumulative)

- Pressure setups recorded: **1395** (active: 1, finalized: 1394)

- Valid (FULL) +120s observations: **0** · Partial: **1394** · Unobserved windows (excluded, per §14): **0**
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
