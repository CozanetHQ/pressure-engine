# Pressure Engine — Phase A Diagnostic Report

Generated: **2026-10-03T10:20:01.804362+00:00** · model: **pressure_states_v1** (weights PROVISIONAL EQUAL — not locked, no online learning)

> Shadow-only. No trades. Raw forward-collected telemetry. Numbers without FULL-observation sample sizes are not evidence of edge.

## Runtime coverage (GitHub Actions)

- Runs: **1243** · Observed: **75,483.0s** of expected **134,099.0s** → coverage **56.3%**
- Blind gaps recorded: **500**

## Current state by symbol

| Symbol | State | LONG | SHORT | Coverage | OI 1m | CVD 60s | Imb10 | Liquidity | Effort (L/S) | FFP |
|---|---|---|---|---|---|---|---|---|---|---|
| NEAR | NEUTRAL | **47.3** | **11.9** | PARTIAL_TAPE(272) | 15289775 | 2442.0 | 0.23 | LIQUIDITY_REMOVAL_UNCERTAIN | EXPANSION_/UNKNOWN | 0/0 |
| BTC | NEUTRAL | **23.7** | **53.0** | PARTIAL_TAPE(2070) | 32720 | -49.3 | -0.21 | CONSUMED_WITH_PRINTS | UNKNOWN/UNKNOWN | 0/0 |
| ETH | NEUTRAL | **9.2** | **35.1** | PARTIAL_TAPE(1013) | 778855 | -50.4 | -0.56 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/UNKNOWN | 0/0 |
| SOL | NEUTRAL | **10.6** | **29.4** | PARTIAL_TAPE(380) | 4039045 | -378.4 | -0.36 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/UNKNOWN | 0/0 |
| XRP | NEUTRAL | **20.0** | **36.8** | PARTIAL_TAPE(341) | 170981446 | 1345.0 | 0.07 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/UNKNOWN | 0/0 |

Component status per symbol (latest evaluation):

**NEAR**

- LONG: score **47.3** — location=0.46(swing_high), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.40(FULL), liquidity=0.43(OK), effortresult=1.00(EXPANSION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **11.9** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.17(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)

**BTC**

- LONG: score **23.7** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.57(OK), effortresult=0.50(INSUFFICIENT_HISTORY), forcedflowproxy=0.00(OK)
- SHORT: score **53.0** — location=0.00(NO_LEVEL_NEAR), positioning=0.85(PRICE_WITH_DIR_OI_RISING), flow=1.00(FULL), liquidity=0.83(OK), effortresult=0.50(INSUFFICIENT_HISTORY), forcedflowproxy=0.00(OK)

**ETH**

- LONG: score **9.2** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.00(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **35.1** — location=0.00(NO_LEVEL_NEAR), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.41(FULL), liquidity=0.60(OK), effortresult=0.55(UNKNOWN), forcedflowproxy=0.00(OK)

**SOL**

- LONG: score **10.6** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.08(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **29.4** — location=0.00(NO_LEVEL_NEAR), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.41(FULL), liquidity=0.52(OK), effortresult=0.29(UNKNOWN), forcedflowproxy=0.00(OK)

**XRP**

- LONG: score **20.0** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.31(FULL), liquidity=0.34(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **36.8** — location=0.40(swing_low), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.00(FULL), liquidity=0.26(OK), effortresult=1.00(UNKNOWN), forcedflowproxy=0.00(OK)

## Forward-outcome experiment (cumulative)

- Pressure setups recorded: **79** (active: 0, finalized: 79)

- Valid (FULL) +120s observations: **0** · Partial: **79** · Unobserved windows (excluded, per §14): **0**
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
