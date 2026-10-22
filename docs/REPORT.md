# Pressure Engine — Phase A Diagnostic Report

Generated: **2026-10-22T02:13:03.387970+00:00** · model: **pressure_states_v1** (weights PROVISIONAL EQUAL — not locked, no online learning)

> Shadow-only. No trades. Raw forward-collected telemetry. Numbers without FULL-observation sample sizes are not evidence of edge.

## Runtime coverage (GitHub Actions)

- Runs: **19815** · Observed: **1,202,844.0s** of expected **1,746,481.0s** → coverage **68.9%**
- Blind gaps recorded: **500**

## Current state by symbol

| Symbol | State | LONG | SHORT | Coverage | OI 1m | CVD 60s | Imb10 | Liquidity | Effort (L/S) | FFP |
|---|---|---|---|---|---|---|---|---|---|---|
| NEAR | NEUTRAL | **13.5** | **36.9** | PARTIAL_TAPE(7327) | 16616718 | -4346.0 | -0.07 | LIQUIDITY_REMOVAL_UNCERTAIN | ABSORPTION/EXPANSION_ | 0/0 |
| BTC | NEUTRAL | **26.5** | **29.9** | PARTIAL_TAPE(30719) | 35377 | 4.1 | -0.14 | CONSUMED_WITH_PRINTS | ABSORPTION/UNKNOWN | 0/0 |
| ETH | NEUTRAL | **36.6** | **20.6** | PARTIAL_TAPE(19099) | 751800 | 41.3 | 0.36 | CONSUMED_WITH_PRINTS | ABSORPTION/ABSORPTION | 0/0 |
| SOL | NEUTRAL | **23.8** | **31.6** | PARTIAL_TAPE(6505) | 4039421 | -67.2 | 0.19 | LIQUIDITY_REMOVAL_UNCERTAIN | ABSORPTION/UNKNOWN | 0/0 |
| XRP | NEUTRAL | **36.8** | **32.6** | PARTIAL_TAPE(4218) | 181306882 | 5760.0 | -0.03 | CONSUMED_WITH_PRINTS | ABSORPTION/UNKNOWN | 0/0 |

Component status per symbol (latest evaluation):

**NEAR**

- LONG: score **13.5** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(FULL), liquidity=0.26(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **36.9** — location=0.00(NO_LEVEL_NEAR), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.41(FULL), liquidity=0.34(OK), effortresult=0.91(EXPANSION_CANDIDATE), forcedflowproxy=0.00(OK)

**BTC**

- LONG: score **26.5** — location=0.00(NO_LEVEL_NEAR), positioning=0.35(NO_POSITIONING_INFO), flow=0.42(PARTIAL_TAPE), liquidity=0.62(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **29.9** — location=0.04(session_low), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.00(PARTIAL_TAPE), liquidity=0.78(OK), effortresult=0.42(UNKNOWN), forcedflowproxy=0.00(OK)

**ETH**

- LONG: score **36.6** — location=0.35(swing_high), positioning=0.35(NO_POSITIONING_INFO), flow=0.38(PARTIAL_TAPE), liquidity=0.91(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **20.6** — location=0.00(swing_low), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.00(PARTIAL_TAPE), liquidity=0.49(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)

**SOL**

- LONG: score **23.8** — location=0.46(swing_high), positioning=0.35(NO_POSITIONING_INFO), flow=0.00(PARTIAL_TAPE), liquidity=0.41(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **31.6** — location=0.45(swing_low), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.31(PARTIAL_TAPE), liquidity=0.19(OK), effortresult=0.40(UNKNOWN), forcedflowproxy=0.00(OK)

**XRP**

- LONG: score **36.8** — location=0.64(swing_high), positioning=0.35(NO_POSITIONING_INFO), flow=0.34(FULL), liquidity=0.68(OK), effortresult=0.20(ABSORPTION_CANDIDATE), forcedflowproxy=0.00(OK)
- SHORT: score **32.6** — location=0.00(session_low), positioning=0.55(PRICE_WITH_DIR_OI_FLAT), flow=0.00(FULL), liquidity=0.72(OK), effortresult=0.68(UNKNOWN), forcedflowproxy=0.00(OK)

## Forward-outcome experiment (cumulative)

- Pressure setups recorded: **931** (active: 0, finalized: 931)

- Valid (FULL) +120s observations: **0** · Partial: **931** · Unobserved windows (excluded, per §14): **0**
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
