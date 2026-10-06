# Pressure Engine — Phase A Diagnostic Report

Generated: **2026-10-06T18:29:10.887913+00:00** · model: **pressure_states_v1** (weights PROVISIONAL EQUAL — not locked, no online learning)

> Shadow-only. No trades. Raw forward-collected telemetry. Numbers without FULL-observation sample sizes are not evidence of edge.

## Runtime coverage (GitHub Actions)

- Runs: **4559** · Observed: **276,327.0s** of expected **422,648.0s** → coverage **65.4%**
- Blind gaps recorded: **500**

## Current state by symbol

| Symbol | State | LONG | SHORT | Coverage | OI 1m | CVD 60s | Imb10 | Liquidity | Effort (L/S) | FFP |
|---|---|---|---|---|---|---|---|---|---|---|
| NEAR | NEUTRAL | **35.3** | **36.5** | PARTIAL_TAPE(1119) | 15770198 | -6328.0 | 0.11 | CONSUMED_WITH_PRINTS | UNKNOWN/ABSORPTION | 0/0 |
| BTC | NEUTRAL | **32.3** | **24.6** | PARTIAL_TAPE(6011) | 31640 | 1.2 | -0.58 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/UNKNOWN | 0/0 |
| ETH | NEUTRAL | **18.0** | **18.9** | PARTIAL_TAPE(2480) | 755390 | 4.0 | -0.14 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/UNKNOWN | 0/0 |
| SOL | NEUTRAL | **24.4** | **27.3** | PARTIAL_TAPE(998) | 3875045 | 2510.5 | -0.35 | LIQUIDITY_REMOVAL_UNCERTAIN | ABSORPTION/UNKNOWN | 0/0 |
| XRP | NEUTRAL | **12.2** | **53.1** | PARTIAL_TAPE(753) | 173713114 | -972.0 | -0.22 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/UNKNOWN | 0/0 |

Component status per symbol (latest evaluation):

**NEAR**

- LONG: score **35.3** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.77(OK), effortresult=1.00(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **36.5** — location=0.00(NO_LEVEL_NEAR), positioning=0.85(PRICE_WITH_DIR_OI_RISING), flow=0.51(FULL), liquidity=0.63(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

**BTC**

- LONG: score **32.3** — location=0.00(swing_high), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.39(FULL), liquidity=0.00(OK), effortresult=1.00(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **24.6** — location=0.32(swing_low), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.60(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)

**ETH**

- LONG: score **18.0** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.31(FULL), liquidity=0.22(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **18.9** — location=0.00(NO_LEVEL_NEAR), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.00(FULL), liquidity=0.38(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)

**SOL**

- LONG: score **24.4** — location=0.00(swing_high), positioning=0.35(NO_POSITIONING_INFO), flow=0.82(PARTIAL_TAPE), liquidity=0.09(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **27.3** — location=0.00(NO_LEVEL_NEAR), positioning=0.85(PRICE_WITH_DIR_OI_RISING), flow=0.00(PARTIAL_TAPE), liquidity=0.51(OK), effortresult=0.28(UNKNOWN), forcedflowproxy=0.00(OK)

**XRP**

- LONG: score **12.2** — location=0.01(swing_high), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.17(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **53.1** — location=0.90(swing_low), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.30(FULL), liquidity=0.43(OK), effortresult=1.00(UNKNOWN), forcedflowproxy=0.00(OK)

## Forward-outcome experiment (cumulative)

- Pressure setups recorded: **254** (active: 2, finalized: 252)

- Valid (FULL) +120s observations: **0** · Partial: **252** · Unobserved windows (excluded, per §14): **0**
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
