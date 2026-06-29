from datetime import datetime


def price(
    value: float,
    digits: int = 2,
) -> str:
    """
    Formatiert einen Preis.
    """

    return f"{value:.{digits}f}"


def percentage(
    value: float,
) -> str:

    return f"{value:.2f}%"


def profit(
    value: float,
    currency: str = "$",
) -> str:

    sign = "+" if value >= 0 else ""

    return (
        f"{sign}{currency}"
        f"{value:.2f}"
    )


def rr(
    value: float,
) -> str:

    return f"{value:.2f}:1"


def timestamp(
    dt: datetime,
) -> str:

    return dt.strftime(
        "%Y-%m-%d %H:%M:%S UTC"
    )


def signal_title(
    market: str,
    direction: str,
) -> str:

    return (
        f"{market.upper()} "
        f"{direction.upper()} SIGNAL"
    )


def telegram_message(
    signal,
) -> str:

    return (
        f"📈 {signal_title(signal.market, signal.direction)}\n\n"
        f"Entry: {price(signal.entry)}\n"
        f"SL: {price(signal.stop_loss)}\n"
        f"TP1: {price(signal.take_profit_1)}\n"
        f"TP2: {price(signal.take_profit_2)}\n"
        f"TP3: {price(signal.take_profit_3)}\n\n"
        f"Quality: {percentage(signal.quality_score)}\n"
        f"RR: {rr(signal.risk_reward_ratio)}"
    )


def dashboard_profit(
    value: float,
) -> str:

    return profit(
        value,
        "$",
    )


def dashboard_winrate(
    value: float,
) -> str:

    return percentage(value)


def dashboard_drawdown(
    value: float,
) -> str:

    return percentage(value)
