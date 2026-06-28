from dataclasses import dataclass


@dataclass
class MarketConfig:
    """
    Konfiguration eines unterstützten Marktes.
    """

    name: str
    symbol: str
    timeframe: str

    enabled: bool

    risk_percent: float

    minimum_quality: float

    minimum_rr: float

    strategy: str


MARKETS = {

    "GOLD": MarketConfig(
        name="Gold",
        symbol="XAUUSD",
        timeframe="15m",
        enabled=True,
        risk_percent=1.0,
        minimum_quality=90.0,
        minimum_rr=2.5,
        strategy="GoldStrategy",
    ),

    "NAS100": MarketConfig(
        name="NAS100",
        symbol="NAS100",
        timeframe="15m",
        enabled=True,
        risk_percent=1.0,
        minimum_quality=88.0,
        minimum_rr=2.3,
        strategy="Nas100Strategy",
    ),

    "FOREX": MarketConfig(
        name="Forex",
        symbol="EURUSD",
        timeframe="15m",
        enabled=True,
        risk_percent=1.0,
        minimum_quality=85.0,
        minimum_rr=2.0,
        strategy="ForexStrategy",
    ),

    "CRYPTO": MarketConfig(
        name="Crypto",
        symbol="BTCUSDT",
        timeframe="15m",
        enabled=True,
        risk_percent=1.0,
        minimum_quality=86.0,
        minimum_rr=2.2,
        strategy="CryptoStrategy",
    ),

    "CUSTOM_1": MarketConfig(
        name="Custom Slot 1",
        symbol="",
        timeframe="15m",
        enabled=True,
        risk_percent=1.0,
        minimum_quality=85.0,
        minimum_rr=2.0,
        strategy="CustomStrategy",
    ),

    "CUSTOM_2": MarketConfig(
        name="Custom Slot 2",
        symbol="",
        timeframe="15m",
        enabled=True,
        risk_percent=1.0,
        minimum_quality=85.0,
        minimum_rr=2.0,
        strategy="CustomStrategy",
    ),

    "CUSTOM_3": MarketConfig(
        name="Custom Slot 3",
        symbol="",
        timeframe="15m",
        enabled=True,
        risk_percent=1.0,
        minimum_quality=85.0,
        minimum_rr=2.0,
        strategy="CustomStrategy",
    ),

    "CUSTOM_4": MarketConfig(
        name="Custom Slot 4",
        symbol="",
        timeframe="15m",
        enabled=True,
        risk_percent=1.0,
        minimum_quality=85.0,
        minimum_rr=2.0,
        strategy="CustomStrategy",
    ),
}


def get_market(
    market: str,
) -> MarketConfig:

    return MARKETS[market.upper()]


def all_markets():

    return list(
        MARKETS.values()
    )


def enabled_markets():

    return [
        market
        for market in MARKETS.values()
        if market.enabled
    ]
