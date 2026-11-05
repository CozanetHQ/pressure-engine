# Pressure Engine — Phase A Diagnostic Report

Generated: **2026-11-05T05:40:11.731751+00:00** · model: **pressure_states_v1** (weights PROVISIONAL EQUAL — not locked, no online learning)

> Shadow-only. No trades. Raw forward-collected telemetry. Numbers without FULL-observation sample sizes are not evidence of edge.

## Runtime coverage (GitHub Actions)

- Runs: **33011** · Observed: **2,003,218.0s** of expected **2,968,509.0s** → coverage **67.5%**
- Blind gaps recorded: **500**

## Current state by symbol

| Symbol | State | LONG | SHORT | Coverage | OI 1m | CVD 60s | Imb10 | Liquidity | Effort (L/S) | FFP |
|---|---|---|---|---|---|---|---|---|---|---|
| NEAR | LONG_PRESSURE_BUILDING | **39.6** | **20.6** | PARTIAL_TAPE(10027) | 17072063 | -95.0 | 0.02 | LIQUIDITY_REMOVAL_UNCERTAIN | ABSORPTION/ABSORPTION | 0/0 |
| BTC | NEUTRAL | **30.7** | **23.3** | PARTIAL_TAPE(53156) | 37276 | 2.2 | -0.24 | CONSUMED_WITH_PRINTS | UNKNOWN/ABSORPTION | 0/0 |
| ETH | NEUTRAL | **39.7** | **16.6** | PARTIAL_TAPE(36919) | 788557 | 75.5 | -0.24 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/UNKNOWN | 0/0 |
| SOL | LONG_PRESSURE_BUILDING | **32.4** | **26.7** | PARTIAL_TAPE(10291) | 4398971 | 822.6 | -0.59 | LIQUIDITY_REMOVAL_UNCERTAIN | ABSORPTION/UNKNOWN | 0/0 |
| XRP | NEUTRAL | **23.6** | **14.6** | PARTIAL_TAPE(6267) | 190303544 | 3257.0 | -0.04 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/ABSORPTION | 0/0 |

Component status per symbol (latest evaluation):

**NEAR**

- LONG: score **39.6** — location=0.84(swing_high), positioning=0.35(NO_POSITIONING_INFO), flow=0.68(FULL), liquidity=0.31(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **20.6** — location=0.00(swing_low), positioning=0.75(COUNTER_POSITIONS_UNWINDING), flow=0.00(FULL), liquidity=0.29(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

**BTC**

- LONG: score **30.7** — location=0.00(NO_LEVEL_NEAR), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.38(PARTIAL_TAPE), liquidity=0.55(OK), effortresult=0.35(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **23.3** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(PARTIAL_TAPE), liquidity=0.85(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

**ETH**

- LONG: score **39.7** — location=0.90(swing_high), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.42(PARTIAL_TAPE), liquidity=0.15(OK), effortresult=0.36(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **16.6** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(PARTIAL_TAPE), liquidity=0.45(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)

**SOL**

- LONG: score **32.4** — location=0.85(swing_high), positioning=0.35(NO_POSITIONING_INFO), flow=0.55(FULL), liquidity=0.00(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **26.7** — location=0.05(swing_low), positioning=0.75(COUNTER_POSITIONS_UNWINDING), flow=0.00(FULL), liquidity=0.60(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)

**XRP**

- LONG: score **23.6** — location=0.00(NO_LEVEL_NEAR), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.33(FULL), liquidity=0.27(OK), effortresult=0.26(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **14.6** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.33(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

## Forward-outcome experiment (cumulative)

- Pressure setups recorded: **1394** (active: 0, finalized: 1394)

- Valid (FULL) +120s observations: **0** · Partial: **1394** · Unobserved windows (excluded, per §14): **0**
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
