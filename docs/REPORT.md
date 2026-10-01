# Pressure Engine — Phase A Diagnostic Report

Generated: **2026-10-01T21:06:02.684565+00:00** · model: **pressure_states_v1** (weights PROVISIONAL EQUAL — not locked, no online learning)

> Shadow-only. No trades. Raw forward-collected telemetry. Numbers without FULL-observation sample sizes are not evidence of edge.

## Runtime coverage (GitHub Actions)

- Runs: **1** · Observed: **60.0s** of expected **60.0s** → coverage **100.0%**
- Blind gaps recorded: **0**

## Current state by symbol

| Symbol | State | LONG | SHORT | Coverage | OI 1m | CVD 60s | Imb10 | Liquidity | Effort (L/S) | FFP |
|---|---|---|---|---|---|---|---|---|---|---|
| NEAR | NEUTRAL | **21.7** | **26.7** | INSUFFICIENT_OI_HISTORY | 15445464 | 619.0 | -0.52 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/UNKNOWN | 0/0 |
| BTC | NEUTRAL | **33.3** | **28.3** | INSUFFICIENT_OI_HISTORY | 31264 | -2.4 | 0.98 | CONSUMED_WITH_PRINTS | UNKNOWN/UNKNOWN | 0/0 |
| ETH | NEUTRAL | **19.2** | **29.2** | INSUFFICIENT_OI_HISTORY | 737497 | -3.2 | -0.25 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/UNKNOWN | 0/0 |
| SOL | NEUTRAL | **34.3** | **32.8** | INSUFFICIENT_OI_HISTORY | 4072277 | 2159.9 | -0.11 | CONSUMED_WITH_PRINTS | UNKNOWN/UNKNOWN | 0/0 |
| XRP | NEUTRAL | **24.7** | **23.7** | INSUFFICIENT_OI_HISTORY | 172832994 | -12462.0 | 0.30 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/UNKNOWN | 0/0 |

Component status per symbol (latest evaluation):

**NEAR**

- LONG: score **21.7** — location=0.00(NO_LEVEL_NEAR), positioning=0.50(INSUFFICIENT_DATA), flow=0.30(INSUFFICIENT_HISTORY), liquidity=0.00(INSUFFICIENT_HISTORY), effortresult=0.50(INSUFFICIENT_HISTORY), forcedflowproxy=0.00(INSUFFICIENT_DATA)
- SHORT: score **26.7** — location=0.00(NO_LEVEL_NEAR), positioning=0.50(INSUFFICIENT_DATA), flow=0.00(INSUFFICIENT_HISTORY), liquidity=0.60(INSUFFICIENT_HISTORY), effortresult=0.50(INSUFFICIENT_HISTORY), forcedflowproxy=0.00(INSUFFICIENT_DATA)

**BTC**

- LONG: score **33.3** — location=0.00(NO_LEVEL_NEAR), positioning=0.50(INSUFFICIENT_DATA), flow=0.00(INSUFFICIENT_HISTORY), liquidity=1.00(INSUFFICIENT_HISTORY), effortresult=0.50(INSUFFICIENT_HISTORY), forcedflowproxy=0.00(INSUFFICIENT_DATA)
- SHORT: score **28.3** — location=0.00(NO_LEVEL_NEAR), positioning=0.50(INSUFFICIENT_DATA), flow=0.30(INSUFFICIENT_HISTORY), liquidity=0.40(INSUFFICIENT_HISTORY), effortresult=0.50(INSUFFICIENT_HISTORY), forcedflowproxy=0.00(INSUFFICIENT_DATA)

**ETH**

- LONG: score **19.2** — location=0.00(NO_LEVEL_NEAR), positioning=0.50(INSUFFICIENT_DATA), flow=0.00(INSUFFICIENT_HISTORY), liquidity=0.15(INSUFFICIENT_HISTORY), effortresult=0.50(INSUFFICIENT_HISTORY), forcedflowproxy=0.00(INSUFFICIENT_DATA)
- SHORT: score **29.2** — location=0.00(NO_LEVEL_NEAR), positioning=0.50(INSUFFICIENT_DATA), flow=0.30(INSUFFICIENT_HISTORY), liquidity=0.45(INSUFFICIENT_HISTORY), effortresult=0.50(INSUFFICIENT_HISTORY), forcedflowproxy=0.00(INSUFFICIENT_DATA)

**SOL**

- LONG: score **34.3** — location=0.13(swing_high), positioning=0.50(INSUFFICIENT_DATA), flow=0.30(INSUFFICIENT_HISTORY), liquidity=0.63(INSUFFICIENT_HISTORY), effortresult=0.50(INSUFFICIENT_HISTORY), forcedflowproxy=0.00(INSUFFICIENT_DATA)
- SHORT: score **32.8** — location=0.20(swing_low), positioning=0.50(INSUFFICIENT_DATA), flow=0.00(INSUFFICIENT_HISTORY), liquidity=0.77(INSUFFICIENT_HISTORY), effortresult=0.50(INSUFFICIENT_HISTORY), forcedflowproxy=0.00(INSUFFICIENT_DATA)

**XRP**

- LONG: score **24.7** — location=0.00(NO_LEVEL_NEAR), positioning=0.50(INSUFFICIENT_DATA), flow=0.00(INSUFFICIENT_HISTORY), liquidity=0.48(INSUFFICIENT_HISTORY), effortresult=0.50(INSUFFICIENT_HISTORY), forcedflowproxy=0.00(INSUFFICIENT_DATA)
- SHORT: score **23.7** — location=0.00(swing_low), positioning=0.50(INSUFFICIENT_DATA), flow=0.30(INSUFFICIENT_HISTORY), liquidity=0.12(INSUFFICIENT_HISTORY), effortresult=0.50(INSUFFICIENT_HISTORY), forcedflowproxy=0.00(INSUFFICIENT_DATA)

## Forward-outcome experiment (cumulative)

- Pressure setups recorded: **0** (active: 0, finalized: 0)

- Valid (FULL) +120s observations: **0** · Partial: **0** · Unobserved windows (excluded, per §14): **0**
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
