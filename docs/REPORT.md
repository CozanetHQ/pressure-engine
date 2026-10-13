# Pressure Engine — Phase A Diagnostic Report

Generated: **2026-10-13T14:11:39.590195+00:00** · model: **pressure_states_v1** (weights PROVISIONAL EQUAL — not locked, no online learning)

> Shadow-only. No trades. Raw forward-collected telemetry. Numbers without FULL-observation sample sizes are not evidence of edge.

## Runtime coverage (GitHub Actions)

- Runs: **11488** · Observed: **697,053.0s** of expected **1,011,997.0s** → coverage **68.9%**
- Blind gaps recorded: **500**

## Current state by symbol

| Symbol | State | LONG | SHORT | Coverage | OI 1m | CVD 60s | Imb10 | Liquidity | Effort (L/S) | FFP |
|---|---|---|---|---|---|---|---|---|---|---|
| NEAR | NEUTRAL | **18.6** | **23.8** | PARTIAL_TAPE(4687) | 15810158 | 5103.0 | -0.29 | LIQUIDITY_REMOVAL_UNCERTAIN | ABSORPTION/ABSORPTION | 0/0 |
| BTC | NEUTRAL | **30.0** | **39.2** | PARTIAL_TAPE | 32517 | -1.2 | 0.75 | CONSUMED_WITH_PRINTS | UNKNOWN/ABSORPTION | 0/0 |
| ETH | NEUTRAL | **34.2** | **25.1** | PARTIAL_TAPE(8926) | 747801 | -259.9 | 0.94 | CONSUMED_WITH_PRINTS | ABSORPTION/ABSORPTION | 0/0 |
| SOL | NEUTRAL | **52.2** | **17.9** | PARTIAL_TAPE | 4021645 | 977.5 | 0.56 | CONSUMED_WITH_PRINTS | ABSORPTION/ABSORPTION | 0/0 |
| XRP | NEUTRAL | **36.8** | **22.0** | PARTIAL_TAPE(2418) | 175347403 | 68463.0 | -0.56 | LIQUIDITY_REMOVAL_UNCERTAIN | ABSORPTION/ABSORPTION | 0/0 |

Component status per symbol (latest evaluation):

**NEAR**

- LONG: score **18.6** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.44(PARTIAL_TAPE), liquidity=0.12(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **23.8** — location=0.00(NO_LEVEL_NEAR), positioning=0.75(COUNTER_POSITIONS_UNWINDING), flow=0.00(PARTIAL_TAPE), liquidity=0.48(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

**BTC**

- LONG: score **30.0** — location=0.12(swing_high), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(PARTIAL_TAPE), liquidity=1.00(OK), effortresult=0.33(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **39.2** — location=0.69(swing_low), positioning=0.75(COUNTER_POSITIONS_UNWINDING), flow=0.31(PARTIAL_TAPE), liquidity=0.40(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

**ETH**

- LONG: score **34.2** — location=0.00(NO_LEVEL_NEAR), positioning=0.85(PRICE_WITH_DIR_OI_RISING), flow=0.00(PARTIAL_TAPE), liquidity=1.00(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **25.1** — location=0.00(swing_low), positioning=0.35(NO_POSITIONING_INFO), flow=0.55(PARTIAL_TAPE), liquidity=0.40(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

**SOL**

- LONG: score **52.2** — location=0.94(session_high), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.45(PARTIAL_TAPE), liquidity=1.00(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **17.9** — location=0.12(swing_low), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(PARTIAL_TAPE), liquidity=0.40(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

**XRP**

- LONG: score **36.8** — location=0.91(session_high), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.54(PARTIAL_TAPE), liquidity=0.00(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **22.0** — location=0.17(swing_low), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(PARTIAL_TAPE), liquidity=0.60(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

## Forward-outcome experiment (cumulative)

- Pressure setups recorded: **583** (active: 0, finalized: 583)

- Valid (FULL) +120s observations: **0** · Partial: **583** · Unobserved windows (excluded, per §14): **0**
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
