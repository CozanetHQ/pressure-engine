# Pressure Engine — Phase A Diagnostic Report

Generated: **2026-10-02T22:53:51.768272+00:00** · model: **pressure_states_v1** (weights PROVISIONAL EQUAL — not locked, no online learning)

> Shadow-only. No trades. Raw forward-collected telemetry. Numbers without FULL-observation sample sizes are not evidence of edge.

## Runtime coverage (GitHub Actions)

- Runs: **719** · Observed: **43,677.0s** of expected **92,929.0s** → coverage **47.0%**
- Blind gaps recorded: **500**

## Current state by symbol

| Symbol | State | LONG | SHORT | Coverage | OI 1m | CVD 60s | Imb10 | Liquidity | Effort (L/S) | FFP |
|---|---|---|---|---|---|---|---|---|---|---|
| NEAR | NEUTRAL | **15.8** | **23.2** | PARTIAL_TAPE(238) | 15420089 | -563.0 | 0.16 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/UNKNOWN | 0/0 |
| BTC | NEUTRAL | **22.2** | **35.9** | PARTIAL_TAPE(1978) | 32538 | -5.5 | -0.06 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/UNKNOWN | 0/0 |
| ETH | NEUTRAL | **19.1** | **20.4** | PARTIAL_TAPE(953) | 771383 | -85.4 | 0.49 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/UNKNOWN | 0/0 |
| SOL | NEUTRAL | **33.0** | **25.2** | PARTIAL_TAPE(341) | 4045036 | -64.7 | 0.51 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/UNKNOWN | 0/0 |
| XRP | NEUTRAL | **20.5** | **35.1** | PARTIAL_TAPE(300) | 167312282 | -2108.0 | -0.16 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/EXPANSION_ | 0/0 |

Component status per symbol (latest evaluation):

**NEAR**

- LONG: score **15.8** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.40(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **23.2** — location=0.00(NO_LEVEL_NEAR), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.30(FULL), liquidity=0.20(OK), effortresult=0.33(UNKNOWN), forcedflowproxy=0.00(OK)

**BTC**

- LONG: score **22.2** — location=0.52(swing_high), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.27(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **35.9** — location=0.21(swing_low), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.49(FULL), liquidity=0.33(OK), effortresult=0.56(UNKNOWN), forcedflowproxy=0.00(OK)

**ETH**

- LONG: score **19.1** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.60(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **20.4** — location=0.00(NO_LEVEL_NEAR), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.47(FULL), liquidity=0.00(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)

**SOL**

- LONG: score **33.0** — location=0.83(swing_high), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.60(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **25.2** — location=0.00(NO_LEVEL_NEAR), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.32(FULL), liquidity=0.00(OK), effortresult=0.64(UNKNOWN), forcedflowproxy=0.00(OK)

**XRP**

- LONG: score **20.5** — location=0.48(session_high), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.21(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **35.1** — location=0.00(NO_LEVEL_NEAR), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.32(FULL), liquidity=0.39(OK), effortresult=0.84(EXPANSION_CANDIDATE), forcedflowproxy=0.00(OK)

## Forward-outcome experiment (cumulative)

- Pressure setups recorded: **73** (active: 1, finalized: 72)

- Valid (FULL) +120s observations: **0** · Partial: **72** · Unobserved windows (excluded, per §14): **0**
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
