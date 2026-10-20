# Pressure Engine — Phase A Diagnostic Report

Generated: **2026-10-20T12:52:35.543108+00:00** · model: **pressure_states_v1** (weights PROVISIONAL EQUAL — not locked, no online learning)

> Shadow-only. No trades. Raw forward-collected telemetry. Numbers without FULL-observation sample sizes are not evidence of edge.

## Runtime coverage (GitHub Actions)

- Runs: **18262** · Observed: **1,108,555.0s** of expected **1,612,053.0s** → coverage **68.8%**
- Blind gaps recorded: **500**

## Current state by symbol

| Symbol | State | LONG | SHORT | Coverage | OI 1m | CVD 60s | Imb10 | Liquidity | Effort (L/S) | FFP |
|---|---|---|---|---|---|---|---|---|---|---|
| NEAR | LONG_PRESSURE_BUILDING | **40.3** | **13.3** | PARTIAL_TAPE(6728) | 16487050 | 10740.0 | 0.09 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/ABSORPTION | 0/0 |
| BTC | SHORT_PRESSURE_BUILDING | **64.4** | **23.9** | PARTIAL_TAPE(27675) | 35329 | 1.4 | 0.50 | CONSUMED_WITH_PRINTS | EXPANSION_/ABSORPTION | 0/0 |
| ETH | NEUTRAL | **17.3** | **30.8** | PARTIAL_TAPE(16125) | 787724 | -0.3 | -0.98 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/ABSORPTION | 0/0 |
| SOL | NEUTRAL | **30.4** | **11.7** | PARTIAL_TAPE(5917) | 4030960 | 172.7 | 0.32 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/ABSORPTION | 0/0 |
| XRP | NEUTRAL | **30.3** | **28.0** | PARTIAL_TAPE(3796) | 180580794 | 3094.0 | -0.03 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/ABSORPTION | 0/0 |

Component status per symbol (latest evaluation):

**NEAR**

- LONG: score **40.3** — location=0.55(swing_high), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.73(FULL), liquidity=0.35(OK), effortresult=0.24(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **13.3** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.25(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

**BTC**

- LONG: score **64.4** — location=0.97(swing_high), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.34(PARTIAL_TAPE), liquidity=1.00(OK), effortresult=1.00(EXPANSION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **23.9** — location=0.48(swing_low), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(PARTIAL_TAPE), liquidity=0.40(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

**ETH**

- LONG: score **17.3** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(PARTIAL_TAPE), liquidity=0.00(OK), effortresult=0.69(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **30.8** — location=0.00(NO_LEVEL_NEAR), positioning=0.75(COUNTER_POSITIONS_UNWINDING), flow=0.30(PARTIAL_TAPE), liquidity=0.60(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

**SOL**

- LONG: score **30.4** — location=0.00(NO_LEVEL_NEAR), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.36(FULL), liquidity=0.49(OK), effortresult=0.42(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **11.7** — location=0.04(swing_low), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.11(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

**XRP**

- LONG: score **30.3** — location=0.00(swing_high), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.32(FULL), liquidity=0.28(OK), effortresult=0.67(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **28.0** — location=0.81(swing_low), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.32(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

## Forward-outcome experiment (cumulative)

- Pressure setups recorded: **869** (active: 0, finalized: 869)

- Valid (FULL) +120s observations: **0** · Partial: **869** · Unobserved windows (excluded, per §14): **0**
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
