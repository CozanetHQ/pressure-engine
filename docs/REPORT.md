# Pressure Engine — Phase A Diagnostic Report

Generated: **2026-10-20T13:58:29.020217+00:00** · model: **pressure_states_v1** (weights PROVISIONAL EQUAL — not locked, no online learning)

> Shadow-only. No trades. Raw forward-collected telemetry. Numbers without FULL-observation sample sizes are not evidence of edge.

## Runtime coverage (GitHub Actions)

- Runs: **18308** · Observed: **1,111,359.0s** of expected **1,616,006.0s** → coverage **68.8%**
- Blind gaps recorded: **500**

## Current state by symbol

| Symbol | State | LONG | SHORT | Coverage | OI 1m | CVD 60s | Imb10 | Liquidity | Effort (L/S) | FFP |
|---|---|---|---|---|---|---|---|---|---|---|
| NEAR | LONG_PRESSURE_BUILDING | **61.1** | **16.2** | PARTIAL_TAPE(6745) | 16603571 | 15601.0 | 0.47 | CONSUMED_WITH_PRINTS | UNKNOWN/ABSORPTION | 0/0 |
| BTC | PRESSURE_FAILED | **52.4** | **22.4** | PARTIAL_TAPE | 35657 | 22.6 | -0.16 | CONSUMED_WITH_PRINTS | EXPANSION_/ABSORPTION | 0/0 |
| ETH | LONG_PRESSURE_CONFIRMED | **68.9** | **29.5** | PARTIAL_TAPE | 771547 | 357.9 | 0.45 | CONSUMED_WITH_PRINTS | EXPANSION_/ABSORPTION | 0/0 |
| SOL | LONG_PRESSURE_BUILDING | **53.5** | **22.9** | PARTIAL_TAPE | 4043421 | 1809.2 | 0.08 | CONSUMED_WITH_PRINTS | ABSORPTION/ABSORPTION | 0/0 |
| XRP | LONG_PRESSURE_BUILDING | **38.2** | **18.4** | PARTIAL_TAPE(3803) | 181215631 | 34740.0 | -0.42 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/ABSORPTION | 0/0 |

Component status per symbol (latest evaluation):

**NEAR**

- LONG: score **61.1** — location=0.81(swing_high), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.93(FULL), liquidity=0.98(OK), effortresult=0.40(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **16.2** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.42(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

**BTC**

- LONG: score **52.4** — location=0.24(session_high), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.99(PARTIAL_TAPE), liquidity=0.61(OK), effortresult=0.76(EXPANSION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **22.4** — location=0.00(swing_low), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(PARTIAL_TAPE), liquidity=0.79(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

**ETH**

- LONG: score **68.9** — location=0.91(swing_high), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.70(PARTIAL_TAPE), liquidity=0.97(OK), effortresult=1.00(EXPANSION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **29.5** — location=0.79(swing_low), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(PARTIAL_TAPE), liquidity=0.43(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

**SOL**

- LONG: score **53.5** — location=0.83(swing_high), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.89(PARTIAL_TAPE), liquidity=0.75(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **22.9** — location=0.17(swing_low), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(PARTIAL_TAPE), liquidity=0.65(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

**XRP**

- LONG: score **38.2** — location=0.94(swing_high), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.41(FULL), liquidity=0.05(OK), effortresult=0.34(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **18.4** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.55(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

## Forward-outcome experiment (cumulative)

- Pressure setups recorded: **874** (active: 3, finalized: 871)

- Valid (FULL) +120s observations: **0** · Partial: **871** · Unobserved windows (excluded, per §14): **0**
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
