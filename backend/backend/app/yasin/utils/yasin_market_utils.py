from app.yasin.config.yasin_constants import (
    MARKET_GOLD,
    MARKET_NAS100,
    MARKET_FOREX,
    MARKET_CRYPTO,
)


def normalize_price(
    price: float,
    digits: int = 5,
) -> float:
    """
    Rundet Preise auf die gewünschte Genauigkeit.
    """
    return round(price, digits)


def pip_size(
    market: str,
) -> float:
    """
    Liefert die Pip-/Tickgröße.
    """

    market = market.upper()

    if market == MARKET_GOLD:
        return 0.01

    if market == MARKET_NAS100:
        return 1.0

    if market == MARKET_CRYPTO:
        return 0.01

    return 0.0001


def point_value(
    market: str,
) -> float:
    """
    Standard Point Value.
    """

    market = market.upper()

    if market == MARKET_NAS100:
        return 1.0

    return pip_size(market)


def spread(
    bid: float,
    ask: float,
) -> float:

    return abs(ask - bid)


def spread_in_pips(
    bid: float,
    ask: float,
    market: str,
) -> float:

    return (
        spread(bid, ask)
        / pip_size(market)
    )


def price_distance(
    price1: float,
    price2: float,
) -> float:

    return abs(price1 - price2)


def volatility_level(
    atr: float,
):

    if atr < 0.5:
        return "LOW"

    if atr < 2:
        return "MEDIUM"

    return "HIGH"


def market_name(
    market: str,
):

    names = {
        MARKET_GOLD: "Gold",
        MARKET_NAS100: "NAS100",
        MARKET_FOREX: "Forex",
        MARKET_CRYPTO: "Crypto",
    }

    return names.get(
        market.upper(),
        market,
    )


def valid_price(
    price: float,
):

    return price > 0
