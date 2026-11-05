# Pressure Engine — Phase A Diagnostic Report

Generated: **2026-11-05T12:22:38.296601+00:00** · model: **pressure_states_v1** (weights PROVISIONAL EQUAL — not locked, no online learning)

> Shadow-only. No trades. Raw forward-collected telemetry. Numbers without FULL-observation sample sizes are not evidence of edge.

## Runtime coverage (GitHub Actions)

- Runs: **33276** · Observed: **2,019,283.0s** of expected **2,992,656.0s** → coverage **67.5%**
- Blind gaps recorded: **500**

## Current state by symbol

| Symbol | State | LONG | SHORT | Coverage | OI 1m | CVD 60s | Imb10 | Liquidity | Effort (L/S) | FFP |
|---|---|---|---|---|---|---|---|---|---|---|
| NEAR | SHORT_PRESSURE_BUILDING | **20.2** | **33.6** | PARTIAL_TAPE(10032) | 16792889 | -10140.0 | 0.27 | LIQUIDITY_REMOVAL_UNCERTAIN | ABSORPTION/ABSORPTION | 0/0 |
| BTC | SHORT_PRESSURE_BUILDING | **18.8** | **41.2** | PARTIAL_TAPE(53427) | 37482 | 8.0 | -0.94 | LIQUIDITY_REMOVAL_UNCERTAIN | ABSORPTION/UNKNOWN | 0/0 |
| ETH | SHORT_PRESSURE_BUILDING | **25.0** | **48.4** | PARTIAL_TAPE(37112) | 812845 | 347.6 | -0.84 | LIQUIDITY_REMOVAL_UNCERTAIN | ABSORPTION/EXPANSION_ | 0/0 |
| SOL | NEUTRAL | **23.9** | **19.1** | PARTIAL_TAPE(10326) | 4397086 | 211.3 | 0.02 | LIQUIDITY_REMOVAL_UNCERTAIN | ABSORPTION/UNKNOWN | 0/0 |
| XRP | NEUTRAL | **27.5** | **43.1** | PARTIAL_TAPE(6290) | 193822374 | 4722.0 | -0.09 | LIQUIDITY_REMOVAL_UNCERTAIN | ABSORPTION/UNKNOWN | 0/0 |

Component status per symbol (latest evaluation):

**NEAR**

- LONG: score **20.2** — location=0.00(NO_LEVEL_NEAR), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.00(FULL), liquidity=0.46(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **33.6** — location=0.72(swing_low), positioning=0.35(NO_POSITIONING_INFO), flow=0.61(FULL), liquidity=0.14(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

**BTC**

- LONG: score **18.8** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.58(PARTIAL_TAPE), liquidity=0.00(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **41.2** — location=0.77(swing_low), positioning=0.75(COUNTER_POSITIONS_UNWINDING), flow=0.00(PARTIAL_TAPE), liquidity=0.60(OK), effortresult=0.35(UNKNOWN), forcedflowproxy=0.00(OK)

**ETH**

- LONG: score **25.0** — location=0.00(NO_LEVEL_NEAR), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.75(PARTIAL_TAPE), liquidity=0.00(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **48.4** — location=0.95(swing_low), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(PARTIAL_TAPE), liquidity=0.60(OK), effortresult=1.00(EXPANSION_CANDIDATE), forcedflowproxy=0.00(OK)

**SOL**

- LONG: score **23.9** — location=0.00(swing_high), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.37(FULL), liquidity=0.31(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **19.1** — location=0.02(session_low), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.29(OK), effortresult=0.49(UNKNOWN), forcedflowproxy=0.00(OK)

**XRP**

- LONG: score **27.5** — location=0.32(swing_high), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.33(FULL), liquidity=0.25(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **43.1** — location=0.89(swing_low), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.35(OK), effortresult=1.00(UNKNOWN), forcedflowproxy=0.00(OK)

## Forward-outcome experiment (cumulative)

- Pressure setups recorded: **1399** (active: 1, finalized: 1398)

- Valid (FULL) +120s observations: **0** · Partial: **1398** · Unobserved windows (excluded, per §14): **0**
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
