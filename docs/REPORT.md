# Pressure Engine — Phase A Diagnostic Report

Generated: **2026-11-01T03:46:32.689574+00:00** · model: **pressure_states_v1** (weights PROVISIONAL EQUAL — not locked, no online learning)

> Shadow-only. No trades. Raw forward-collected telemetry. Numbers without FULL-observation sample sizes are not evidence of edge.

## Runtime coverage (GitHub Actions)

- Runs: **29517** · Observed: **1,791,237.0s** of expected **2,616,090.0s** → coverage **68.5%**
- Blind gaps recorded: **500**

## Current state by symbol

| Symbol | State | LONG | SHORT | Coverage | OI 1m | CVD 60s | Imb10 | Liquidity | Effort (L/S) | FFP |
|---|---|---|---|---|---|---|---|---|---|---|
| NEAR | SHORT_PRESSURE_BUILDING | **16.6** | **43.3** | PARTIAL_TAPE(9481) | 16258528 | 1034.0 | -0.38 | LIQUIDITY_REMOVAL_UNCERTAIN | ABSORPTION/EXPANSION_ | 0/0 |
| BTC | NEUTRAL | **9.3** | **43.5** | PARTIAL_TAPE(47782) | 37033 | -2.3 | -0.48 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/EXPANSION_ | 0/0 |
| ETH | NEUTRAL | **16.0** | **36.3** | PARTIAL_TAPE(33716) | 775564 | -67.0 | 0.18 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/EXPANSION_ | 0/0 |
| SOL | NEUTRAL | **20.7** | **40.8** | PARTIAL_TAPE(9410) | 4222724 | 26.3 | -0.05 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/EXPANSION_ | 0/0 |
| XRP | NEUTRAL | **25.0** | **39.2** | PARTIAL_TAPE(5862) | 184449886 | -14982.0 | -0.03 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/EXPANSION_ | 0/0 |

Component status per symbol (latest evaluation):

**NEAR**

- LONG: score **16.6** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.37(FULL), liquidity=0.07(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **43.3** — location=0.53(session_low), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.00(FULL), liquidity=0.53(OK), effortresult=0.99(EXPANSION_CANDIDATE), forcedflowproxy=0.00(OK)

**BTC**

- LONG: score **9.3** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.01(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **43.5** — location=0.00(NO_LEVEL_NEAR), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.47(FULL), liquidity=0.59(OK), effortresult=1.00(EXPANSION_CANDIDATE), forcedflowproxy=0.00(OK)

**ETH**

- LONG: score **16.0** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.41(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **36.3** — location=0.00(NO_LEVEL_NEAR), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.44(FULL), liquidity=0.19(OK), effortresult=1.00(EXPANSION_CANDIDATE), forcedflowproxy=0.00(OK)

**SOL**

- LONG: score **20.7** — location=0.10(swing_high), positioning=0.35(NO_POSITIONING_INFO), flow=0.32(FULL), liquidity=0.27(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **40.8** — location=0.56(swing_low), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.00(FULL), liquidity=0.33(OK), effortresult=1.00(EXPANSION_CANDIDATE), forcedflowproxy=0.00(OK)

**XRP**

- LONG: score **25.0** — location=0.36(swing_high), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.28(OK), effortresult=0.50(INSUFFICIENT_HISTORY), forcedflowproxy=0.00(OK)
- SHORT: score **39.2** — location=0.00(NO_LEVEL_NEAR), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.49(FULL), liquidity=0.32(OK), effortresult=1.00(EXPANSION_CANDIDATE), forcedflowproxy=0.00(OK)

## Forward-outcome experiment (cumulative)

- Pressure setups recorded: **1246** (active: 0, finalized: 1246)

- Valid (FULL) +120s observations: **0** · Partial: **1246** · Unobserved windows (excluded, per §14): **0**
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
