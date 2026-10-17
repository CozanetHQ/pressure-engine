# Pressure Engine — Phase A Diagnostic Report

Generated: **2026-10-17T22:05:57.474611+00:00** · model: **pressure_states_v1** (weights PROVISIONAL EQUAL — not locked, no online learning)

> Shadow-only. No trades. Raw forward-collected telemetry. Numbers without FULL-observation sample sizes are not evidence of edge.

## Runtime coverage (GitHub Actions)

- Runs: **15766** · Observed: **957,216.0s** of expected **1,386,055.0s** → coverage **69.1%**
- Blind gaps recorded: **500**

## Current state by symbol

| Symbol | State | LONG | SHORT | Coverage | OI 1m | CVD 60s | Imb10 | Liquidity | Effort (L/S) | FFP |
|---|---|---|---|---|---|---|---|---|---|---|
| NEAR | NEUTRAL | **31.1** | **21.2** | PARTIAL_TAPE(6197) | 16055354 | 3701.0 | 0.30 | CONSUMED_WITH_PRINTS | ABSORPTION/ABSORPTION | 0/0 |
| BTC | SHORT_PRESSURE_BUILDING | **17.0** | **38.6** | PARTIAL_TAPE(24604) | 34585 | -6.9 | 0.28 | LIQUIDITY_REMOVAL_UNCERTAIN | ABSORPTION/ABSORPTION | 0/0 |
| ETH | NEUTRAL | **26.9** | **19.5** | PARTIAL_TAPE(13495) | 770530 | -27.4 | 0.37 | LIQUIDITY_REMOVAL_UNCERTAIN | EXPANSION_/ABSORPTION | 0/0 |
| SOL | NEUTRAL | **31.5** | **26.0** | PARTIAL_TAPE(5174) | 4127610 | 162.1 | -0.15 | LIQUIDITY_REMOVAL_UNCERTAIN | EXPANSION_/ABSORPTION | 0/0 |
| XRP | NEUTRAL | **23.3** | **22.1** | PARTIAL_TAPE(3408) | 179531672 | 48962.0 | 0.24 | LIQUIDITY_REMOVAL_UNCERTAIN | ABSORPTION/ABSORPTION | 0/0 |

Component status per symbol (latest evaluation):

**NEAR**

- LONG: score **31.1** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.44(PARTIAL_TAPE), liquidity=0.88(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **21.2** — location=0.00(swing_low), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.00(PARTIAL_TAPE), liquidity=0.52(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

**BTC**

- LONG: score **17.0** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(PARTIAL_TAPE), liquidity=0.47(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **38.6** — location=0.84(swing_low), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.60(PARTIAL_TAPE), liquidity=0.13(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

**ETH**

- LONG: score **26.9** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(PARTIAL_TAPE), liquidity=0.52(OK), effortresult=0.74(EXPANSION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **19.5** — location=0.00(NO_LEVEL_NEAR), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.34(PARTIAL_TAPE), liquidity=0.08(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

**SOL**

- LONG: score **31.5** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.33(FULL), liquidity=0.21(OK), effortresult=1.00(EXPANSION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **26.0** — location=0.42(swing_low), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.00(FULL), liquidity=0.39(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

**XRP**

- LONG: score **23.3** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.40(FULL), liquidity=0.45(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **22.1** — location=0.42(swing_low), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.00(FULL), liquidity=0.15(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

## Forward-outcome experiment (cumulative)

- Pressure setups recorded: **772** (active: 2, finalized: 770)

- Valid (FULL) +120s observations: **0** · Partial: **770** · Unobserved windows (excluded, per §14): **0**
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
