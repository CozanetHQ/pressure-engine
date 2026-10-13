# Pressure Engine — Phase A Diagnostic Report

Generated: **2026-10-13T14:19:57.112905+00:00** · model: **pressure_states_v1** (weights PROVISIONAL EQUAL — not locked, no online learning)

> Shadow-only. No trades. Raw forward-collected telemetry. Numbers without FULL-observation sample sizes are not evidence of edge.

## Runtime coverage (GitHub Actions)

- Runs: **11494** · Observed: **697,420.0s** of expected **1,012,495.0s** → coverage **68.9%**
- Blind gaps recorded: **500**

## Current state by symbol

| Symbol | State | LONG | SHORT | Coverage | OI 1m | CVD 60s | Imb10 | Liquidity | Effort (L/S) | FFP |
|---|---|---|---|---|---|---|---|---|---|---|
| NEAR | SHORT_PRESSURE_BUILDING | **25.8** | **39.8** | PARTIAL_TAPE(4695) | 15860055 | -6819.0 | 0.52 | CONSUMED_WITH_PRINTS | ABSORPTION/UNKNOWN | 0/0 |
| BTC | SHORT_PRESSURE_BUILDING | **30.0** | **53.0** | PARTIAL_TAPE | 32310 | -7.9 | -0.67 | CONSUMED_WITH_PRINTS | ABSORPTION/UNKNOWN | 0/0 |
| ETH | LONG_PRESSURE_BUILDING | **20.1** | **48.5** | PARTIAL_TAPE(8951) | 746594 | -1.3 | -0.07 | CONSUMED_WITH_PRINTS | ABSORPTION/UNKNOWN | 0/0 |
| SOL | NEUTRAL | **24.5** | **26.9** | PARTIAL_TAPE(3478) | 4005782 | 181.9 | 0.73 | LIQUIDITY_REMOVAL_UNCERTAIN | ABSORPTION/UNKNOWN | 0/0 |
| XRP | PRESSURE_FAILED | **34.2** | **19.1** | PARTIAL_TAPE(2424) | 174630295 | 89590.0 | 0.04 | LIQUIDITY_REMOVAL_UNCERTAIN | ABSORPTION/UNKNOWN | 0/0 |

Component status per symbol (latest evaluation):

**NEAR**

- LONG: score **25.8** — location=0.00(swing_high), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(PARTIAL_TAPE), liquidity=1.00(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **39.8** — location=0.56(swing_low), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.49(PARTIAL_TAPE), liquidity=0.40(OK), effortresult=0.39(UNKNOWN), forcedflowproxy=0.00(OK)

**BTC**

- LONG: score **30.0** — location=0.45(swing_high), positioning=0.75(COUNTER_POSITIONS_UNWINDING), flow=0.00(PARTIAL_TAPE), liquidity=0.40(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **53.0** — location=0.67(swing_low), positioning=0.35(NO_POSITIONING_INFO), flow=0.48(PARTIAL_TAPE), liquidity=1.00(OK), effortresult=0.68(UNKNOWN), forcedflowproxy=0.00(OK)

**ETH**

- LONG: score **20.1** — location=0.00(swing_high), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(PARTIAL_TAPE), liquidity=0.66(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **48.5** — location=0.77(swing_low), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.30(PARTIAL_TAPE), liquidity=0.74(OK), effortresult=0.54(UNKNOWN), forcedflowproxy=0.00(OK)

**SOL**

- LONG: score **24.5** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.32(PARTIAL_TAPE), liquidity=0.60(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **26.9** — location=0.43(swing_low), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.00(PARTIAL_TAPE), liquidity=0.00(OK), effortresult=0.63(UNKNOWN), forcedflowproxy=0.00(OK)

**XRP**

- LONG: score **34.2** — location=0.16(swing_high), positioning=0.75(COUNTER_POSITIONS_UNWINDING), flow=0.62(PARTIAL_TAPE), liquidity=0.32(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **19.1** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(PARTIAL_TAPE), liquidity=0.28(OK), effortresult=0.52(UNKNOWN), forcedflowproxy=0.00(OK)

## Forward-outcome experiment (cumulative)

- Pressure setups recorded: **587** (active: 1, finalized: 586)

- Valid (FULL) +120s observations: **0** · Partial: **586** · Unobserved windows (excluded, per §14): **0**
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
