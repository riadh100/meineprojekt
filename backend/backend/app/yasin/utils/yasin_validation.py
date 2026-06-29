"""
Zentrale Validierungsfunktionen
für Yasin AI.
"""

from typing import Any


VALID_MARKETS = {
    "GOLD",
    "FOREX",
    "NASDAQ",
    "SP500",
    "BTC",
}

VALID_TIMEFRAMES = {
    "1m",
    "5m",
    "15m",
    "30m",
    "1h",
    "4h",
    "1d",
}


def validate_market(
    market: str,
) -> bool:
    """Markt validieren."""
    return (
        market.upper()
        in VALID_MARKETS
    )


def validate_symbol(
    symbol: str,
) -> bool:
    """Handelssymbol validieren."""
    return (
        isinstance(symbol, str)
        and len(symbol.strip()) >= 3
    )


def validate_timeframe(
    timeframe: str,
) -> bool:
    """Timeframe validieren."""
    return (
        timeframe
        in VALID_TIMEFRAMES
    )


def validate_price(
    value: float,
) -> bool:
    """Preis validieren."""
    return (
        isinstance(value, (int, float))
        and value > 0
    )


def validate_percentage(
    value: float,
) -> bool:
    """Prozentwert validieren."""
    return (
        isinstance(value, (int, float))
        and 0 <= value <= 100
    )


def validate_risk(
    risk: float,
) -> bool:
    """Risiko validieren."""
    return (
        isinstance(risk, (int, float))
        and 0 < risk <= 10
    )


def validate_signal(
    signal: dict[str, Any],
) -> bool:
    """Trading-Signal validieren."""

    required = [

        "market",

        "symbol",

        "direction",

        "entry",

        "stop_loss",

    ]

    return all(
        key in signal
        for key in required
    )


def validate_direction(
    direction: str,
) -> bool:
    """Handelsrichtung validieren."""
    return direction.upper() in {
        "BUY",
        "SELL",
    }


def validate_email(
    email: str,
) -> bool:
    """E-Mail validieren."""
    return (
        "@" in email
        and "." in email
    )


def validate_not_empty(
    value: str,
) -> bool:
    """Leeren String prüfen."""
    return bool(
        value
        and value.strip()
    )
