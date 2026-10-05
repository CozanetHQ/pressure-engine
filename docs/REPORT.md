# Pressure Engine — Phase A Diagnostic Report

Generated: **2026-10-05T11:29:13.728314+00:00** · model: **pressure_states_v1** (weights PROVISIONAL EQUAL — not locked, no online learning)

> Shadow-only. No trades. Raw forward-collected telemetry. Numbers without FULL-observation sample sizes are not evidence of edge.

## Runtime coverage (GitHub Actions)

- Runs: **3475** · Observed: **210,608.0s** of expected **311,051.0s** → coverage **67.7%**
- Blind gaps recorded: **500**

## Current state by symbol

| Symbol | State | LONG | SHORT | Coverage | OI 1m | CVD 60s | Imb10 | Liquidity | Effort (L/S) | FFP |
|---|---|---|---|---|---|---|---|---|---|---|
| NEAR | SHORT_PRESSURE_BUILDING | **31.7** | **42.1** | PARTIAL_TAPE(806) | 15014992 | -15666.0 | -0.79 | LIQUIDITY_REMOVAL_UNCERTAIN | EXPANSION_/ABSORPTION | 0/0 |
| BTC | NEUTRAL | **27.0** | **15.3** | PARTIAL_TAPE(3874) | 31459 | 0.1 | -0.11 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/ABSORPTION | 0/0 |
| ETH | NEUTRAL | **26.7** | **19.2** | PARTIAL_TAPE(1803) | 745801 | 114.6 | -0.81 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/ABSORPTION | 0/0 |
| SOL | NEUTRAL | **32.9** | **39.6** | PARTIAL_TAPE(702) | 3956540 | 32.9 | -0.34 | CONSUMED_WITH_PRINTS | EXPANSION_/ABSORPTION | 0/0 |
| XRP | NEUTRAL | **36.8** | **12.4** | PARTIAL_TAPE(547) | 173766932 | 42221.0 | 0.18 | LIQUIDITY_REMOVAL_UNCERTAIN | EXPANSION_/UNKNOWN | 0/0 |

Component status per symbol (latest evaluation):

**NEAR**

- LONG: score **31.7** — location=0.35(swing_high), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.00(FULL), liquidity=0.00(OK), effortresult=1.00(EXPANSION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **42.1** — location=0.55(swing_low), positioning=0.35(NO_POSITIONING_INFO), flow=0.82(FULL), liquidity=0.60(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

**BTC**

- LONG: score **27.0** — location=0.00(NO_LEVEL_NEAR), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.32(PARTIAL_TAPE), liquidity=0.23(OK), effortresult=0.52(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **15.3** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(PARTIAL_TAPE), liquidity=0.37(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

**ETH**

- LONG: score **26.7** — location=0.00(swing_high), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.49(PARTIAL_TAPE), liquidity=0.00(OK), effortresult=0.57(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **19.2** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(PARTIAL_TAPE), liquidity=0.60(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

**SOL**

- LONG: score **32.9** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.32(FULL), liquidity=0.50(OK), effortresult=0.80(EXPANSION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **39.6** — location=0.52(swing_low), positioning=0.75(COUNTER_POSITIONS_UNWINDING), flow=0.00(FULL), liquidity=0.90(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

**XRP**

- LONG: score **36.8** — location=0.00(NO_LEVEL_NEAR), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.45(FULL), liquidity=0.41(OK), effortresult=0.80(EXPANSION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **12.4** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.19(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)

## Forward-outcome experiment (cumulative)

- Pressure setups recorded: **150** (active: 0, finalized: 150)

- Valid (FULL) +120s observations: **0** · Partial: **150** · Unobserved windows (excluded, per §14): **0**
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
