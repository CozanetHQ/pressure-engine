# Pressure Engine — Phase A Diagnostic Report

Generated: **2026-10-24T09:25:55.849172+00:00** · model: **pressure_states_v1** (weights PROVISIONAL EQUAL — not locked, no online learning)

> Shadow-only. No trades. Raw forward-collected telemetry. Numbers without FULL-observation sample sizes are not evidence of edge.

## Runtime coverage (GitHub Actions)

- Runs: **22127** · Observed: **1,342,942.0s** of expected **1,945,253.0s** → coverage **69.0%**
- Blind gaps recorded: **500**

## Current state by symbol

| Symbol | State | LONG | SHORT | Coverage | OI 1m | CVD 60s | Imb10 | Liquidity | Effort (L/S) | FFP |
|---|---|---|---|---|---|---|---|---|---|---|
| NEAR | NEUTRAL | **19.2** | **33.8** | PARTIAL_TAPE(7780) | 16649981 | -20284.0 | 0.51 | LIQUIDITY_REMOVAL_UNCERTAIN | ABSORPTION/ABSORPTION | 0/0 |
| BTC | NEUTRAL | **9.2** | **41.9** | PARTIAL_TAPE(34464) | 36369 | -2.2 | -0.63 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/EXPANSION_ | 0/0 |
| ETH | NEUTRAL | **11.4** | **37.5** | PARTIAL_TAPE(22582) | 797714 | -482.4 | -0.28 | LIQUIDITY_REMOVAL_UNCERTAIN | ABSORPTION/ABSORPTION | 0/0 |
| SOL | NEUTRAL | **16.6** | **45.1** | PARTIAL_TAPE(7045) | 4160793 | -2651.9 | -0.43 | CONSUMED_WITH_PRINTS | ABSORPTION/ABSORPTION | 0/0 |
| XRP | NEUTRAL | **15.4** | **35.3** | PARTIAL_TAPE(4562) | 176207412 | -12003.0 | 0.13 | LIQUIDITY_REMOVAL_UNCERTAIN | ABSORPTION/EXPANSION_ | 0/0 |

Component status per symbol (latest evaluation):

**NEAR**

- LONG: score **19.2** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(PARTIAL_TAPE), liquidity=0.60(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **33.8** — location=0.00(session_low), positioning=0.85(PRICE_WITH_DIR_OI_RISING), flow=0.97(PARTIAL_TAPE), liquidity=0.00(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

**BTC**

- LONG: score **9.2** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(PARTIAL_TAPE), liquidity=0.00(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **41.9** — location=0.00(session_low), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.37(PARTIAL_TAPE), liquidity=0.60(OK), effortresult=1.00(EXPANSION_CANDIDATE), forcedflowproxy=0.00(OK)

**ETH**

- LONG: score **11.4** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(PARTIAL_TAPE), liquidity=0.13(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **37.5** — location=0.00(NO_LEVEL_NEAR), positioning=0.85(PRICE_WITH_DIR_OI_RISING), flow=0.74(PARTIAL_TAPE), liquidity=0.47(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

**SOL**

- LONG: score **16.6** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(PARTIAL_TAPE), liquidity=0.44(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **45.1** — location=0.00(session_low), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=1.00(PARTIAL_TAPE), liquidity=0.96(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

**XRP**

- LONG: score **15.4** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.38(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **35.3** — location=0.00(session_low), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.37(FULL), liquidity=0.22(OK), effortresult=0.98(EXPANSION_CANDIDATE), forcedflowproxy=0.00(OK)

## Forward-outcome experiment (cumulative)

- Pressure setups recorded: **1006** (active: 0, finalized: 1006)

- Valid (FULL) +120s observations: **0** · Partial: **1006** · Unobserved windows (excluded, per §14): **0**
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
