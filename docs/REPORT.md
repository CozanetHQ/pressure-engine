# Pressure Engine — Phase A Diagnostic Report

Generated: **2026-11-04T04:09:27.692508+00:00** · model: **pressure_states_v1** (weights PROVISIONAL EQUAL — not locked, no online learning)

> Shadow-only. No trades. Raw forward-collected telemetry. Numbers without FULL-observation sample sizes are not evidence of edge.

## Runtime coverage (GitHub Actions)

- Runs: **32291** · Observed: **1,959,557.0s** of expected **2,876,665.0s** → coverage **68.1%**
- Blind gaps recorded: **500**

## Current state by symbol

| Symbol | State | LONG | SHORT | Coverage | OI 1m | CVD 60s | Imb10 | Liquidity | Effort (L/S) | FFP |
|---|---|---|---|---|---|---|---|---|---|---|
| NEAR | NEUTRAL | **39.9** | **29.1** | PARTIAL_TAPE(9917) | 16644441 | 6278.0 | -0.41 | LIQUIDITY_REMOVAL_UNCERTAIN | EXPANSION_/ABSORPTION | 0/0 |
| BTC | NEUTRAL | **32.0** | **38.1** | PARTIAL_TAPE | 36884 | 14.8 | -0.54 | CONSUMED_WITH_PRINTS | UNKNOWN/ABSORPTION | 0/0 |
| ETH | LONG_PRESSURE_CONFIRMED | **52.8** | **10.9** | PARTIAL_TAPE | 767718 | 638.0 | 0.33 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/ABSORPTION | 0/0 |
| SOL | NEUTRAL | **27.9** | **26.8** | PARTIAL_TAPE(10090) | 4298587 | -3715.4 | 0.40 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/ABSORPTION | 0/0 |
| XRP | NEUTRAL | **32.8** | **18.9** | PARTIAL_TAPE(6188) | 188535301 | 351942.0 | 0.19 | LIQUIDITY_REMOVAL_UNCERTAIN | ABSORPTION/ABSORPTION | 0/0 |

Component status per symbol (latest evaluation):

**NEAR**

- LONG: score **39.9** — location=0.00(swing_high), positioning=0.85(PRICE_WITH_DIR_OI_RISING), flow=0.49(FULL), liquidity=0.05(OK), effortresult=1.00(EXPANSION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **29.1** — location=0.65(swing_low), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.55(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

**BTC**

- LONG: score **32.0** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.70(PARTIAL_TAPE), liquidity=0.40(OK), effortresult=0.47(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **38.1** — location=0.34(swing_low), positioning=0.75(COUNTER_POSITIONS_UNWINDING), flow=0.00(PARTIAL_TAPE), liquidity=1.00(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

**ETH**

- LONG: score **52.8** — location=0.60(swing_high), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=1.00(PARTIAL_TAPE), liquidity=0.50(OK), effortresult=0.52(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **10.9** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(PARTIAL_TAPE), liquidity=0.10(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

**SOL**

- LONG: score **27.9** — location=0.00(NO_LEVEL_NEAR), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.00(FULL), liquidity=0.54(OK), effortresult=0.58(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **26.8** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=1.00(FULL), liquidity=0.06(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

**XRP**

- LONG: score **32.8** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=1.00(PARTIAL_TAPE), liquidity=0.42(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **18.9** — location=0.00(NO_LEVEL_NEAR), positioning=0.75(COUNTER_POSITIONS_UNWINDING), flow=0.00(PARTIAL_TAPE), liquidity=0.18(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

## Forward-outcome experiment (cumulative)

- Pressure setups recorded: **1375** (active: 1, finalized: 1374)

- Valid (FULL) +120s observations: **0** · Partial: **1374** · Unobserved windows (excluded, per §14): **0**
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
