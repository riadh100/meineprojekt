import re

from app.yasin.config.yasin_constants import (
    SUPPORTED_MARKETS,
    SUPPORTED_TIMEFRAMES,
    SIGNAL_TYPES,
)


def valid_price(
    price: float,
) -> bool:
    """
    Prüft einen Preis.
    """

    return (
        isinstance(price, (int, float))
        and price > 0
    )


def valid_symbol(
    symbol: str,
) -> bool:
    """
    Prüft ein Handelssymbol.
    """

    return bool(
        re.fullmatch(
            r"[A-Z0-9._-]{2,20}",
            symbol.upper(),
        )
    )


def valid_market(
    market: str,
) -> bool:

    return (
        market.upper()
        in SUPPORTED_MARKETS
    )


def valid_timeframe(
    timeframe: str,
) -> bool:

    return (
        timeframe
        in SUPPORTED_TIMEFRAMES
    )


def valid_direction(
    direction: str,
) -> bool:

    return (
        direction.upper()
        in SIGNAL_TYPES
    )


def valid_percentage(
    value: float,
) -> bool:

    return (
        0 <= value <= 100
    )


def valid_rr(
    rr: float,
) -> bool:

    return rr >= 1.0


def valid_quality(
    quality: float,
) -> bool:

    return (
        0 <= quality <= 100
    )


def valid_confirmation_count(
    confirmations: int,
) -> bool:

    return confirmations >= 0


def valid_stop_loss(
    entry: float,
    stop_loss: float,
    direction: str,
) -> bool:

    direction = direction.upper()

    if direction == "BUY":
        return stop_loss < entry

    return stop_loss > entry


def valid_take_profit(
    entry: float,
    target: float,
    direction: str,
) -> bool:

    direction = direction.upper()

    if direction == "BUY":
        return target > entry

    return target < entry


def valid_signal(
    signal,
) -> bool:

    return (
        valid_market(signal.market)
        and valid_symbol(signal.symbol)
        and valid_direction(
            signal.direction
        )
        and valid_price(signal.entry)
        and valid_price(
            signal.stop_loss
        )
        and valid_quality(
            signal.quality_score
        )
    )
