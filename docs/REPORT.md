# Pressure Engine — Phase A Diagnostic Report

Generated: **2026-10-04T16:48:31.299184+00:00** · model: **pressure_states_v1** (weights PROVISIONAL EQUAL — not locked, no online learning)

> Shadow-only. No trades. Raw forward-collected telemetry. Numbers without FULL-observation sample sizes are not evidence of edge.

## Runtime coverage (GitHub Actions)

- Runs: **2627** · Observed: **159,275.0s** of expected **243,809.0s** → coverage **65.3%**
- Blind gaps recorded: **500**

## Current state by symbol

| Symbol | State | LONG | SHORT | Coverage | OI 1m | CVD 60s | Imb10 | Liquidity | Effort (L/S) | FFP |
|---|---|---|---|---|---|---|---|---|---|---|
| NEAR | LONG_PRESSURE_BUILDING | **37.6** | **40.2** | PARTIAL_TAPE(496) | 15185662 | -50771.0 | 0.40 | CONSUMED_WITH_PRINTS | ABSORPTION/ABSORPTION | 0/0 |
| BTC | NEUTRAL | **26.1** | **11.5** | PARTIAL_TAPE(2501) | 32908 | 0.6 | 0.27 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/UNKNOWN | 0/0 |
| ETH | LONG_PRESSURE_BUILDING | **44.5** | **9.2** | PARTIAL_TAPE(1236) | 757819 | 258.2 | 0.58 | LIQUIDITY_REMOVAL_UNCERTAIN | ABSORPTION/ABSORPTION | 0/0 |
| SOL | NEUTRAL | **50.8** | **18.3** | PARTIAL_TAPE(539) | 3986153 | 21.5 | 0.25 | CONSUMED_WITH_PRINTS | UNKNOWN/UNKNOWN | 0/0 |
| XRP | NEUTRAL | **41.1** | **21.9** | PARTIAL_TAPE(411) | 173419514 | 24115.0 | -0.11 | CONSUMED_WITH_PRINTS | UNKNOWN/UNKNOWN | 0/0 |

Component status per symbol (latest evaluation):

**NEAR**

- LONG: score **37.6** — location=0.77(session_high), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(PARTIAL_TAPE), liquidity=0.94(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **40.2** — location=0.00(NO_LEVEL_NEAR), positioning=0.75(COUNTER_POSITIONS_UNWINDING), flow=1.00(PARTIAL_TAPE), liquidity=0.46(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

**BTC**

- LONG: score **26.1** — location=0.00(NO_LEVEL_NEAR), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.36(FULL), liquidity=0.46(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **11.5** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.14(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)

**ETH**

- LONG: score **44.5** — location=0.71(swing_high), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.61(PARTIAL_TAPE), liquidity=0.60(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **9.2** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(PARTIAL_TAPE), liquidity=0.00(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

**SOL**

- LONG: score **50.8** — location=0.30(swing_high), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.34(FULL), liquidity=0.85(OK), effortresult=1.00(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **18.3** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.55(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)

**XRP**

- LONG: score **41.1** — location=0.54(swing_high), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.51(FULL), liquidity=0.63(OK), effortresult=0.23(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **21.9** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.77(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)

## Forward-outcome experiment (cumulative)

- Pressure setups recorded: **111** (active: 1, finalized: 110)

- Valid (FULL) +120s observations: **0** · Partial: **110** · Unobserved windows (excluded, per §14): **0**
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
