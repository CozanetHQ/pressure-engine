# Pressure Engine — Phase A Diagnostic Report

Generated: **2026-10-11T21:23:39.791264+00:00** · model: **pressure_states_v1** (weights PROVISIONAL EQUAL — not locked, no online learning)

> Shadow-only. No trades. Raw forward-collected telemetry. Numbers without FULL-observation sample sizes are not evidence of edge.

## Runtime coverage (GitHub Actions)

- Runs: **9692** · Observed: **587,958.0s** of expected **865,117.0s** → coverage **68.0%**
- Blind gaps recorded: **500**

## Current state by symbol

| Symbol | State | LONG | SHORT | Coverage | OI 1m | CVD 60s | Imb10 | Liquidity | Effort (L/S) | FFP |
|---|---|---|---|---|---|---|---|---|---|---|
| NEAR | SHORT_PRESSURE_BUILDING | **19.2** | **34.3** | PARTIAL_TAPE(3663) | 16464895 | -3786.0 | 0.57 | LIQUIDITY_REMOVAL_UNCERTAIN | ABSORPTION/UNKNOWN | 0/0 |
| BTC | NEUTRAL | **22.3** | **16.5** | PARTIAL_TAPE(13160) | 33346 | -0.7 | 0.48 | LIQUIDITY_REMOVAL_UNCERTAIN | ABSORPTION/UNKNOWN | 0/0 |
| ETH | NEUTRAL | **37.4** | **15.8** | PARTIAL_TAPE(6719) | 763331 | 120.8 | 0.61 | CONSUMED_WITH_PRINTS | ABSORPTION/ABSORPTION | 0/0 |
| SOL | NEUTRAL | **30.4** | **27.1** | PARTIAL_TAPE(2582) | 4172245 | -281.0 | 0.23 | LIQUIDITY_REMOVAL_UNCERTAIN | ABSORPTION/ABSORPTION | 0/0 |
| XRP | NEUTRAL | **20.9** | **21.2** | PARTIAL_TAPE(1816) | 189977737 | -17783.0 | -0.01 | LIQUIDITY_REMOVAL_UNCERTAIN | ABSORPTION/ABSORPTION | 0/0 |

Component status per symbol (latest evaluation):

**NEAR**

- LONG: score **19.2** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(PARTIAL_TAPE), liquidity=0.60(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **34.3** — location=0.46(session_low), positioning=0.85(PRICE_WITH_DIR_OI_RISING), flow=0.40(PARTIAL_TAPE), liquidity=0.00(OK), effortresult=0.35(UNKNOWN), forcedflowproxy=0.00(OK)

**BTC**

- LONG: score **22.3** — location=0.00(NO_LEVEL_NEAR), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.00(PARTIAL_TAPE), liquidity=0.59(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **16.5** — location=0.00(session_low), positioning=0.35(NO_POSITIONING_INFO), flow=0.31(PARTIAL_TAPE), liquidity=0.01(OK), effortresult=0.31(UNKNOWN), forcedflowproxy=0.00(OK)

**ETH**

- LONG: score **37.4** — location=0.00(NO_LEVEL_NEAR), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.49(PARTIAL_TAPE), liquidity=1.00(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **15.8** — location=0.00(session_low), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(PARTIAL_TAPE), liquidity=0.40(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

**SOL**

- LONG: score **30.4** — location=0.64(swing_high), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.00(PARTIAL_TAPE), liquidity=0.44(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **27.1** — location=0.56(swing_low), positioning=0.35(NO_POSITIONING_INFO), flow=0.35(PARTIAL_TAPE), liquidity=0.16(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

**XRP**

- LONG: score **20.9** — location=0.21(swing_high), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.00(FULL), liquidity=0.29(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **21.2** — location=0.00(session_low), positioning=0.35(NO_POSITIONING_INFO), flow=0.42(FULL), liquidity=0.31(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

## Forward-outcome experiment (cumulative)

- Pressure setups recorded: **497** (active: 1, finalized: 496)

- Valid (FULL) +120s observations: **0** · Partial: **496** · Unobserved windows (excluded, per §14): **0**
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
