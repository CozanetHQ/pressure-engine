# Pressure Engine — Phase A Diagnostic Report

Generated: **2026-10-03T22:13:47.096855+00:00** · model: **pressure_states_v1** (weights PROVISIONAL EQUAL — not locked, no online learning)

> Shadow-only. No trades. Raw forward-collected telemetry. Numbers without FULL-observation sample sizes are not evidence of edge.

## Runtime coverage (GitHub Actions)

- Runs: **1779** · Observed: **107,916.0s** of expected **176,925.0s** → coverage **61.0%**
- Blind gaps recorded: **500**

## Current state by symbol

| Symbol | State | LONG | SHORT | Coverage | OI 1m | CVD 60s | Imb10 | Liquidity | Effort (L/S) | FFP |
|---|---|---|---|---|---|---|---|---|---|---|
| NEAR | NEUTRAL | **23.0** | **29.2** | PARTIAL_TAPE(333) | 15352778 | 4178.0 | 0.13 | LIQUIDITY_REMOVAL_UNCERTAIN | ABSORPTION/UNKNOWN | 0/0 |
| BTC | NEUTRAL | **31.9** | **23.0** | PARTIAL_TAPE(2227) | 33012 | 1.7 | 0.57 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/ABSORPTION | 0/0 |
| ETH | NEUTRAL | **28.7** | **24.9** | PARTIAL_TAPE(1073) | 778971 | -2.4 | -0.06 | LIQUIDITY_REMOVAL_UNCERTAIN | ABSORPTION/UNKNOWN | 0/0 |
| SOL | NEUTRAL | **38.4** | **19.1** | PARTIAL_TAPE(409) | 4032899 | 308.1 | 0.47 | LIQUIDITY_REMOVAL_UNCERTAIN | ABSORPTION/EXPANSION_ | 0/0 |
| XRP | NEUTRAL | **34.3** | **30.6** | PARTIAL_TAPE(372) | 171126608 | 1088.0 | -0.31 | LIQUIDITY_REMOVAL_UNCERTAIN | ABSORPTION/EXPANSION_ | 0/0 |

Component status per symbol (latest evaluation):

**NEAR**

- LONG: score **23.0** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.45(PARTIAL_TAPE), liquidity=0.38(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **29.2** — location=0.00(NO_LEVEL_NEAR), positioning=0.85(PRICE_WITH_DIR_OI_RISING), flow=0.00(PARTIAL_TAPE), liquidity=0.22(OK), effortresult=0.68(UNKNOWN), forcedflowproxy=0.00(OK)

**BTC**

- LONG: score **31.9** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.39(PARTIAL_TAPE), liquidity=0.60(OK), effortresult=0.58(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **23.0** — location=0.43(swing_low), positioning=0.75(COUNTER_POSITIONS_UNWINDING), flow=0.00(PARTIAL_TAPE), liquidity=0.00(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

**ETH**

- LONG: score **28.7** — location=0.71(swing_high), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.00(PARTIAL_TAPE), liquidity=0.27(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **24.9** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.33(PARTIAL_TAPE), liquidity=0.33(OK), effortresult=0.48(UNKNOWN), forcedflowproxy=0.00(OK)

**SOL**

- LONG: score **38.4** — location=0.52(swing_high), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.46(PARTIAL_TAPE), liquidity=0.58(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **19.1** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(PARTIAL_TAPE), liquidity=0.02(OK), effortresult=0.78(EXPANSION_CANDIDATE), forcedflowproxy=0.00(OK)

**XRP**

- LONG: score **34.3** — location=0.88(swing_high), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.31(FULL), liquidity=0.12(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **30.6** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.48(OK), effortresult=1.00(EXPANSION_CANDIDATE), forcedflowproxy=0.00(OK)

## Forward-outcome experiment (cumulative)

- Pressure setups recorded: **86** (active: 0, finalized: 86)

- Valid (FULL) +120s observations: **0** · Partial: **86** · Unobserved windows (excluded, per §14): **0**
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
