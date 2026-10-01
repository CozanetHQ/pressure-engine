"""Pressure states + two independent 0-100 scores.

The states distinguish pressure BUILDING from pressure RELEASED:

  NEUTRAL
  LONG_PRESSURE_BUILDING / SHORT_PRESSURE_BUILDING
  LONG_PRESSURE_CONFIRMED / SHORT_PRESSURE_CONFIRMED
  FORCED_FLOW_PROXY_LONG / FORCED_FLOW_PROXY_SHORT
  EXPANSION_LONG / EXPANSION_SHORT
  EXHAUSTION_LONG / EXHAUSTION_SHORT
  PRESSURE_FAILED

There is NO liquidation feed on Bitget. Cascade-shaped evidence is labeled
FORCED_FLOW_PROXY — never "liquidations confirmed" (README §3).

Scores: 6 components, each normalized 0-1 first, then combined with
PROVISIONAL EQUAL WEIGHT (mean x 100). Weights are NOT locked — they will
be derived offline from the forward dataset later (README §17). Funding
is context, never a component (README §7).

All thresholds are pressure_states_v1 — a priori, versioned, changed only
offline with a version bump.
"""
STATE_VERSION = "pressure_states_v1"

BUILDING_MIN_LOCATION = 0.5
BUILDING_MIN_FLOW = 0.6
CONFIRMED_MIN_EFFORT = 0.5
CONFIRMED_MIN_BOOK = -0.1     # imb_10 must not be strongly against the direction
BUILDING_VALIDITY_SEC = 120   # re-confirm window before PRESSURE_FAILED
FFP_DISPLACEMENT_ATR = 1.5    # 60s displacement >= 1.5 x ATR14(1m)
FFP_OI_DECLINE_PCT = 0.3      # 60s OI decline >= 0.3%
FFP_FLOW_Z = 2.0              # 60s delta z >= 2.0 (signed)

COMPONENTS = ("location", "positioning", "flow", "liquidity", "effortresult", "forcedflowproxy")

LONG_STATES = ("LONG_PRESSURE_BUILDING", "LONG_PRESSURE_CONFIRMED",
               "FORCED_FLOW_PROXY_LONG", "EXPANSION_LONG", "EXHAUSTION_LONG")
SHORT_STATES = ("SHORT_PRESSURE_BUILDING", "SHORT_PRESSURE_CONFIRMED",
                "FORCED_FLOW_PROXY_SHORT", "EXPANSION_SHORT", "EXHAUSTION_SHORT")
ACTIVE_STATES = LONG_STATES + SHORT_STATES


def _clamp01(x):
    return max(0.0, min(1.0, x))


def flow_component(delta_z_dir, cvd_delta_dir):
    """0..1 — unusual directional aggressive flow.
    0.7 * clamp(z / 2.5) + 0.3 * cvd rising in direction."""
    z = delta_z_dir if delta_z_dir is not None else 0.0
    base = _clamp01(max(0.0, z) / 2.5)
    rising = 1.0 if cvd_delta_dir > 0 else 0.0
    return round(0.7 * base + 0.3 * rising, 4)


def forced_flow_proxy(direction, disp_60_atr, oi_state, delta_z):
    """The 3-condition proxy (ALL must hold):
    rapid displacement + rapid OI decline + strong directional aggressive flow.
    Evidence consistent with forced position reduction — NOT liquidation data."""
    if oi_state is None or oi_state.get("change_pct_1m") is None:
        return 0.0, "INSUFFICIENT_DATA"
    with_dir = disp_60_atr if direction == "long" else -disp_60_atr
    cond_disp = with_dir >= FFP_DISPLACEMENT_ATR
    cond_oi = oi_state["change_pct_1m"] <= -FFP_OI_DECLINE_PCT
    z = delta_z if delta_z is not None else 0.0
    cond_flow = (z >= FFP_FLOW_Z) if direction == "long" else (z <= -FFP_FLOW_Z)
    if cond_disp and cond_oi and cond_flow:
        return 1.0, "FORCED_FLOW_PROXY_CONDITIONS_MET"
    return 0.0, "OK"


