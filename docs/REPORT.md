# Pressure Engine — Phase A Diagnostic Report

Generated: **2026-10-08T15:58:52.014266+00:00** · model: **pressure_states_v1** (weights PROVISIONAL EQUAL — not locked, no online learning)

> Shadow-only. No trades. Raw forward-collected telemetry. Numbers without FULL-observation sample sizes are not evidence of edge.

## Runtime coverage (GitHub Actions)

- Runs: **6224** · Observed: **377,520.0s** of expected **586,430.0s** → coverage **64.4%**
- Blind gaps recorded: **500**

## Current state by symbol

| Symbol | State | LONG | SHORT | Coverage | OI 1m | CVD 60s | Imb10 | Liquidity | Effort (L/S) | FFP |
|---|---|---|---|---|---|---|---|---|---|---|
| NEAR | NEUTRAL | **10.9** | **37.6** | PARTIAL_TAPE(2199) | 15596793 | -4254.0 | -0.33 | LIQUIDITY_REMOVAL_UNCERTAIN | ABSORPTION/EXPANSION_ | 0/0 |
| BTC | NEUTRAL | **26.1** | **34.7** | PARTIAL_TAPE | 36821 | -5.1 | -0.14 | CONSUMED_WITH_PRINTS | UNKNOWN/UNKNOWN | 0/0 |
| ETH | NEUTRAL | **9.2** | **34.1** | PARTIAL_TAPE(4804) | 798275 | -32.3 | -0.66 | LIQUIDITY_REMOVAL_UNCERTAIN | ABSORPTION/UNKNOWN | 0/0 |
| SOL | NEUTRAL | **17.5** | **37.6** | PARTIAL_TAPE(1726) | 4245698 | -77.2 | 0.34 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/UNKNOWN | 0/0 |
| XRP | NEUTRAL | **21.9** | **22.3** | PARTIAL_TAPE(1339) | 201037685 | -28922.0 | 0.11 | LIQUIDITY_REMOVAL_UNCERTAIN | ABSORPTION/UNKNOWN | 0/0 |

Component status per symbol (latest evaluation):

**NEAR**

- LONG: score **10.9** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(PARTIAL_TAPE), liquidity=0.10(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **37.6** — location=0.00(session_low), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.42(PARTIAL_TAPE), liquidity=0.50(OK), effortresult=0.79(EXPANSION_CANDIDATE), forcedflowproxy=0.00(OK)

**BTC**

- LONG: score **26.1** — location=0.00(NO_LEVEL_NEAR), positioning=0.75(COUNTER_POSITIONS_UNWINDING), flow=0.00(PARTIAL_TAPE), liquidity=0.61(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **34.7** — location=0.00(session_low), positioning=0.35(NO_POSITIONING_INFO), flow=0.45(PARTIAL_TAPE), liquidity=0.79(OK), effortresult=0.50(UNKNOWN), forcedflowproxy=0.00(OK)

**ETH**

- LONG: score **9.2** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(PARTIAL_TAPE), liquidity=0.00(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **34.1** — location=0.00(session_low), positioning=0.85(PRICE_WITH_DIR_OI_RISING), flow=0.32(PARTIAL_TAPE), liquidity=0.60(OK), effortresult=0.28(UNKNOWN), forcedflowproxy=0.00(OK)

**SOL**

- LONG: score **17.5** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(PARTIAL_TAPE), liquidity=0.50(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **37.6** — location=0.00(NO_LEVEL_NEAR), positioning=0.85(PRICE_WITH_DIR_OI_RISING), flow=0.31(PARTIAL_TAPE), liquidity=0.10(OK), effortresult=1.00(UNKNOWN), forcedflowproxy=0.00(OK)

**XRP**

- LONG: score **21.9** — location=0.00(NO_LEVEL_NEAR), positioning=0.75(COUNTER_POSITIONS_UNWINDING), flow=0.00(PARTIAL_TAPE), liquidity=0.36(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **22.3** — location=0.00(session_low), positioning=0.35(NO_POSITIONING_INFO), flow=0.37(PARTIAL_TAPE), liquidity=0.24(OK), effortresult=0.39(UNKNOWN), forcedflowproxy=0.00(OK)

## Forward-outcome experiment (cumulative)

- Pressure setups recorded: **363** (active: 0, finalized: 363)

- Valid (FULL) +120s observations: **0** · Partial: **363** · Unobserved windows (excluded, per §14): **0**
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
