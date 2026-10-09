# Pressure Engine — Phase A Diagnostic Report

Generated: **2026-10-09T11:09:14.193607+00:00** · model: **pressure_states_v1** (weights PROVISIONAL EQUAL — not locked, no online learning)

> Shadow-only. No trades. Raw forward-collected telemetry. Numbers without FULL-observation sample sizes are not evidence of edge.

## Runtime coverage (GitHub Actions)

- Runs: **7070** · Observed: **428,949.0s** of expected **655,452.0s** → coverage **65.4%**
- Blind gaps recorded: **500**

## Current state by symbol

| Symbol | State | LONG | SHORT | Coverage | OI 1m | CVD 60s | Imb10 | Liquidity | Effort (L/S) | FFP |
|---|---|---|---|---|---|---|---|---|---|---|
| NEAR | NEUTRAL | **36.6** | **12.4** | PARTIAL_TAPE(2704) | 16067297 | 8665.0 | 0.17 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/UNKNOWN | 0/0 |
| BTC | NEUTRAL | **21.5** | **30.8** | PARTIAL_TAPE(11465) | 34818 | 3.9 | -0.60 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/UNKNOWN | 0/0 |
| ETH | NEUTRAL | **33.7** | **30.6** | PARTIAL_TAPE(5721) | 784089 | -53.3 | -0.05 | CONSUMED_WITH_PRINTS | EXPANSION_/ABSORPTION | 0/0 |
| SOL | NEUTRAL | **38.0** | **12.1** | PARTIAL_TAPE(2084) | 4251194 | 50.4 | 0.21 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/UNKNOWN | 0/0 |
| XRP | NEUTRAL | **51.3** | **26.6** | PARTIAL_TAPE(1581) | 201120222 | 3273.0 | -0.06 | LIQUIDITY_REMOVAL_UNCERTAIN | EXPANSION_/ABSORPTION | 0/0 |

Component status per symbol (latest evaluation):

**NEAR**

- LONG: score **36.6** — location=0.00(NO_LEVEL_NEAR), positioning=0.85(PRICE_WITH_DIR_OI_RISING), flow=0.59(FULL), liquidity=0.40(OK), effortresult=0.35(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **12.4** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.20(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)

**BTC**

- LONG: score **21.5** — location=0.00(NO_LEVEL_NEAR), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.49(FULL), liquidity=0.00(OK), effortresult=0.24(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **30.8** — location=0.69(swing_low), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.60(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)

**ETH**

- LONG: score **33.7** — location=0.00(swing_high), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(PARTIAL_TAPE), liquidity=0.67(OK), effortresult=1.00(EXPANSION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **30.6** — location=0.00(NO_LEVEL_NEAR), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.36(PARTIAL_TAPE), liquidity=0.73(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

**SOL**

- LONG: score **38.0** — location=0.00(NO_LEVEL_NEAR), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.31(FULL), liquidity=0.42(OK), effortresult=1.00(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **12.1** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.18(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)

**XRP**

- LONG: score **51.3** — location=0.94(swing_high), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.32(FULL), liquidity=0.26(OK), effortresult=1.00(EXPANSION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **26.6** — location=0.71(swing_low), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.34(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

## Forward-outcome experiment (cumulative)

- Pressure setups recorded: **389** (active: 2, finalized: 387)

- Valid (FULL) +120s observations: **0** · Partial: **387** · Unobserved windows (excluded, per §14): **0**
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
