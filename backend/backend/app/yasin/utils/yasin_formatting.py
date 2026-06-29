"""
Formatierungsfunktionen
für Yasin AI.
"""

from datetime import datetime


def format_price(
    value: float,
    decimals: int = 2,
) -> str:
    """Preis formatieren."""
    return f"{value:.{decimals}f}"


def format_percent(
    value: float,
    decimals: int = 2,
) -> str:
    """Prozent formatieren."""
    return f"{value:.{decimals}f}%"


def format_currency(
    value: float,
    currency: str = "USD",
) -> str:
    """Währungswert formatieren."""
    return f"{value:,.2f} {currency}"


def format_volume(
    value: float,
) -> str:
    """Volumen formatieren."""

    if value >= 1_000_000:

        return f"{value / 1_000_000:.2f}M"

    if value >= 1_000:

        return f"{value / 1_000:.2f}K"

    return str(value)


def format_datetime(
    value: datetime,
    fmt: str = "%Y-%m-%d %H:%M:%S",
) -> str:
    """Datum/Zeit formatieren."""
    return value.strftime(fmt)


def format_duration(
    seconds: int,
) -> str:
    """Laufzeit formatieren."""

    hours = seconds // 3600

    minutes = (
        seconds % 3600
    ) // 60

    remaining = seconds % 60

    return (
        f"{hours:02d}:"
        f"{minutes:02d}:"
        f"{remaining:02d}"
    )


def format_trade_direction(
    direction: str,
) -> str:
    """Handelsrichtung formatieren."""
    return direction.upper()


def format_rr(
    value: float,
) -> str:
    """Risk/Reward formatieren."""
    return f"1:{value:.2f}"


def format_market(
    market: str,
) -> str:
    """Marktname formatieren."""
    return market.upper()


def format_symbol(
    symbol: str,
) -> str:
    """Symbol formatieren."""
    return symbol.upper()
