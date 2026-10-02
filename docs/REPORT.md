# Pressure Engine — Phase A Diagnostic Report

Generated: **2026-10-02T14:28:08.803184+00:00** · model: **pressure_states_v1** (weights PROVISIONAL EQUAL — not locked, no online learning)

> Shadow-only. No trades. Raw forward-collected telemetry. Numbers without FULL-observation sample sizes are not evidence of edge.

## Runtime coverage (GitHub Actions)

- Runs: **336** · Observed: **20,388.0s** of expected **62,586.0s** → coverage **32.6%**
- Blind gaps recorded: **335**

## Current state by symbol

| Symbol | State | LONG | SHORT | Coverage | OI 1m | CVD 60s | Imb10 | Liquidity | Effort (L/S) | FFP |
|---|---|---|---|---|---|---|---|---|---|---|
| NEAR | NEUTRAL | **27.4** | **19.9** | PARTIAL_TAPE(106) | 15338716 | -5083.0 | 0.58 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/ABSORPTION | 0/0 |
| BTC | SHORT_PRESSURE_BUILDING | **15.8** | **52.9** | PARTIAL_TAPE | 32411 | -17.9 | -0.93 | LIQUIDITY_REMOVAL_UNCERTAIN | ABSORPTION/UNKNOWN | 0/0 |
| ETH | NEUTRAL | **39.5** | **33.3** | PARTIAL_TAPE(483) | 740754 | 362.0 | 0.71 | CONSUMED_WITH_PRINTS | ABSORPTION/EXPANSION_ | 0/0 |
| SOL | NEUTRAL | **32.5** | **34.7** | PARTIAL_TAPE(167) | 3950673 | -810.8 | 0.86 | CONSUMED_WITH_PRINTS | UNKNOWN/UNKNOWN | 0/0 |
| XRP | NEUTRAL | **15.0** | **37.3** | PARTIAL_TAPE(147) | 172996346 | -70431.0 | 0.08 | LIQUIDITY_REMOVAL_UNCERTAIN | ABSORPTION/UNKNOWN | 0/0 |

Component status per symbol (latest evaluation):

**NEAR**

- LONG: score **27.4** — location=0.49(swing_high), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.60(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **19.9** — location=0.00(swing_low), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.44(FULL), liquidity=0.00(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

**BTC**

- LONG: score **15.8** — location=0.00(NO_LEVEL_NEAR), positioning=0.75(COUNTER_POSITIONS_UNWINDING), flow=0.00(PARTIAL_TAPE), liquidity=0.00(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **52.9** — location=0.87(swing_low), positioning=0.35(NO_POSITIONING_INFO), flow=0.87(PARTIAL_TAPE), liquidity=0.60(OK), effortresult=0.48(UNKNOWN), forcedflowproxy=0.00(OK)

**ETH**

- LONG: score **39.5** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.82(PARTIAL_TAPE), liquidity=1.00(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **33.3** — location=0.05(session_low), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.00(PARTIAL_TAPE), liquidity=0.40(OK), effortresult=1.00(EXPANSION_CANDIDATE), forcedflowproxy=0.00(OK)

**SOL**

- LONG: score **32.5** — location=0.40(swing_high), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=1.00(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **34.7** — location=0.00(NO_LEVEL_NEAR), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.52(FULL), liquidity=0.40(OK), effortresult=0.61(UNKNOWN), forcedflowproxy=0.00(OK)

**XRP**

- LONG: score **15.0** — location=0.00(swing_high), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(PARTIAL_TAPE), liquidity=0.35(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **37.3** — location=0.00(swing_low), positioning=0.85(PRICE_WITH_DIR_OI_RISING), flow=0.63(PARTIAL_TAPE), liquidity=0.25(OK), effortresult=0.50(UNKNOWN), forcedflowproxy=0.00(OK)

## Forward-outcome experiment (cumulative)

- Pressure setups recorded: **32** (active: 2, finalized: 30)

- Valid (FULL) +120s observations: **0** · Partial: **30** · Unobserved windows (excluded, per §14): **0**
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
