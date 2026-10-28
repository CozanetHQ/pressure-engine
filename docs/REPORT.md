# Pressure Engine — Phase A Diagnostic Report

Generated: **2026-10-28T01:28:11.373567+00:00** · model: **pressure_states_v1** (weights PROVISIONAL EQUAL — not locked, no online learning)

> Shadow-only. No trades. Raw forward-collected telemetry. Numbers without FULL-observation sample sizes are not evidence of edge.

## Runtime coverage (GitHub Actions)

- Runs: **25679** · Observed: **1,558,328.0s** of expected **2,262,189.0s** → coverage **68.9%**
- Blind gaps recorded: **500**

## Current state by symbol

| Symbol | State | LONG | SHORT | Coverage | OI 1m | CVD 60s | Imb10 | Liquidity | Effort (L/S) | FFP |
|---|---|---|---|---|---|---|---|---|---|---|
| NEAR | NEUTRAL | **23.9** | **36.0** | PARTIAL_TAPE(8429) | 16678637 | -663.0 | -0.20 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/UNKNOWN | 0/0 |
| BTC | SHORT_PRESSURE_BUILDING | **32.1** | **56.3** | PARTIAL_TAPE(40101) | 37163 | -20.5 | -0.88 | CONSUMED_WITH_PRINTS | UNKNOWN/UNKNOWN | 0/0 |
| ETH | NEUTRAL | **9.2** | **33.7** | PARTIAL_TAPE(28127) | 784093 | -144.0 | -0.94 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/UNKNOWN | 0/0 |
| SOL | NEUTRAL | **30.0** | **24.8** | PARTIAL_TAPE(7836) | 4201189 | 267.8 | -0.26 | LIQUIDITY_REMOVAL_UNCERTAIN | ABSORPTION/UNKNOWN | 0/0 |
| XRP | NEUTRAL | **32.8** | **32.5** | PARTIAL_TAPE(4988) | 184302834 | 1014.0 | -0.16 | LIQUIDITY_REMOVAL_UNCERTAIN | ABSORPTION/EXPANSION_ | 0/0 |

Component status per symbol (latest evaluation):

**NEAR**

- LONG: score **23.9** — location=0.71(swing_high), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.18(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **36.0** — location=0.34(swing_low), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.30(FULL), liquidity=0.42(OK), effortresult=0.54(UNKNOWN), forcedflowproxy=0.00(OK)

**BTC**

- LONG: score **32.1** — location=0.98(swing_high), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(PARTIAL_TAPE), liquidity=0.40(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **56.3** — location=0.66(swing_low), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.93(PARTIAL_TAPE), liquidity=1.00(OK), effortresult=0.24(UNKNOWN), forcedflowproxy=0.00(OK)

**ETH**

- LONG: score **9.2** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.00(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **33.7** — location=0.00(NO_LEVEL_NEAR), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.43(FULL), liquidity=0.60(OK), effortresult=0.45(UNKNOWN), forcedflowproxy=0.00(OK)

**SOL**

- LONG: score **30.0** — location=0.72(swing_high), positioning=0.35(NO_POSITIONING_INFO), flow=0.39(FULL), liquidity=0.14(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **24.8** — location=0.00(NO_LEVEL_NEAR), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.00(FULL), liquidity=0.46(OK), effortresult=0.48(UNKNOWN), forcedflowproxy=0.00(OK)

**XRP**

- LONG: score **32.8** — location=0.90(swing_high), positioning=0.35(NO_POSITIONING_INFO), flow=0.31(FULL), liquidity=0.20(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **32.5** — location=0.00(NO_LEVEL_NEAR), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.00(FULL), liquidity=0.40(OK), effortresult=1.00(EXPANSION_CANDIDATE), forcedflowproxy=0.00(OK)

## Forward-outcome experiment (cumulative)

- Pressure setups recorded: **1115** (active: 1, finalized: 1114)

- Valid (FULL) +120s observations: **0** · Partial: **1114** · Unobserved windows (excluded, per §14): **0**
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
