# Pressure Engine — Phase A Diagnostic Report

Generated: **2026-10-23T19:24:35.228918+00:00** · model: **pressure_states_v1** (weights PROVISIONAL EQUAL — not locked, no online learning)

> Shadow-only. No trades. Raw forward-collected telemetry. Numbers without FULL-observation sample sizes are not evidence of edge.

## Runtime coverage (GitHub Actions)

- Runs: **21531** · Observed: **1,306,822.0s** of expected **1,894,773.0s** → coverage **69.0%**
- Blind gaps recorded: **500**

## Current state by symbol

| Symbol | State | LONG | SHORT | Coverage | OI 1m | CVD 60s | Imb10 | Liquidity | Effort (L/S) | FFP |
|---|---|---|---|---|---|---|---|---|---|---|
| NEAR | NEUTRAL | **33.1** | **32.2** | PARTIAL_TAPE(7679) | 16544394 | -1393.0 | -0.22 | CONSUMED_WITH_PRINTS | EXPANSION_/ABSORPTION | 0/0 |
| BTC | NEUTRAL | **35.1** | **32.9** | PARTIAL_TAPE(33825) | 36160 | 5.7 | -0.41 | LIQUIDITY_REMOVAL_UNCERTAIN | EXPANSION_/ABSORPTION | 0/0 |
| ETH | NEUTRAL | **38.0** | **20.2** | PARTIAL_TAPE(21929) | 759678 | 255.8 | 0.33 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/UNKNOWN | 0/0 |
| SOL | NEUTRAL | **33.4** | **21.7** | PARTIAL_TAPE(6945) | 4113877 | 525.7 | 0.16 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/ABSORPTION | 0/0 |
| XRP | SHORT_PRESSURE_BUILDING | **27.1** | **35.9** | PARTIAL_TAPE(4515) | 175290430 | -39.0 | -0.26 | LIQUIDITY_REMOVAL_UNCERTAIN | EXPANSION_/ABSORPTION | 0/0 |

Component status per symbol (latest evaluation):

**NEAR**

- LONG: score **33.1** — location=0.00(NO_LEVEL_NEAR), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.00(FULL), liquidity=0.57(OK), effortresult=0.87(EXPANSION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **32.2** — location=0.20(session_low), positioning=0.35(NO_POSITIONING_INFO), flow=0.35(FULL), liquidity=0.83(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

**BTC**

- LONG: score **35.1** — location=0.00(NO_LEVEL_NEAR), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.50(PARTIAL_TAPE), liquidity=0.05(OK), effortresult=1.00(EXPANSION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **32.9** — location=0.88(session_low), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(PARTIAL_TAPE), liquidity=0.55(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

**ETH**

- LONG: score **38.0** — location=0.00(NO_LEVEL_NEAR), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.74(PARTIAL_TAPE), liquidity=0.50(OK), effortresult=0.48(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **20.2** — location=0.56(swing_low), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(PARTIAL_TAPE), liquidity=0.10(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)

**SOL**

- LONG: score **33.4** — location=0.00(NO_LEVEL_NEAR), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.44(FULL), liquidity=0.40(OK), effortresult=0.62(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **21.7** — location=0.55(session_low), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.20(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

**XRP**

- LONG: score **27.1** — location=0.00(NO_LEVEL_NEAR), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.02(FULL), liquidity=0.14(OK), effortresult=0.92(EXPANSION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **35.9** — location=0.85(session_low), positioning=0.35(NO_POSITIONING_INFO), flow=0.30(FULL), liquidity=0.46(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

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