def build_snapshot(sym, now_ms, price, ctx):
    """ctx keys: delta_z, cvd_60, disp_60_atr, price_slope_60, oi_state,
    effort_state, quality_flags. Returns the full component snapshot."""
    from . import oi as OI
    from . import book as BOOK
    from . import location as LOC
    from . import effort as EFF

    imb = sym["book"]["last"]["imb_10"] if sym["book"]["last"] else 0.0
    comp = {"long": {}, "short": {}}
    for d in ("long", "short"):
        # location
        v, s = LOC.location_component(sym, price, d)
        comp[d]["location"] = {"value": v, "status": s}
        # positioning — price slope +1 = moving WITH this direction
        slope = 1 if (ctx["price_slope_60"] > 0) == (d == "long") else -1
        v, s = OI.positioning_component(ctx["oi_state"], slope)
        comp[d]["positioning"] = {"value": v, "status": s}
        # flow
        dz = ctx["delta_z"]
        dz_dir = dz if d == "long" else (-dz if dz is not None else None)
        cvd_dir = ctx["cvd_60"] if d == "long" else -ctx["cvd_60"]
        comp[d]["flow"] = {"value": flow_component(dz_dir, cvd_dir),
                           "status": ctx["flow_status"]}
        # liquidity
        v, s = BOOK.liquidity_component(sym["book"], d, now_ms)
        comp[d]["liquidity"] = {"value": v, "status": s}
        # effort vs result
        v, s = EFF.effort_component(ctx["effort_state"], d)
        comp[d]["effortresult"] = {"value": v, "status": s}
        # forced flow proxy
        v, s = forced_flow_proxy(d, ctx["disp_60_atr"], ctx["oi_state"], ctx["delta_z"])
        comp[d]["forcedflowproxy"] = {"value": v, "status": s}
        # provisional equal-weight score (weights NOT locked — README §12/§17)
        score = sum(comp[d][k]["value"] for k in COMPONENTS)
        comp[d]["score"] = round(100.0 * score / len(COMPONENTS), 1)
        comp[d]["weights"] = "PROVISIONAL_EQUAL_WEIGHT"
    comp["data_coverage"] = ctx["quality_flags"]
    comp["atr_1m"] = sym["location"]["atr_1m"]
    comp["price"] = price
    comp["state_version"] = STATE_VERSION
    comp["effort_state_long"] = ctx["effort_state"].get("interpretation_long", "UNKNOWN")
    comp["effort_state_short"] = ctx["effort_state"].get("interpretation_short", "UNKNOWN")
    return comp


def _conditions_hold(c):
    """Do the minimal conditions that keep an active state alive still hold?"""
    return c["location"]["value"] >= BUILDING_MIN_LOCATION and c["flow"]["value"] >= BUILDING_MIN_FLOW


