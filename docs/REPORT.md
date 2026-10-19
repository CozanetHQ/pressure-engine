# Pressure Engine — Phase A Diagnostic Report

Generated: **2026-10-19T14:45:23.236120+00:00** · model: **pressure_states_v1** (weights PROVISIONAL EQUAL — not locked, no online learning)

> Shadow-only. No trades. Raw forward-collected telemetry. Numbers without FULL-observation sample sizes are not evidence of edge.

## Runtime coverage (GitHub Actions)

- Runs: **17332** · Observed: **1,052,158.0s** of expected **1,532,421.0s** → coverage **68.7%**
- Blind gaps recorded: **500**

## Current state by symbol

| Symbol | State | LONG | SHORT | Coverage | OI 1m | CVD 60s | Imb10 | Liquidity | Effort (L/S) | FFP |
|---|---|---|---|---|---|---|---|---|---|---|
| NEAR | NEUTRAL | **43.7** | **21.8** | PARTIAL_TAPE(6552) | 16097097 | 2718.0 | -0.09 | CONSUMED_WITH_PRINTS | UNKNOWN/UNKNOWN | 0/0 |
| BTC | SHORT_PRESSURE_BUILDING | **25.6** | **49.4** | PARTIAL_TAPE(26569) | 33974 | -24.1 | -0.35 | LIQUIDITY_REMOVAL_UNCERTAIN | EXPANSION_/ABSORPTION | 0/0 |
| ETH | LONG_PRESSURE_BUILDING | **47.3** | **15.9** | PARTIAL_TAPE | 765731 | 323.0 | -0.17 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/UNKNOWN | 0/0 |
| SOL | NEUTRAL | **25.1** | **23.9** | PARTIAL_TAPE(5722) | 4034979 | -1167.4 | -0.11 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/ABSORPTION | 0/0 |
| XRP | NEUTRAL | **35.1** | **23.3** | PARTIAL_TAPE(3677) | 185896577 | 15384.0 | -0.13 | LIQUIDITY_REMOVAL_UNCERTAIN | EXPANSION_/ABSORPTION | 0/0 |

Component status per symbol (latest evaluation):

**NEAR**

- LONG: score **43.7** — location=0.00(NO_LEVEL_NEAR), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.43(FULL), liquidity=0.64(OK), effortresult=1.00(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **21.8** — location=0.00(session_low), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.76(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)

**BTC**

- LONG: score **25.6** — location=0.00(NO_LEVEL_NEAR), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.00(PARTIAL_TAPE), liquidity=0.09(OK), effortresult=0.90(EXPANSION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **49.4** — location=0.92(swing_low), positioning=0.35(NO_POSITIONING_INFO), flow=0.99(PARTIAL_TAPE), liquidity=0.51(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

**ETH**

- LONG: score **47.3** — location=0.69(swing_high), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.68(PARTIAL_TAPE), liquidity=0.20(OK), effortresult=0.71(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **15.9** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(PARTIAL_TAPE), liquidity=0.40(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)

**SOL**

- LONG: score **25.1** — location=0.00(NO_LEVEL_NEAR), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.00(PARTIAL_TAPE), liquidity=0.24(OK), effortresult=0.72(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **23.9** — location=0.01(swing_low), positioning=0.35(NO_POSITIONING_INFO), flow=0.51(PARTIAL_TAPE), liquidity=0.36(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

**XRP**

- LONG: score **35.1** — location=0.10(swing_high), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.33(FULL), liquidity=0.22(OK), effortresult=0.91(EXPANSION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **23.3** — location=0.47(swing_low), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.38(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

## Forward-outcome experiment (cumulative)

- Pressure setups recorded: **849** (active: 2, finalized: 847)

- Valid (FULL) +120s observations: **0** · Partial: **847** · Unobserved windows (excluded, per §14): **0**
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
