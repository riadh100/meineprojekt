from statistics import mean


def win_rate(
    wins: int,
    total: int,
) -> float:
    """
    Berechnet die Gewinnquote.
    """

    if total == 0:
        return 0.0

    return round(
        wins / total * 100,
        2,
    )


def loss_rate(
    losses: int,
    total: int,
) -> float:

    if total == 0:
        return 0.0

    return round(
        losses / total * 100,
        2,
    )


def profit_factor(
    gross_profit: float,
    gross_loss: float,
) -> float:

    if gross_loss == 0:

        if gross_profit > 0:
            return float("inf")

        return 0.0

    return round(
        gross_profit / abs(gross_loss),
        2,
    )


def expectancy(
    average_win: float,
    average_loss: float,
    winrate: float,
) -> float:

    return round(
        (
            average_win
            * (winrate / 100)
        )
        -
        (
            average_loss
            * (1 - (winrate / 100))
        ),
        2,
    )


def average_rr(
    values: list[float],
) -> float:

    if not values:
        return 0.0

    return round(
        mean(values),
        2,
    )


def max_drawdown(
    equity_curve: list[float],
) -> float:

    if not equity_curve:
        return 0.0

    peak = equity_curve[0]

    max_dd = 0.0

    for value in equity_curve:

        if value > peak:
            peak = value

        drawdown = (
            peak - value
        ) / peak * 100

        if drawdown > max_dd:
            max_dd = drawdown

    return round(
        max_dd,
        2,
    )


def net_profit(
    gross_profit: float,
    gross_loss: float,
) -> float:

    return round(
        gross_profit - abs(gross_loss),
        2,
    )


def profit_percent(
    initial_balance: float,
    current_balance: float,
) -> float:

    if initial_balance == 0:
        return 0.0

    return round(
        (
            current_balance
            - initial_balance
        )
        / initial_balance
        * 100,
        2,
    )
