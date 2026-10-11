# Pressure Engine — Phase A Diagnostic Report

Generated: **2026-10-11T01:55:49.141658+00:00** · model: **pressure_states_v1** (weights PROVISIONAL EQUAL — not locked, no online learning)

> Shadow-only. No trades. Raw forward-collected telemetry. Numbers without FULL-observation sample sizes are not evidence of edge.

## Runtime coverage (GitHub Actions)

- Runs: **8815** · Observed: **534,825.0s** of expected **795,047.0s** → coverage **67.3%**
- Blind gaps recorded: **500**

## Current state by symbol

| Symbol | State | LONG | SHORT | Coverage | OI 1m | CVD 60s | Imb10 | Liquidity | Effort (L/S) | FFP |
|---|---|---|---|---|---|---|---|---|---|---|
| NEAR | NEUTRAL | **24.5** | **29.1** | PARTIAL_TAPE(3238) | 16539686 | 1620.0 | 0.11 | LIQUIDITY_REMOVAL_UNCERTAIN | ABSORPTION/ABSORPTION | 0/0 |
| BTC | NEUTRAL | **14.4** | **44.5** | PARTIAL_TAPE(12711) | 34130 | -0.9 | 0.02 | LIQUIDITY_REMOVAL_UNCERTAIN | ABSORPTION/EXPANSION_ | 0/0 |
| ETH | NEUTRAL | **31.0** | **41.1** | PARTIAL_TAPE(6333) | 776640 | -218.3 | -0.36 | CONSUMED_WITH_PRINTS | UNKNOWN/ABSORPTION | 0/0 |
| SOL | NEUTRAL | **40.1** | **37.0** | PARTIAL_TAPE(2410) | 4230224 | 565.7 | -0.28 | CONSUMED_WITH_PRINTS | ABSORPTION/UNKNOWN | 0/0 |
| XRP | NEUTRAL | **31.1** | **37.3** | PARTIAL_TAPE(1739) | 195044372 | 17861.0 | 0.02 | CONSUMED_WITH_PRINTS | ABSORPTION/EXPANSION_ | 0/0 |

Component status per symbol (latest evaluation):

**NEAR**

- LONG: score **24.5** — location=0.00(NO_LEVEL_NEAR), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.35(PARTIAL_TAPE), liquidity=0.36(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **29.1** — location=0.96(swing_low), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(PARTIAL_TAPE), liquidity=0.24(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

**BTC**

- LONG: score **14.4** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.31(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **44.5** — location=0.50(swing_low), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.34(FULL), liquidity=0.29(OK), effortresult=1.00(EXPANSION_CANDIDATE), forcedflowproxy=0.00(OK)

**ETH**

- LONG: score **31.0** — location=0.83(swing_high), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.48(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **41.1** — location=0.00(NO_LEVEL_NEAR), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.80(FULL), liquidity=0.92(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

**SOL**

- LONG: score **40.1** — location=0.78(swing_high), positioning=0.35(NO_POSITIONING_INFO), flow=0.55(FULL), liquidity=0.53(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **37.0** — location=0.52(swing_low), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.00(FULL), liquidity=0.87(OK), effortresult=0.29(UNKNOWN), forcedflowproxy=0.00(OK)

**XRP**

- LONG: score **31.1** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.60(FULL), liquidity=0.71(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **37.3** — location=0.00(swing_low), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.00(FULL), liquidity=0.69(OK), effortresult=1.00(EXPANSION_CANDIDATE), forcedflowproxy=0.00(OK)

## Forward-outcome experiment (cumulative)

- Pressure setups recorded: **443** (active: 0, finalized: 443)

- Valid (FULL) +120s observations: **0** · Partial: **443** · Unobserved windows (excluded, per §14): **0**
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
