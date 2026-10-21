# Pressure Engine — Phase A Diagnostic Report

Generated: **2026-10-21T15:10:52.367057+00:00** · model: **pressure_states_v1** (weights PROVISIONAL EQUAL — not locked, no online learning)

> Shadow-only. No trades. Raw forward-collected telemetry. Numbers without FULL-observation sample sizes are not evidence of edge.

## Runtime coverage (GitHub Actions)

- Runs: **19348** · Observed: **1,174,475.0s** of expected **1,706,750.0s** → coverage **68.8%**
- Blind gaps recorded: **500**

## Current state by symbol

| Symbol | State | LONG | SHORT | Coverage | OI 1m | CVD 60s | Imb10 | Liquidity | Effort (L/S) | FFP |
|---|---|---|---|---|---|---|---|---|---|---|
| NEAR | NEUTRAL | **45.3** | **34.8** | PARTIAL_TAPE(7188) | 16669990 | -19738.0 | 0.19 | CONSUMED_WITH_PRINTS | ABSORPTION/UNKNOWN | 0/0 |
| BTC | LONG_PRESSURE_BUILDING | **42.2** | **27.2** | PARTIAL_TAPE(29882) | 35036 | -11.6 | 0.41 | CONSUMED_WITH_PRINTS | ABSORPTION/UNKNOWN | 0/0 |
| ETH | LONG_PRESSURE_BUILDING | **32.8** | **16.7** | PARTIAL_TAPE | 765019 | -36.5 | 0.27 | LIQUIDITY_REMOVAL_UNCERTAIN | ABSORPTION/ABSORPTION | 0/0 |
| SOL | NEUTRAL | **43.1** | **15.8** | PARTIAL_TAPE(6341) | 4060057 | 877.2 | 0.60 | CONSUMED_WITH_PRINTS | ABSORPTION/ABSORPTION | 0/0 |
| XRP | NEUTRAL | **36.3** | **9.6** | PARTIAL_TAPE(4109) | 181857781 | 193841.0 | 0.46 | LIQUIDITY_REMOVAL_UNCERTAIN | ABSORPTION/ABSORPTION | 0/0 |

Component status per symbol (latest evaluation):

**NEAR**

- LONG: score **45.3** — location=0.85(session_high), positioning=0.85(PRICE_WITH_DIR_OI_RISING), flow=0.00(PARTIAL_TAPE), liquidity=0.81(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **34.8** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.82(PARTIAL_TAPE), liquidity=0.59(OK), effortresult=0.33(UNKNOWN), forcedflowproxy=0.00(OK)

**BTC**

- LONG: score **42.2** — location=0.63(session_high), positioning=0.75(COUNTER_POSITIONS_UNWINDING), flow=0.00(PARTIAL_TAPE), liquidity=0.95(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **27.2** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.58(PARTIAL_TAPE), liquidity=0.45(OK), effortresult=0.24(UNKNOWN), forcedflowproxy=0.00(OK)

**ETH**

- LONG: score **32.8** — location=0.56(session_high), positioning=0.75(COUNTER_POSITIONS_UNWINDING), flow=0.00(PARTIAL_TAPE), liquidity=0.46(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **16.7** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.32(PARTIAL_TAPE), liquidity=0.14(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

**SOL**

- LONG: score **43.1** — location=0.33(session_high), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.51(PARTIAL_TAPE), liquidity=1.00(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **15.8** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(PARTIAL_TAPE), liquidity=0.40(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

**XRP**

- LONG: score **36.3** — location=0.00(NO_LEVEL_NEAR), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.85(PARTIAL_TAPE), liquidity=0.57(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **9.6** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(PARTIAL_TAPE), liquidity=0.03(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

## Forward-outcome experiment (cumulative)

- Pressure setups recorded: **921** (active: 4, finalized: 917)

- Valid (FULL) +120s observations: **0** · Partial: **917** · Unobserved windows (excluded, per §14): **0**
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
