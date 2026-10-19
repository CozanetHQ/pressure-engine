# Pressure Engine — Phase A Diagnostic Report

Generated: **2026-10-19T14:25:14.368532+00:00** · model: **pressure_states_v1** (weights PROVISIONAL EQUAL — not locked, no online learning)

> Shadow-only. No trades. Raw forward-collected telemetry. Numbers without FULL-observation sample sizes are not evidence of edge.

## Runtime coverage (GitHub Actions)

- Runs: **17318** · Observed: **1,051,305.0s** of expected **1,531,212.0s** → coverage **68.7%**
- Blind gaps recorded: **500**

## Current state by symbol

| Symbol | State | LONG | SHORT | Coverage | OI 1m | CVD 60s | Imb10 | Liquidity | Effort (L/S) | FFP |
|---|---|---|---|---|---|---|---|---|---|---|
| NEAR | NEUTRAL | **11.9** | **39.9** | PARTIAL_TAPE(6546) | 16071375 | -5388.0 | -0.23 | LIQUIDITY_REMOVAL_UNCERTAIN | ABSORPTION/ABSORPTION | 0/0 |
| BTC | NEUTRAL | **18.9** | **43.5** | PARTIAL_TAPE(26535) | 33871 | -0.8 | 0.41 | LIQUIDITY_REMOVAL_UNCERTAIN | ABSORPTION/EXPANSION_ | 0/0 |
| ETH | NEUTRAL | **26.3** | **26.5** | PARTIAL_TAPE(15119) | 739823 | -454.6 | 0.54 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/ABSORPTION | 0/0 |
| SOL | SHORT_PRESSURE_BUILDING | **25.8** | **32.7** | PARTIAL_TAPE(5710) | 4034895 | -1443.1 | 0.58 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/ABSORPTION | 0/0 |
| XRP | NEUTRAL | **18.7** | **38.4** | PARTIAL_TAPE(3672) | 185816703 | -75834.0 | -0.07 | LIQUIDITY_REMOVAL_UNCERTAIN | ABSORPTION/UNKNOWN | 0/0 |

Component status per symbol (latest evaluation):

**NEAR**

- LONG: score **11.9** — location=0.00(swing_high), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.16(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **39.9** — location=0.70(swing_low), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.51(FULL), liquidity=0.44(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

**BTC**

- LONG: score **18.9** — location=0.02(swing_high), positioning=0.35(NO_POSITIONING_INFO), flow=0.01(PARTIAL_TAPE), liquidity=0.55(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **43.5** — location=0.71(swing_low), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.30(PARTIAL_TAPE), liquidity=0.05(OK), effortresult=1.00(EXPANSION_CANDIDATE), forcedflowproxy=0.00(OK)

**ETH**

- LONG: score **26.3** — location=0.43(swing_high), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(PARTIAL_TAPE), liquidity=0.60(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **26.5** — location=0.00(NO_LEVEL_NEAR), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.84(PARTIAL_TAPE), liquidity=0.00(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

**SOL**

- LONG: score **25.8** — location=0.00(NO_LEVEL_NEAR), positioning=0.75(COUNTER_POSITIONS_UNWINDING), flow=0.00(PARTIAL_TAPE), liquidity=0.60(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **32.7** — location=0.86(swing_low), positioning=0.35(NO_POSITIONING_INFO), flow=0.55(PARTIAL_TAPE), liquidity=0.00(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

**XRP**

- LONG: score **18.7** — location=0.31(swing_high), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.26(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **38.4** — location=0.66(swing_low), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.49(FULL), liquidity=0.34(OK), effortresult=0.27(UNKNOWN), forcedflowproxy=0.00(OK)

## Forward-outcome experiment (cumulative)

- Pressure setups recorded: **847** (active: 3, finalized: 844)

- Valid (FULL) +120s observations: **0** · Partial: **844** · Unobserved windows (excluded, per §14): **0**
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
