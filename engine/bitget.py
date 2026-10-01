"""Bitget v2 public REST client — market data only, no auth, no secrets.

Phase A is shadow-only: every endpoint here is PUBLIC. There are no API
keys in this repo by design.

Empirically verified constraints (2026-10-01, see README §3):
  - fills: newest 100 trades only; pagination params are IGNORED by the
    exchange. The tape is forward-collect only.
  - open-interest: current snapshot only. No history endpoint exists.
  - history-fund-rate: exists (8h settlements).
  - merge-depth: returns ~100 levels at step0.
"""
import json
import time
import urllib.request
import urllib.error

API = "https://api.bitget.com/api/v2/mix/market"
PRODUCT = "USDT-FUTURES"


def http_get(url, timeout=8, retries=3):
    last = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={"Content-Type": "application/json"})
            with urllib.request.urlopen(req, timeout=timeout) as res:
                return json.loads(res.read().decode())
        except urllib.error.HTTPError as e:
            # 4xx from Bitget usually carries a JSON body with the real reason
            raw = e.read().decode(errors="replace") if hasattr(e, "read") else ""
            try:
                return json.loads(raw) if raw else {"code": "HTTP%d" % e.code, "msg": str(e)}
            except ValueError:
                return {"code": "HTTP%d" % e.code, "msg": raw or str(e)}
        except Exception as e:  # transient transport fault — retry GETs
            last = e
            time.sleep(0.4 * (2 ** attempt))
    return {"code": "TRANSPORT", "msg": str(last)}


def _ok(data):
    return data.get("code") == "00000"


def fetch_fills(symbol, limit=100):
    """Newest-first executed trades: [{tradeId, price, size, side, ts}]."""
    data = http_get(f"{API}/fills?symbol={symbol}&productType={PRODUCT}&limit={limit}")
    if not _ok(data):
        return None, data.get("msg")
    rows = data.get("data") or []
    out = [{"trade_id": str(r["tradeId"]), "price": float(r["price"]),
            "size": float(r["size"]), "side": r["side"], "ts": int(r["ts"])}
           for r in rows]
    # defensive: force newest-first (highest tradeId first)
    out.sort(key=lambda r: int(r["trade_id"]), reverse=True)
    return out, None


def fetch_depth(symbol):
    """Full merged book. Returns {'bids': [(price, size)...] desc, 'asks': asc}."""
    data = http_get(f"{API}/merge-depth?symbol={symbol}&productType={PRODUCT}&type=step0&limit=100")
    if not _ok(data):
        return None, data.get("msg")
    d = data.get("data") or {}
    bids = sorted(((float(b[0]), float(b[1])) for b in (d.get("bids") or [])),
                  key=lambda x: x[0], reverse=True)
    asks = sorted(((float(a[0]), float(a[1])) for a in (d.get("asks") or [])),
                  key=lambda x: x[0])
    return {"bids": bids, "asks": asks, "ts": int(data.get("requestTime") or 0) or None}, None


def fetch_open_interest(symbol):
    """Current OI in base-coin units: (size, ts) or (None, err)."""
    data = http_get(f"{API}/open-interest?symbol={symbol}&productType={PRODUCT}")
    if not _ok(data):
        return None, data.get("msg")
    lst = (data.get("data") or {}).get("openInterestList") or []
    if not lst:
        return None, "empty oi list"
    return float(lst[0]["size"]), None


def fetch_funding_current(symbol):
    """Current (predicted) funding rate as a fraction, e.g. 0.0001."""
    data = http_get(f"{API}/current-fund-rate?symbol={symbol}&productType={PRODUCT}")
    if not _ok(data) or not data.get("data"):
        return None, data.get("msg")
    d = data["data"][0]
    try:
        return float(d["fundingRate"]), None
    except (TypeError, ValueError):
        return None, "bad funding rate"


def fetch_funding_history(symbol, page_size=100):
    """Past settled funding rates (8h cadence), newest first."""
    data = http_get(f"{API}/history-fund-rate?symbol={symbol}&productType={PRODUCT}&pageSize={page_size}")
    if not _ok(data) or not isinstance(data.get("data"), list):
        return None, data.get("msg")
    out = []
    for d in data["data"]:
        try:
            out.append({"rate": float(d["fundingRate"]), "ts": int(d.get("fundingTime") or d.get("ts") or 0)})
        except (TypeError, ValueError):
            continue
    out.sort(key=lambda x: x["ts"], reverse=True)
    return out, None


def fetch_candles(symbol, granularity, limit):
    """Closed+forming candles, oldest→newest: [{ts, open, high, low, close, vol}]."""
    data = http_get(f"{API}/candles?symbol={symbol}&productType={PRODUCT}"
                    f"&granularity={granularity}&limit={limit}")
    if not _ok(data):
        return None, data.get("msg")
    return [{"ts": int(d[0]), "open": float(d[1]), "high": float(d[2]),
             "low": float(d[3]), "close": float(d[4]), "vol": float(d[5])}
            for d in data["data"]], None
