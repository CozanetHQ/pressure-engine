"""Funding — 8h context variable, NEVER a fast cascade signal.

Percentile/z-score computed only once >= 20 settled 8h points exist
(Bitget history-fund-rate provides ~33 days at 100 points). Until then:
INSUFFICIENT_HISTORY. The funding value never enters the fast pressure
score; it is stored as context on every experiment record.
"""
from . import bitget

MIN_FUNDING_POINTS = 20


def refresh(symbol, sym, now_ms):
    cur, err = bitget.fetch_funding_current(symbol)
    if cur is not None:
        sym["funding"]["current"] = cur
        sym["funding"]["fetched_at"] = now_ms
    hist, err2 = bitget.fetch_funding_history(symbol)
    if hist:
        sym["funding"]["history"] = hist[:100]
    _derive(sym)


def _derive(sym):
    f = sym["funding"]
    hist = f["history"]
    if len(hist) >= MIN_FUNDING_POINTS:
        rates = [p["rate"] for p in hist]
        mean = sum(rates) / len(rates)
        var = sum((x - mean) ** 2 for x in rates) / len(rates)
        std = var ** 0.5
        cur = f["current"] if f["current"] is not None else rates[0]
        f["zscore"] = round((cur - mean) / std, 4) if std > 1e-12 else 0.0
        f["percentile"] = round(sum(1 for x in rates if x <= cur) / len(rates), 4)
        f["history_status"] = "OK"
    else:
        f["zscore"] = None
        f["percentile"] = None
        f["history_status"] = "INSUFFICIENT_HISTORY"


def context(sym):
    f = sym["funding"]
    return {
        "current": f["current"],
        "percentile": f["percentile"],
        "zscore": f["zscore"],
        "history_status": f["history_status"],
    }
