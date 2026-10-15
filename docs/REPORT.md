# Pressure Engine — Phase A Diagnostic Report

Generated: **2026-10-15T23:10:56.847188+00:00** · model: **pressure_states_v1** (weights PROVISIONAL EQUAL — not locked, no online learning)

> Shadow-only. No trades. Raw forward-collected telemetry. Numbers without FULL-observation sample sizes are not evidence of edge.

## Runtime coverage (GitHub Actions)

- Runs: **13711** · Observed: **832,591.0s** of expected **1,217,154.0s** → coverage **68.4%**
- Blind gaps recorded: **500**

## Current state by symbol

| Symbol | State | LONG | SHORT | Coverage | OI 1m | CVD 60s | Imb10 | Liquidity | Effort (L/S) | FFP |
|---|---|---|---|---|---|---|---|---|---|---|
| NEAR | SHORT_PRESSURE_BUILDING | **16.5** | **56.0** | PARTIAL_TAPE(5697) | 16347626 | -16787.0 | -0.89 | CONSUMED_WITH_PRINTS | UNKNOWN/ABSORPTION | 0/0 |
| BTC | NEUTRAL | **18.2** | **33.5** | PARTIAL_TAPE(22373) | 33940 | 0.6 | -0.76 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/UNKNOWN | 0/0 |
| ETH | NEUTRAL | **22.8** | **18.6** | PARTIAL_TAPE(11937) | 783248 | 16.4 | -0.00 | LIQUIDITY_REMOVAL_UNCERTAIN | ABSORPTION/ABSORPTION | 0/0 |
| SOL | NEUTRAL | **22.6** | **14.3** | PARTIAL_TAPE(4592) | 4037347 | 62.4 | -0.01 | LIQUIDITY_REMOVAL_UNCERTAIN | ABSORPTION/UNKNOWN | 0/0 |
| XRP | NEUTRAL | **26.7** | **38.2** | PARTIAL_TAPE(3097) | 171981436 | -17057.0 | -0.19 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/ABSORPTION | 0/0 |

Component status per symbol (latest evaluation):

**NEAR**

- LONG: score **16.5** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.40(OK), effortresult=0.24(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **56.0** — location=0.65(session_low), positioning=0.85(PRICE_WITH_DIR_OI_RISING), flow=0.66(FULL), liquidity=1.00(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

**BTC**

- LONG: score **18.2** — location=0.00(NO_LEVEL_NEAR), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.34(FULL), liquidity=0.00(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **33.5** — location=0.86(swing_low), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.60(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)

**ETH**

- LONG: score **22.8** — location=0.00(swing_high), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.32(FULL), liquidity=0.30(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **18.6** — location=0.26(session_low), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.30(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

**SOL**

- LONG: score **22.6** — location=0.00(NO_LEVEL_NEAR), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.32(FULL), liquidity=0.29(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **14.3** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.31(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)

**XRP**

- LONG: score **26.7** — location=0.86(swing_high), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.19(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **38.2** — location=0.73(session_low), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.40(FULL), liquidity=0.41(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

## Forward-outcome experiment (cumulative)

- Pressure setups recorded: **684** (active: 0, finalized: 684)

- Valid (FULL) +120s observations: **0** · Partial: **684** · Unobserved windows (excluded, per §14): **0**
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
