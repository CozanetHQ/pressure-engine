# Pressure Engine — Phase A Diagnostic Report

Generated: **2026-10-08T08:28:47.171421+00:00** · model: **pressure_states_v1** (weights PROVISIONAL EQUAL — not locked, no online learning)

> Shadow-only. No trades. Raw forward-collected telemetry. Numbers without FULL-observation sample sizes are not evidence of edge.

## Runtime coverage (GitHub Actions)

- Runs: **5893** · Observed: **357,412.0s** of expected **559,425.0s** → coverage **63.9%**
- Blind gaps recorded: **500**

## Current state by symbol

| Symbol | State | LONG | SHORT | Coverage | OI 1m | CVD 60s | Imb10 | Liquidity | Effort (L/S) | FFP |
|---|---|---|---|---|---|---|---|---|---|---|
| NEAR | NEUTRAL | **21.3** | **33.8** | PARTIAL_TAPE(1870) | 15419823 | -142.0 | 0.21 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/UNKNOWN | 0/0 |
| BTC | NEUTRAL | **20.4** | **30.7** | PARTIAL_TAPE(8547) | 36289 | 3.0 | 0.01 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/UNKNOWN | 0/0 |
| ETH | NEUTRAL | **19.9** | **48.9** | PARTIAL_TAPE(3908) | 844930 | -14.0 | -0.60 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/UNKNOWN | 0/0 |
| SOL | NEUTRAL | **21.3** | **17.7** | PARTIAL_TAPE(1370) | 4269643 | 144.7 | -0.14 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/UNKNOWN | 0/0 |
| XRP | NEUTRAL | **33.1** | **40.8** | PARTIAL_TAPE(1132) | 182785180 | 118528.0 | 0.00 | CONSUMED_WITH_PRINTS | ABSORPTION/UNKNOWN | 0/0 |

Component status per symbol (latest evaluation):

**NEAR**

- LONG: score **21.3** — location=0.30(swing_high), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.43(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **33.8** — location=0.00(swing_low), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.31(FULL), liquidity=0.17(OK), effortresult=1.00(UNKNOWN), forcedflowproxy=0.00(OK)

**BTC**

- LONG: score **20.4** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.37(PARTIAL_TAPE), liquidity=0.31(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **30.7** — location=0.00(NO_LEVEL_NEAR), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.00(PARTIAL_TAPE), liquidity=0.29(OK), effortresult=1.00(UNKNOWN), forcedflowproxy=0.00(OK)

**ETH**

- LONG: score **19.9** — location=0.64(swing_high), positioning=0.35(NO_POSITIONING_INFO), flow=0.01(FULL), liquidity=0.00(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **48.9** — location=0.48(swing_low), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.30(FULL), liquidity=0.60(OK), effortresult=1.00(UNKNOWN), forcedflowproxy=0.00(OK)

**SOL**

- LONG: score **21.3** — location=0.00(NO_LEVEL_NEAR), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.31(FULL), liquidity=0.22(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **17.7** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.38(OK), effortresult=0.33(UNKNOWN), forcedflowproxy=0.00(OK)

**XRP**

- LONG: score **33.1** — location=0.07(swing_high), positioning=0.35(NO_POSITIONING_INFO), flow=0.67(FULL), liquidity=0.70(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **40.8** — location=0.00(NO_LEVEL_NEAR), positioning=0.75(COUNTER_POSITIONS_UNWINDING), flow=0.00(FULL), liquidity=0.70(OK), effortresult=1.00(UNKNOWN), forcedflowproxy=0.00(OK)

## Forward-outcome experiment (cumulative)

- Pressure setups recorded: **341** (active: 0, finalized: 341)

- Valid (FULL) +120s observations: **0** · Partial: **341** · Unobserved windows (excluded, per §14): **0**
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
