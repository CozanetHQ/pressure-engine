# Pressure Engine — Phase A Diagnostic Report

Generated: **2026-10-06T00:09:12.832130+00:00** · model: **pressure_states_v1** (weights PROVISIONAL EQUAL — not locked, no online learning)

> Shadow-only. No trades. Raw forward-collected telemetry. Numbers without FULL-observation sample sizes are not evidence of edge.

## Runtime coverage (GitHub Actions)

- Runs: **3741** · Observed: **226,762.0s** of expected **356,650.0s** → coverage **63.6%**
- Blind gaps recorded: **500**

## Current state by symbol

| Symbol | State | LONG | SHORT | Coverage | OI 1m | CVD 60s | Imb10 | Liquidity | Effort (L/S) | FFP |
|---|---|---|---|---|---|---|---|---|---|---|
| NEAR | NEUTRAL | **46.6** | **12.6** | PARTIAL_TAPE(897) | 15123330 | 3404.0 | 0.52 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/UNKNOWN | 0/0 |
| BTC | NEUTRAL | **34.2** | **19.4** | PARTIAL_TAPE(4643) | 31049 | 1.9 | 0.56 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/UNKNOWN | 0/0 |
| ETH | LONG_PRESSURE_BUILDING | **54.4** | **23.5** | PARTIAL_TAPE(2058) | 745718 | 92.9 | 0.04 | CONSUMED_WITH_PRINTS | UNKNOWN/UNKNOWN | 0/0 |
| SOL | NEUTRAL | **27.5** | **19.7** | PARTIAL_TAPE(780) | 3901796 | -4.5 | -0.05 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/UNKNOWN | 0/0 |
| XRP | SHORT_PRESSURE_BUILDING | **42.6** | **11.6** | PARTIAL_TAPE(609) | 173653036 | 3430.0 | 0.25 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/UNKNOWN | 0/0 |

Component status per symbol (latest evaluation):

**NEAR**

- LONG: score **46.6** — location=0.00(swing_high), positioning=0.85(PRICE_WITH_DIR_OI_RISING), flow=0.53(PARTIAL_TAPE), liquidity=0.60(OK), effortresult=0.81(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **12.6** — location=0.21(session_low), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(PARTIAL_TAPE), liquidity=0.00(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)

**BTC**

- LONG: score **34.2** — location=0.00(NO_LEVEL_NEAR), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.46(FULL), liquidity=0.60(OK), effortresult=0.44(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **19.4** — location=0.61(swing_low), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.00(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)

**ETH**

- LONG: score **54.4** — location=0.99(session_high), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.72(FULL), liquidity=0.72(OK), effortresult=0.28(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **23.5** — location=0.18(swing_low), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.68(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)

**SOL**

- LONG: score **27.5** — location=0.27(swing_high), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.00(FULL), liquidity=0.27(OK), effortresult=0.56(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **19.7** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.30(FULL), liquidity=0.33(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)

**XRP**

- LONG: score **42.6** — location=0.18(session_high), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.37(FULL), liquidity=0.45(OK), effortresult=1.00(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **11.6** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.15(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)

## Forward-outcome experiment (cumulative)

- Pressure setups recorded: **165** (active: 0, finalized: 165)

- Valid (FULL) +120s observations: **0** · Partial: **165** · Unobserved windows (excluded, per §14): **0**
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
