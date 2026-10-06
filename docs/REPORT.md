# Pressure Engine — Phase A Diagnostic Report

Generated: **2026-10-06T04:59:36.471007+00:00** · model: **pressure_states_v1** (weights PROVISIONAL EQUAL — not locked, no online learning)

> Shadow-only. No trades. Raw forward-collected telemetry. Numbers without FULL-observation sample sizes are not evidence of edge.

## Runtime coverage (GitHub Actions)

- Runs: **3960** · Observed: **240,041.0s** of expected **374,074.0s** → coverage **64.2%**
- Blind gaps recorded: **500**

## Current state by symbol

| Symbol | State | LONG | SHORT | Coverage | OI 1m | CVD 60s | Imb10 | Liquidity | Effort (L/S) | FFP |
|---|---|---|---|---|---|---|---|---|---|---|
| NEAR | NEUTRAL | **32.0** | **22.6** | PARTIAL_TAPE(975) | 15031712 | 2291.0 | 0.12 | CONSUMED_WITH_PRINTS | ABSORPTION/UNKNOWN | 0/0 |
| BTC | NEUTRAL | **34.7** | **19.2** | PARTIAL_TAPE(4863) | 31229 | 19.6 | -0.83 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/UNKNOWN | 0/0 |
| ETH | NEUTRAL | **38.1** | **12.7** | PARTIAL_TAPE(2108) | 756021 | 18.2 | 0.15 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/UNKNOWN | 0/0 |
| SOL | NEUTRAL | **27.8** | **11.0** | PARTIAL_TAPE(799) | 3922342 | 26.9 | 0.32 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/UNKNOWN | 0/0 |
| XRP | NEUTRAL | **18.8** | **23.7** | PARTIAL_TAPE(623) | 175239987 | -1578.0 | 0.07 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/ABSORPTION | 0/0 |

Component status per symbol (latest evaluation):

**NEAR**

- LONG: score **32.0** — location=0.00(NO_LEVEL_NEAR), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.40(FULL), liquidity=0.77(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **22.6** — location=0.18(swing_low), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.63(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)

**BTC**

- LONG: score **34.7** — location=0.23(swing_high), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=1.00(PARTIAL_TAPE), liquidity=0.00(OK), effortresult=0.30(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **19.2** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(PARTIAL_TAPE), liquidity=0.60(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)

**ETH**

- LONG: score **38.1** — location=0.00(NO_LEVEL_NEAR), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.34(FULL), liquidity=0.39(OK), effortresult=1.00(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **12.7** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.21(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)

**SOL**

- LONG: score **27.8** — location=0.00(NO_LEVEL_NEAR), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.31(FULL), liquidity=0.49(OK), effortresult=0.32(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **11.0** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.11(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)

**XRP**

- LONG: score **18.8** — location=0.00(NO_LEVEL_NEAR), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.00(FULL), liquidity=0.34(OK), effortresult=0.24(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **23.7** — location=0.31(swing_low), positioning=0.35(NO_POSITIONING_INFO), flow=0.30(FULL), liquidity=0.26(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

## Forward-outcome experiment (cumulative)

- Pressure setups recorded: **194** (active: 3, finalized: 191)

- Valid (FULL) +120s observations: **0** · Partial: **191** · Unobserved windows (excluded, per §14): **0**
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
