# Pressure Engine — Phase A Diagnostic Report

Generated: **2026-10-28T19:32:19.057345+00:00** · model: **pressure_states_v1** (weights PROVISIONAL EQUAL — not locked, no online learning)

> Shadow-only. No trades. Raw forward-collected telemetry. Numbers without FULL-observation sample sizes are not evidence of edge.

## Runtime coverage (GitHub Actions)

- Runs: **26414** · Observed: **1,602,992.0s** of expected **2,327,236.0s** → coverage **68.9%**
- Blind gaps recorded: **500**

## Current state by symbol

| Symbol | State | LONG | SHORT | Coverage | OI 1m | CVD 60s | Imb10 | Liquidity | Effort (L/S) | FFP |
|---|---|---|---|---|---|---|---|---|---|---|
| NEAR | NEUTRAL | **34.5** | **11.8** | PARTIAL_TAPE(8561) | 16445887 | 5305.0 | 0.24 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/UNKNOWN | 0/0 |
| BTC | NEUTRAL | **29.5** | **19.2** | PARTIAL_TAPE(41179) | 36972 | 5.4 | -0.65 | LIQUIDITY_REMOVAL_UNCERTAIN | UNKNOWN/UNKNOWN | 0/0 |
| ETH | NEUTRAL | **28.4** | **28.2** | PARTIAL_TAPE(28930) | 770299 | 239.2 | 0.09 | LIQUIDITY_REMOVAL_UNCERTAIN | ABSORPTION/ABSORPTION | 0/0 |
| SOL | NEUTRAL | **41.3** | **11.0** | PARTIAL_TAPE(8056) | 4250791 | 477.4 | 0.32 | LIQUIDITY_REMOVAL_UNCERTAIN | ABSORPTION/UNKNOWN | 0/0 |
| XRP | NEUTRAL | **36.3** | **25.0** | PARTIAL_TAPE(5103) | 184636170 | 163658.0 | -0.30 | LIQUIDITY_REMOVAL_UNCERTAIN | ABSORPTION/UNKNOWN | 0/0 |

Component status per symbol (latest evaluation):

**NEAR**

- LONG: score **34.5** — location=0.27(swing_high), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.55(FULL), liquidity=0.44(OK), effortresult=0.26(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **11.8** — location=0.00(swing_low), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.16(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)

**BTC**

- LONG: score **29.5** — location=0.55(swing_high), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.44(PARTIAL_TAPE), liquidity=0.00(OK), effortresult=0.22(UNKNOWN), forcedflowproxy=0.00(OK)
- SHORT: score **19.2** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(PARTIAL_TAPE), liquidity=0.60(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)

**ETH**

- LONG: score **28.4** — location=0.00(NO_LEVEL_NEAR), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.60(PARTIAL_TAPE), liquidity=0.35(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **28.2** — location=0.89(swing_low), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(PARTIAL_TAPE), liquidity=0.25(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

**SOL**

- LONG: score **41.3** — location=0.82(swing_high), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.42(FULL), liquidity=0.49(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **11.0** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.11(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)

**XRP**

- LONG: score **36.3** — location=0.40(swing_high), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.91(FULL), liquidity=0.12(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **25.0** — location=0.47(swing_low), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.48(OK), effortresult=0.20(UNKNOWN), forcedflowproxy=0.00(OK)

## Forward-outcome experiment (cumulative)

- Pressure setups recorded: **1159** (active: 3, finalized: 1156)

- Valid (FULL) +120s observations: **0** · Partial: **1156** · Unobserved windows (excluded, per §14): **0**
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
