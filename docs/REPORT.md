# Pressure Engine — Phase A Diagnostic Report

Generated: **2026-10-28T18:40:47.401740+00:00** · model: **pressure_states_v1** (weights PROVISIONAL EQUAL — not locked, no online learning)

> Shadow-only. No trades. Raw forward-collected telemetry. Numbers without FULL-observation sample sizes are not evidence of edge.

## Runtime coverage (GitHub Actions)

- Runs: **26380** · Observed: **1,600,909.0s** of expected **2,324,145.0s** → coverage **68.9%**
- Blind gaps recorded: **500**

## Current state by symbol

| Symbol | State | LONG | SHORT | Coverage | OI 1m | CVD 60s | Imb10 | Liquidity | Effort (L/S) | FFP |
|---|---|---|---|---|---|---|---|---|---|---|
| NEAR | NEUTRAL | **41.5** | **21.4** | PARTIAL_TAPE(8546) | 16475477 | 361.0 | -0.03 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/ABSORPTION | 0/0 |
| BTC | NEUTRAL | **47.2** | **30.4** | PARTIAL_TAPE | 36914 | 6.9 | -0.56 | LIQUIDITY_REMOVAL_UNCERTAIN | EXPANSION_/ABSORPTION | 0/0 |
| ETH | NEUTRAL | **50.3** | **37.6** | PARTIAL_TAPE(28827) | 769677 | 147.4 | -0.36 | CONSUMED_WITH_PRINTS | EXPANSION_/ABSORPTION | 0/0 |
| SOL | NEUTRAL | **48.5** | **24.1** | PARTIAL_TAPE(8029) | 4234700 | 964.9 | 0.72 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/ABSORPTION | 0/0 |
| XRP | LONG_PRESSURE_BUILDING | **50.0** | **30.8** | PARTIAL_TAPE(5090) | 184563766 | 30412.0 | -0.33 | LIQUIDITY_REMOVAL_UNCERTAIN | EXPANSION_/ABSORPTION | 0/0 |

Component status per symbol (latest evaluation):

**NEAR**

- LONG: score **41.5** — location=0.47(swing_high), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.59(PARTIAL_TAPE), liquidity=0.28(OK), effortresult=0.59(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **21.4** — location=0.42(swing_low), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(PARTIAL_TAPE), liquidity=0.32(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

**BTC**

- LONG: score **47.2** — location=0.99(swing_high), positioning=0.35(NO_POSITIONING_INFO), flow=0.49(PARTIAL_TAPE), liquidity=0.00(OK), effortresult=1.00(EXPANSION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **30.4** — location=0.27(swing_low), positioning=0.75(COUNTER_POSITIONS_UNWINDING), flow=0.00(PARTIAL_TAPE), liquidity=0.60(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

**ETH**

- LONG: score **50.3** — location=0.89(swing_high), positioning=0.35(NO_POSITIONING_INFO), flow=0.48(PARTIAL_TAPE), liquidity=0.49(OK), effortresult=0.81(EXPANSION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **37.6** — location=0.39(swing_low), positioning=0.75(COUNTER_POSITIONS_UNWINDING), flow=0.00(PARTIAL_TAPE), liquidity=0.91(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

**SOL**

- LONG: score **48.5** — location=0.66(swing_high), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.56(PARTIAL_TAPE), liquidity=0.60(OK), effortresult=0.54(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **24.1** — location=0.90(swing_low), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(PARTIAL_TAPE), liquidity=0.00(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

**XRP**

- LONG: score **50.0** — location=0.93(swing_high), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.41(PARTIAL_TAPE), liquidity=0.10(OK), effortresult=1.00(EXPANSION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **30.8** — location=0.80(swing_low), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(PARTIAL_TAPE), liquidity=0.50(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

## Forward-outcome experiment (cumulative)

- Pressure setups recorded: **1153** (active: 4, finalized: 1149)

- Valid (FULL) +120s observations: **0** · Partial: **1149** · Unobserved windows (excluded, per §14): **0**
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
