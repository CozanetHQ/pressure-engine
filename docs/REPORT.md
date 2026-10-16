# Pressure Engine — Phase A Diagnostic Report

Generated: **2026-10-16T03:44:40.708069+00:00** · model: **pressure_states_v1** (weights PROVISIONAL EQUAL — not locked, no online learning)

> Shadow-only. No trades. Raw forward-collected telemetry. Numbers without FULL-observation sample sizes are not evidence of edge.

## Runtime coverage (GitHub Actions)

- Runs: **13910** · Observed: **844,734.0s** of expected **1,233,578.0s** → coverage **68.5%**
- Blind gaps recorded: **500**

## Current state by symbol

| Symbol | State | LONG | SHORT | Coverage | OI 1m | CVD 60s | Imb10 | Liquidity | Effort (L/S) | FFP |
|---|---|---|---|---|---|---|---|---|---|---|
| NEAR | NEUTRAL | **22.1** | **29.4** | PARTIAL_TAPE(5747) | 16311865 | 4250.0 | -0.33 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/ABSORPTION | 0/0 |
| BTC | LONG_PRESSURE_BUILDING | **52.2** | **13.8** | PARTIAL_TAPE(22582) | 33868 | 22.7 | 0.04 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/UNKNOWN | 0/0 |
| ETH | SHORT_PRESSURE_BUILDING | **30.1** | **22.6** | PARTIAL_TAPE(12052) | 788706 | 478.0 | -0.63 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/ABSORPTION | 0/0 |
| SOL | SHORT_PRESSURE_BUILDING | **37.2** | **31.6** | PARTIAL_TAPE(4610) | 4068489 | 3548.6 | -0.20 | LIQUIDITY_REMOVAL_UNCERTAIN | ABSORPTION/ABSORPTION | 0/0 |
| XRP | SHORT_PRESSURE_BUILDING | **29.0** | **12.3** | PARTIAL_TAPE(3113) | 172998290 | 41766.0 | 0.19 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/ABSORPTION | 0/0 |

Component status per symbol (latest evaluation):

**NEAR**

- LONG: score **22.1** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.42(PARTIAL_TAPE), liquidity=0.10(OK), effortresult=0.46(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **29.4** — location=0.32(session_low), positioning=0.75(COUNTER_POSITIONS_UNWINDING), flow=0.00(PARTIAL_TAPE), liquidity=0.50(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

**BTC**

- LONG: score **52.2** — location=0.88(swing_high), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=1.00(PARTIAL_TAPE), liquidity=0.32(OK), effortresult=0.38(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **13.8** — location=0.00(session_low), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(PARTIAL_TAPE), liquidity=0.28(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)

**ETH**

- LONG: score **30.1** — location=0.00(swing_high), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=1.00(PARTIAL_TAPE), liquidity=0.00(OK), effortresult=0.26(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **22.6** — location=0.20(session_low), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(PARTIAL_TAPE), liquidity=0.60(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

**SOL**

- LONG: score **37.2** — location=0.00(swing_high), positioning=0.85(PRICE_WITH_DIR_OI_RISING), flow=1.00(PARTIAL_TAPE), liquidity=0.18(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **31.6** — location=0.93(session_low), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(PARTIAL_TAPE), liquidity=0.42(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

**XRP**

- LONG: score **29.0** — location=0.00(NO_LEVEL_NEAR), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.45(PARTIAL_TAPE), liquidity=0.41(OK), effortresult=0.32(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **12.3** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(PARTIAL_TAPE), liquidity=0.19(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

## Forward-outcome experiment (cumulative)

- Pressure setups recorded: **689** (active: 4, finalized: 685)

- Valid (FULL) +120s observations: **0** · Partial: **685** · Unobserved windows (excluded, per §14): **0**
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
