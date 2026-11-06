# Pressure Engine — Phase A Diagnostic Report

Generated: **2026-11-06T15:06:04.090554+00:00** · model: **pressure_states_v1** (weights PROVISIONAL EQUAL — not locked, no online learning)

> Shadow-only. No trades. Raw forward-collected telemetry. Numbers without FULL-observation sample sizes are not evidence of edge.

## Runtime coverage (GitHub Actions)

- Runs: **34086** · Observed: **2,068,444.0s** of expected **3,088,862.0s** → coverage **67.0%**
- Blind gaps recorded: **500**

## Current state by symbol

| Symbol | State | LONG | SHORT | Coverage | OI 1m | CVD 60s | Imb10 | Liquidity | Effort (L/S) | FFP |
|---|---|---|---|---|---|---|---|---|---|---|
| NEAR | NEUTRAL | **27.0** | **25.1** | PARTIAL_TAPE(10275) | 16733746 | -1170.0 | -0.05 | LIQUIDITY_REMOVAL_UNCERTAIN | ABSORPTION/ABSORPTION | 0/0 |
| BTC | FORCED_FLOW_PROXY_SHORT | **30.2** | **65.7** | PARTIAL_TAPE | 37437 | -40.2 | 0.27 | CONSUMED_WITH_PRINTS | ABSORPTION/ABSORPTION | 0/1 |
| ETH | SHORT_PRESSURE_BUILDING | **26.4** | **41.5** | PARTIAL_TAPE | 795642 | -8.2 | -0.11 | CONSUMED_WITH_PRINTS | ABSORPTION/ABSORPTION | 0/0 |
| SOL | EXHAUSTION_SHORT | **42.4** | **54.2** | PARTIAL_TAPE(10796) | 4271962 | -4938.7 | -0.00 | CONSUMED_WITH_PRINTS | ABSORPTION/ABSORPTION | 0/1 |
| XRP | NEUTRAL | **12.5** | **37.0** | PARTIAL_TAPE(6650) | 191385257 | -113114.0 | -0.17 | LIQUIDITY_REMOVAL_UNCERTAIN | ABSORPTION/ABSORPTION | 0/0 |

Component status per symbol (latest evaluation):

**NEAR**

- LONG: score **27.0** — location=0.80(swing_high), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(PARTIAL_TAPE), liquidity=0.27(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **25.1** — location=0.10(swing_low), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.33(PARTIAL_TAPE), liquidity=0.33(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

**BTC**

- LONG: score **30.2** — location=0.00(NO_LEVEL_NEAR), positioning=0.75(COUNTER_POSITIONS_UNWINDING), flow=0.00(PARTIAL_TAPE), liquidity=0.86(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **65.7** — location=0.85(session_low), positioning=0.35(NO_POSITIONING_INFO), flow=1.00(PARTIAL_TAPE), liquidity=0.54(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=1.00(FORCED_FLOW_PROXY_CONDITIONS_MET)

**ETH**

- LONG: score **26.4** — location=0.00(NO_LEVEL_NEAR), positioning=0.75(COUNTER_POSITIONS_UNWINDING), flow=0.00(PARTIAL_TAPE), liquidity=0.64(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **41.5** — location=0.87(swing_low), positioning=0.35(NO_POSITIONING_INFO), flow=0.31(PARTIAL_TAPE), liquidity=0.76(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

**SOL**

- LONG: score **42.4** — location=0.90(swing_high), positioning=0.75(COUNTER_POSITIONS_UNWINDING), flow=0.00(PARTIAL_TAPE), liquidity=0.70(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **54.2** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=1.00(PARTIAL_TAPE), liquidity=0.70(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=1.00(FORCED_FLOW_PROXY_CONDITIONS_MET)

**XRP**

- LONG: score **12.5** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(PARTIAL_TAPE), liquidity=0.20(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **37.0** — location=0.34(session_low), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.73(PARTIAL_TAPE), liquidity=0.40(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

## Forward-outcome experiment (cumulative)

- Pressure setups recorded: **1444** (active: 3, finalized: 1441)

- Valid (FULL) +120s observations: **0** · Partial: **1441** · Unobserved windows (excluded, per §14): **0**
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
