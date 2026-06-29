"""
Markt-Hilfsfunktionen
für Yasin AI.
"""

SUPPORTED_MARKETS = {
    "GOLD": "Metalle",
    "SILVER": "Metalle",
    "FOREX": "Devisen",
    "NASDAQ": "Indizes",
    "SP500": "Indizes",
    "DAX": "Indizes",
    "BTC": "Kryptowährungen",
    "ETH": "Kryptowährungen",
}


DEFAULT_TIMEFRAMES = {
    "SCALPING": "5m",
    "INTRADAY": "15m",
    "SWING": "4h",
    "POSITION": "1d",
}


def normalize_market(
    market: str,
) -> str:
    """Marktnamen normalisieren."""
    return market.strip().upper()


def normalize_symbol(
    symbol: str,
) -> str:
    """Handelssymbol normalisieren."""
    return symbol.replace(
        "/",
        ""
    ).replace(
        "-",
        ""
    ).upper()


def is_supported_market(
    market: str,
) -> bool:
    """Unterstützten Markt prüfen."""
    return (
        normalize_market(market)
        in SUPPORTED_MARKETS
    )


def get_asset_class(
    market: str,
) -> str:
    """Asset-Klasse zurückgeben."""
    return SUPPORTED_MARKETS.get(
        normalize_market(market),
        "Unbekannt",
    )


def get_default_timeframe(
    trading_style: str,
) -> str:
    """Standard-Timeframe ermitteln."""
    return DEFAULT_TIMEFRAMES.get(
        trading_style.upper(),
        "15m",
    )


def list_supported_markets():
    """Unterstützte Märkte auflisten."""
    return sorted(
        SUPPORTED_MARKETS.keys()
    )


def list_asset_classes():
    """Asset-Klassen auflisten."""
    return sorted(
        set(
            SUPPORTED_MARKETS.values()
        )
    )
