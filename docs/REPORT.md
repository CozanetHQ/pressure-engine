# Pressure Engine — Phase A Diagnostic Report

Generated: **2026-10-30T00:08:05.664881+00:00** · model: **pressure_states_v1** (weights PROVISIONAL EQUAL — not locked, no online learning)

> Shadow-only. No trades. Raw forward-collected telemetry. Numbers without FULL-observation sample sizes are not evidence of edge.

## Runtime coverage (GitHub Actions)

- Runs: **27579** · Observed: **1,673,718.0s** of expected **2,430,183.0s** → coverage **68.9%**
- Blind gaps recorded: **500**

## Current state by symbol

| Symbol | State | LONG | SHORT | Coverage | OI 1m | CVD 60s | Imb10 | Liquidity | Effort (L/S) | FFP |
|---|---|---|---|---|---|---|---|---|---|---|
| NEAR | NEUTRAL | **20.8** | **31.1** | PARTIAL_TAPE(9039) | 16669435 | -423.0 | -0.00 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/UNKNOWN | 0/0 |
| BTC | EXPANSION_LONG | **61.0** | **15.8** | PARTIAL_TAPE | 36927 | 16.6 | 0.88 | CONSUMED_WITH_PRINTS | EXPANSION_/UNKNOWN | 0/0 |
| ETH | NEUTRAL | **24.9** | **30.7** | PARTIAL_TAPE | 789776 | 81.3 | -0.20 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/ABSORPTION | 0/0 |
| SOL | NEUTRAL | **37.5** | **19.2** | PARTIAL_TAPE(8830) | 4381035 | 674.4 | -0.62 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/UNKNOWN | 0/0 |
| XRP | NEUTRAL | **37.4** | **14.0** | PARTIAL_TAPE(5534) | 183465303 | 11759.0 | 0.02 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/UNKNOWN | 0/0 |

Component status per symbol (latest evaluation):

**NEAR**

- LONG: score **20.8** — location=0.00(session_high), positioning=0.75(COUNTER_POSITIONS_UNWINDING), flow=0.00(PARTIAL_TAPE), liquidity=0.30(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **31.1** — location=0.71(swing_low), positioning=0.35(NO_POSITIONING_INFO), flow=0.31(PARTIAL_TAPE), liquidity=0.30(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)

**BTC**

- LONG: score **61.0** — location=0.66(session_high), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.70(PARTIAL_TAPE), liquidity=1.00(OK), effortresult=0.75(EXPANSION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **15.8** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(PARTIAL_TAPE), liquidity=0.40(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)

**ETH**

- LONG: score **24.9** — location=0.20(session_high), positioning=0.35(NO_POSITIONING_INFO), flow=0.37(PARTIAL_TAPE), liquidity=0.18(OK), effortresult=0.39(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **30.7** — location=0.67(swing_low), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.00(PARTIAL_TAPE), liquidity=0.42(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

**SOL**

- LONG: score **37.5** — location=0.65(session_high), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.43(PARTIAL_TAPE), liquidity=0.00(OK), effortresult=0.61(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **19.2** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(PARTIAL_TAPE), liquidity=0.60(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)

**XRP**

- LONG: score **37.4** — location=0.31(session_high), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.35(PARTIAL_TAPE), liquidity=0.31(OK), effortresult=0.73(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **14.0** — location=0.00(swing_low), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(PARTIAL_TAPE), liquidity=0.29(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)

## Forward-outcome experiment (cumulative)

- Pressure setups recorded: **1202** (active: 2, finalized: 1200)

- Valid (FULL) +120s observations: **0** · Partial: **1200** · Unobserved windows (excluded, per §14): **0**
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
