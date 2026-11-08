# Pressure Engine — Phase A Diagnostic Report

Generated: **2026-11-08T02:48:55.702259+00:00** · model: **pressure_states_v1** (weights PROVISIONAL EQUAL — not locked, no online learning)

> Shadow-only. No trades. Raw forward-collected telemetry. Numbers without FULL-observation sample sizes are not evidence of edge.

## Runtime coverage (GitHub Actions)

- Runs: **35387** · Observed: **2,147,317.0s** of expected **3,217,433.0s** → coverage **66.7%**
- Blind gaps recorded: **500**

## Current state by symbol

| Symbol | State | LONG | SHORT | Coverage | OI 1m | CVD 60s | Imb10 | Liquidity | Effort (L/S) | FFP |
|---|---|---|---|---|---|---|---|---|---|---|
| NEAR | NEUTRAL | **30.7** | **14.6** | PARTIAL_TAPE(10370) | 16796091 | 4722.0 | -0.01 | LIQUIDITY_REMOVAL_UNCERTAIN | ABSORPTION/UNKNOWN | 0/0 |
| BTC | NEUTRAL | **26.1** | **10.7** | PARTIAL_TAPE(57043) | 37895 | 0.1 | 0.36 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/UNKNOWN | 0/0 |
| ETH | NEUTRAL | **43.2** | **17.2** | PARTIAL_TAPE(39614) | 799687 | 142.5 | 0.36 | CONSUMED_WITH_PRINTS | UNKNOWN/UNKNOWN | 0/0 |
| SOL | NEUTRAL | **34.8** | **16.4** | PARTIAL_TAPE(10978) | 4272283 | 67.6 | -0.14 | LIQUIDITY_REMOVAL_UNCERTAIN | EXPANSION_/UNKNOWN | 0/0 |
| XRP | NEUTRAL | **23.3** | **13.6** | PARTIAL_TAPE(6790) | 193104851 | 3135.0 | 0.06 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/UNKNOWN | 0/0 |

Component status per symbol (latest evaluation):

**NEAR**

- LONG: score **30.7** — location=0.33(swing_high), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.47(FULL), liquidity=0.29(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **14.6** — location=0.02(session_low), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.31(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)

**BTC**

- LONG: score **26.1** — location=0.00(NO_LEVEL_NEAR), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.30(FULL), liquidity=0.52(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **10.7** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.01(FULL), liquidity=0.08(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)

**ETH**

- LONG: score **43.2** — location=0.00(NO_LEVEL_NEAR), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.72(FULL), liquidity=0.92(OK), effortresult=0.40(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **17.2** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.48(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)

**SOL**

- LONG: score **34.8** — location=0.00(NO_LEVEL_NEAR), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.32(FULL), liquidity=0.22(OK), effortresult=1.00(EXPANSION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **16.4** — location=0.05(session_low), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.38(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)

**XRP**

- LONG: score **23.3** — location=0.00(NO_LEVEL_NEAR), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.31(FULL), liquidity=0.34(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **13.6** — location=0.00(session_low), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.26(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)

## Forward-outcome experiment (cumulative)

- Pressure setups recorded: **1492** (active: 2, finalized: 1490)

- Valid (FULL) +120s observations: **0** · Partial: **1490** · Unobserved windows (excluded, per §14): **0**
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