def evaluate_state(sym, comp, now_ms):
    """Advance the state machine. Returns (new_state, transition_or_None)."""
    p = sym["pressure"]
    old = p["state"]
    L, S = comp["long"], comp["short"]
    imb = sym["book"]["last"]["imb_10"] if sym["book"]["last"] else 0.0

    new, reason = old, None

    # 1. EXHAUSTION — in an active state, directional effort is being absorbed
    if old in ("LONG_PRESSURE_CONFIRMED", "FORCED_FLOW_PROXY_LONG", "EXPANSION_LONG") \
            and comp["effort_state_long"] == "ABSORPTION_CANDIDATE":
        new, reason = "EXHAUSTION_LONG", "high buy effort absorbed (effort-vs-result)"
    elif old in ("SHORT_PRESSURE_CONFIRMED", "FORCED_FLOW_PROXY_SHORT", "EXPANSION_SHORT") \
            and comp["effort_state_short"] == "ABSORPTION_CANDIDATE":
        new, reason = "EXHAUSTION_SHORT", "high sell effort absorbed (effort-vs-result)"

    # 2. FORCED FLOW PROXY — cascade-shaped evidence (displacement+OI drop+flow)
    if new == old and old in ("NEUTRAL", "LONG_PRESSURE_BUILDING", "LONG_PRESSURE_CONFIRMED") \
            and L["forcedflowproxy"]["value"] >= 1.0:
        new, reason = "FORCED_FLOW_PROXY_LONG", "displacement + OI decline + directional flow proxy"
    if new == old and old in ("NEUTRAL", "SHORT_PRESSURE_BUILDING", "SHORT_PRESSURE_CONFIRMED") \
            and S["forcedflowproxy"]["value"] >= 1.0:
        new, reason = "FORCED_FLOW_PROXY_SHORT", "displacement + OI decline + directional flow proxy"

    # 3. EXPANSION — confirmed/forced-flow and flow is moving price efficiently
    if new == old and old in ("LONG_PRESSURE_CONFIRMED", "FORCED_FLOW_PROXY_LONG") \
            and comp["effort_state_long"] == "EXPANSION_CANDIDATE":
        new, reason = "EXPANSION_LONG", "flow moving price efficiently"
    if new == old and old in ("SHORT_PRESSURE_CONFIRMED", "FORCED_FLOW_PROXY_SHORT") \
            and comp["effort_state_short"] == "EXPANSION_CANDIDATE":
        new, reason = "EXPANSION_SHORT", "flow moving price efficiently"

    # 4. CONFIRMED — building conditions + price responds + book not against
    if new == old and L["location"]["value"] >= BUILDING_MIN_LOCATION \
            and L["flow"]["value"] >= BUILDING_MIN_FLOW \
            and L["effortresult"]["value"] >= CONFIRMED_MIN_EFFORT \
            and imb >= CONFIRMED_MIN_BOOK:
        new, reason = "LONG_PRESSURE_CONFIRMED", "location + flow + price response + book"
    if new == old and S["location"]["value"] >= BUILDING_MIN_LOCATION \
            and S["flow"]["value"] >= BUILDING_MIN_FLOW \
            and S["effortresult"]["value"] >= CONFIRMED_MIN_EFFORT \
            and imb <= -CONFIRMED_MIN_BOOK:
        new, reason = "SHORT_PRESSURE_CONFIRMED", "location + flow + price response + book"

    # 5. BUILDING
    if new == old and L["location"]["value"] >= BUILDING_MIN_LOCATION \
            and L["flow"]["value"] >= BUILDING_MIN_FLOW:
        new, reason = "LONG_PRESSURE_BUILDING", "location + flow building"
    if new == old and S["location"]["value"] >= BUILDING_MIN_LOCATION \
            and S["flow"]["value"] >= BUILDING_MIN_FLOW:
        new, reason = "SHORT_PRESSURE_BUILDING", "location + flow building"

    # 6. decay — active state whose conditions fell away past the validity window
    if new == old and old in ACTIVE_STATES:
        c = L if old in LONG_STATES else S
        if old.startswith("FORCED_FLOW_PROXY"):
            holds = c["forcedflowproxy"]["value"] >= 1.0
        else:
            holds = _conditions_hold(c)
        if holds:
            p["last_met_ts"] = now_ms
        else:
            last = p.get("last_met_ts") or p.get("since_ts") or now_ms
            if now_ms - last > BUILDING_VALIDITY_SEC * 1000:
                new, reason = "PRESSURE_FAILED", "conditions decayed past validity window"

    # 7. clear to NEUTRAL
    if new == old and old in ("EXHAUSTION_LONG", "EXHAUSTION_SHORT", "PRESSURE_FAILED") \
            and L["flow"]["value"] < BUILDING_MIN_FLOW and S["flow"]["value"] < BUILDING_MIN_FLOW:
        new, reason = "NEUTRAL", "pressure cleared"

    transition = None
    if new != old:
        transition = {"ts": now_ms, "from": old, "to": new, "reason": reason}
        p["transitions"].append(transition)
        if len(p["transitions"]) > 500:
            del p["transitions"][: len(p["transitions"]) - 500]
        p["state"] = new
        p["since_ts"] = now_ms
        p["last_met_ts"] = now_ms
        p["states_seen"][old] = p["states_seen"].get(old, 0) + 1
    p["states_seen"][new] = p["states_seen"].get(new, 0) + 1
    p["evaluations"] += 1
    p["last_scores"] = comp
    return new, transition
