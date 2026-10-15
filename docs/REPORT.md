# Pressure Engine — Phase A Diagnostic Report

Generated: **2026-10-15T15:27:18.287637+00:00** · model: **pressure_states_v1** (weights PROVISIONAL EQUAL — not locked, no online learning)

> Shadow-only. No trades. Raw forward-collected telemetry. Numbers without FULL-observation sample sizes are not evidence of edge.

## Runtime coverage (GitHub Actions)

- Runs: **13378** · Observed: **812,241.0s** of expected **1,189,336.0s** → coverage **68.3%**
- Blind gaps recorded: **500**

## Current state by symbol

| Symbol | State | LONG | SHORT | Coverage | OI 1m | CVD 60s | Imb10 | Liquidity | Effort (L/S) | FFP |
|---|---|---|---|---|---|---|---|---|---|---|
| NEAR | SHORT_PRESSURE_BUILDING | **33.7** | **49.4** | PARTIAL_TAPE(5491) | 16306175 | -36878.0 | 0.21 | CONSUMED_WITH_PRINTS | ABSORPTION/UNKNOWN | 0/0 |
| BTC | NEUTRAL | **26.0** | **37.2** | PARTIAL_TAPE(21812) | 35211 | -23.9 | 0.30 | CONSUMED_WITH_PRINTS | UNKNOWN/ABSORPTION | 0/0 |
| ETH | SHORT_PRESSURE_BUILDING | **31.9** | **48.9** | PARTIAL_TAPE(11632) | 798397 | -430.9 | -0.30 | CONSUMED_WITH_PRINTS | UNKNOWN/ABSORPTION | 0/0 |
| SOL | NEUTRAL | **44.0** | **31.0** | PARTIAL_TAPE(4503) | 4058899 | -1299.4 | 0.12 | CONSUMED_WITH_PRINTS | UNKNOWN/ABSORPTION | 0/0 |
| XRP | NEUTRAL | **38.0** | **20.8** | PARTIAL_TAPE(3068) | 173340565 | -108851.0 | 0.21 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/ABSORPTION | 0/0 |

Component status per symbol (latest evaluation):

**NEAR**

- LONG: score **33.7** — location=0.25(session_high), positioning=0.75(COUNTER_POSITIONS_UNWINDING), flow=0.00(PARTIAL_TAPE), liquidity=0.82(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **49.4** — location=0.77(swing_low), positioning=0.35(NO_POSITIONING_INFO), flow=1.00(PARTIAL_TAPE), liquidity=0.58(OK), effortresult=0.27(UNKNOWN), forcedflowproxy=0.00(OK)

**BTC**

- LONG: score **26.0** — location=0.13(session_high), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(PARTIAL_TAPE), liquidity=0.88(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **37.2** — location=0.00(NO_LEVEL_NEAR), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.96(PARTIAL_TAPE), liquidity=0.52(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

**ETH**

- LONG: score **31.9** — location=0.84(swing_high), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(PARTIAL_TAPE), liquidity=0.52(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **48.9** — location=0.61(swing_low), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.69(PARTIAL_TAPE), liquidity=0.88(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

**SOL**

- LONG: score **44.0** — location=0.96(swing_high), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(PARTIAL_TAPE), liquidity=0.77(OK), effortresult=0.56(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **31.0** — location=0.00(NO_LEVEL_NEAR), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.48(PARTIAL_TAPE), liquidity=0.63(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

**XRP**

- LONG: score **38.0** — location=0.66(session_high), positioning=0.75(COUNTER_POSITIONS_UNWINDING), flow=0.00(FULL), liquidity=0.42(OK), effortresult=0.44(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **20.8** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.52(FULL), liquidity=0.18(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

## Forward-outcome experiment (cumulative)

- Pressure setups recorded: **675** (active: 5, finalized: 670)

- Valid (FULL) +120s observations: **0** · Partial: **670** · Unobserved windows (excluded, per §14): **0**
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
