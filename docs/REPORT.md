# Pressure Engine — Phase A Diagnostic Report

Generated: **2026-10-03T13:40:59.071405+00:00** · model: **pressure_states_v1** (weights PROVISIONAL EQUAL — not locked, no online learning)

> Shadow-only. No trades. Raw forward-collected telemetry. Numbers without FULL-observation sample sizes are not evidence of edge.

## Runtime coverage (GitHub Actions)

- Runs: **1398** · Observed: **84,868.0s** of expected **146,157.0s** → coverage **58.1%**
- Blind gaps recorded: **500**

## Current state by symbol

| Symbol | State | LONG | SHORT | Coverage | OI 1m | CVD 60s | Imb10 | Liquidity | Effort (L/S) | FFP |
|---|---|---|---|---|---|---|---|---|---|---|
| NEAR | NEUTRAL | **19.8** | **22.4** | PARTIAL_TAPE(282) | 15450476 | 1486.0 | -0.05 | LIQUIDITY_REMOVAL_UNCERTAIN | ABSORPTION/UNKNOWN | 0/0 |
| BTC | NEUTRAL | **31.1** | **24.6** | PARTIAL_TAPE | 33080 | 5.4 | -0.37 | CONSUMED_WITH_PRINTS | UNKNOWN/ABSORPTION | 0/0 |
| ETH | NEUTRAL | **29.2** | **15.6** | PARTIAL_TAPE(1032) | 779560 | 58.6 | -0.14 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/ABSORPTION | 0/0 |
| SOL | NEUTRAL | **32.4** | **30.0** | PARTIAL_TAPE(387) | 4035150 | -85.1 | -0.39 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/UNKNOWN | 0/0 |
| XRP | NEUTRAL | **21.1** | **26.3** | PARTIAL_TAPE(348) | 172004753 | -40690.0 | 0.12 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/ABSORPTION | 0/0 |

Component status per symbol (latest evaluation):

**NEAR**

- LONG: score **19.8** — location=0.00(swing_high), positioning=0.35(NO_POSITIONING_INFO), flow=0.37(FULL), liquidity=0.27(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **22.4** — location=0.00(swing_low), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.00(FULL), liquidity=0.33(OK), effortresult=0.46(UNKNOWN), forcedflowproxy=0.00(OK)

**BTC**

- LONG: score **31.1** — location=0.00(swing_high), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.50(PARTIAL_TAPE), liquidity=0.48(OK), effortresult=0.35(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **24.6** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(PARTIAL_TAPE), liquidity=0.92(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

**ETH**

- LONG: score **29.2** — location=0.00(NO_LEVEL_NEAR), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.43(FULL), liquidity=0.22(OK), effortresult=0.56(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **15.6** — location=0.00(swing_low), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.38(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

**SOL**

- LONG: score **32.4** — location=0.32(swing_high), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.00(FULL), liquidity=0.07(OK), effortresult=1.00(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **30.0** — location=0.40(swing_low), positioning=0.35(NO_POSITIONING_INFO), flow=0.32(FULL), liquidity=0.53(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)

**XRP**

- LONG: score **21.1** — location=0.00(swing_high), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.00(FULL), liquidity=0.37(OK), effortresult=0.34(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **26.3** — location=0.33(swing_low), positioning=0.35(NO_POSITIONING_INFO), flow=0.47(FULL), liquidity=0.23(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

## Forward-outcome experiment (cumulative)

- Pressure setups recorded: **83** (active: 0, finalized: 83)

- Valid (FULL) +120s observations: **0** · Partial: **83** · Unobserved windows (excluded, per §14): **0**
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
