# Pressure Engine — Phase A Diagnostic Report

Generated: **2026-10-09T08:22:46.215313+00:00** · model: **pressure_states_v1** (weights PROVISIONAL EQUAL — not locked, no online learning)

> Shadow-only. No trades. Raw forward-collected telemetry. Numbers without FULL-observation sample sizes are not evidence of edge.

## Runtime coverage (GitHub Actions)

- Runs: **6946** · Observed: **421,421.0s** of expected **645,464.0s** → coverage **65.3%**
- Blind gaps recorded: **500**

## Current state by symbol

| Symbol | State | LONG | SHORT | Coverage | OI 1m | CVD 60s | Imb10 | Liquidity | Effort (L/S) | FFP |
|---|---|---|---|---|---|---|---|---|---|---|
| NEAR | NEUTRAL | **32.5** | **23.3** | PARTIAL_TAPE(2669) | 16049886 | -9597.0 | 0.85 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/ABSORPTION | 0/0 |
| BTC | NEUTRAL | **30.5** | **24.0** | PARTIAL_TAPE(11341) | 35105 | -3.5 | 0.01 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/ABSORPTION | 0/0 |
| ETH | NEUTRAL | **19.2** | **38.8** | PARTIAL_TAPE(5652) | 780060 | -141.4 | -0.17 | CONSUMED_WITH_PRINTS | ABSORPTION/ABSORPTION | 0/0 |
| SOL | NEUTRAL | **32.5** | **27.1** | PARTIAL_TAPE(2059) | 4236265 | -857.0 | 0.76 | CONSUMED_WITH_PRINTS | UNKNOWN/ABSORPTION | 0/0 |
| XRP | NEUTRAL | **22.0** | **28.1** | PARTIAL_TAPE(1544) | 200779162 | -61422.0 | -0.20 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/ABSORPTION | 0/0 |

Component status per symbol (latest evaluation):

**NEAR**

- LONG: score **32.5** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.60(OK), effortresult=1.00(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **23.3** — location=0.06(swing_low), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.58(FULL), liquidity=0.00(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

**BTC**

- LONG: score **30.5** — location=0.36(swing_high), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(PARTIAL_TAPE), liquidity=0.30(OK), effortresult=0.82(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **24.0** — location=0.00(NO_LEVEL_NEAR), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.39(PARTIAL_TAPE), liquidity=0.30(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

**ETH**

- LONG: score **19.2** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(PARTIAL_TAPE), liquidity=0.60(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **38.8** — location=0.00(NO_LEVEL_NEAR), positioning=0.85(PRICE_WITH_DIR_OI_RISING), flow=0.48(PARTIAL_TAPE), liquidity=0.80(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

**SOL**

- LONG: score **32.5** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(PARTIAL_TAPE), liquidity=1.00(OK), effortresult=0.60(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **27.1** — location=0.00(swing_low), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.48(PARTIAL_TAPE), liquidity=0.40(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

**XRP**

- LONG: score **22.0** — location=0.05(swing_high), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(PARTIAL_TAPE), liquidity=0.18(OK), effortresult=0.74(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **28.1** — location=0.00(NO_LEVEL_NEAR), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.52(PARTIAL_TAPE), liquidity=0.42(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

## Forward-outcome experiment (cumulative)

- Pressure setups recorded: **383** (active: 0, finalized: 383)

- Valid (FULL) +120s observations: **0** · Partial: **383** · Unobserved windows (excluded, per §14): **0**
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
