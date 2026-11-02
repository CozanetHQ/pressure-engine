# Pressure Engine — Phase A Diagnostic Report

Generated: **2026-11-02T12:49:24.380909+00:00** · model: **pressure_states_v1** (weights PROVISIONAL EQUAL — not locked, no online learning)

> Shadow-only. No trades. Raw forward-collected telemetry. Numbers without FULL-observation sample sizes are not evidence of edge.

## Runtime coverage (GitHub Actions)

- Runs: **30856** · Observed: **1,872,379.0s** of expected **2,735,062.0s** → coverage **68.5%**
- Blind gaps recorded: **500**

## Current state by symbol

| Symbol | State | LONG | SHORT | Coverage | OI 1m | CVD 60s | Imb10 | Liquidity | Effort (L/S) | FFP |
|---|---|---|---|---|---|---|---|---|---|---|
| NEAR | NEUTRAL | **23.0** | **24.5** | PARTIAL_TAPE(9615) | 16721158 | 1945.0 | -0.10 | LIQUIDITY_REMOVAL_UNCERTAIN | ABSORPTION/UNKNOWN | 0/0 |
| BTC | NEUTRAL | **24.7** | **24.9** | PARTIAL_TAPE(48706) | 35566 | 3.8 | -0.52 | LIQUIDITY_REMOVAL_UNCERTAIN | ABSORPTION/UNKNOWN | 0/0 |
| ETH | NEUTRAL | **31.5** | **28.7** | PARTIAL_TAPE(34284) | 767467 | 35.2 | 0.33 | LIQUIDITY_REMOVAL_UNCERTAIN | ABSORPTION/UNKNOWN | 0/0 |
| SOL | NEUTRAL | **23.1** | **29.2** | PARTIAL_TAPE(9603) | 4299361 | 157.3 | -0.23 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/UNKNOWN | 0/0 |
| XRP | NEUTRAL | **37.1** | **13.2** | PARTIAL_TAPE(5914) | 186041760 | 28286.0 | 0.10 | LIQUIDITY_REMOVAL_UNCERTAIN | ABSORPTION/ABSORPTION | 0/0 |

Component status per symbol (latest evaluation):

**NEAR**

- LONG: score **23.0** — location=0.00(NO_LEVEL_NEAR), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.39(FULL), liquidity=0.24(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **24.5** — location=0.56(swing_low), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.36(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)

**BTC**

- LONG: score **24.7** — location=0.00(swing_high), positioning=0.85(PRICE_WITH_DIR_OI_RISING), flow=0.43(PARTIAL_TAPE), liquidity=0.00(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **24.9** — location=0.35(swing_low), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(PARTIAL_TAPE), liquidity=0.60(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)

**ETH**

- LONG: score **31.5** — location=0.30(swing_high), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.35(PARTIAL_TAPE), liquidity=0.50(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **28.7** — location=0.60(swing_low), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(PARTIAL_TAPE), liquidity=0.10(OK), effortresult=0.66(UNKNOWN), forcedflowproxy=0.00(OK)

**SOL**

- LONG: score **23.1** — location=0.05(swing_high), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.35(FULL), liquidity=0.16(OK), effortresult=0.28(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **29.2** — location=0.76(swing_low), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.44(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)

**XRP**

- LONG: score **37.1** — location=0.59(swing_high), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.53(FULL), liquidity=0.36(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **13.2** — location=0.00(swing_low), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.24(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

## Forward-outcome experiment (cumulative)

- Pressure setups recorded: **1302** (active: 0, finalized: 1302)

- Valid (FULL) +120s observations: **0** · Partial: **1302** · Unobserved windows (excluded, per §14): **0**
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
