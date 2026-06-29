"""
Mathematische Hilfsfunktionen
für Yasin AI.
"""

from statistics import mean


def round_price(
    value: float,
    decimals: int = 2,
) -> float:
    """Preis runden."""
    return round(value, decimals)


def calculate_percentage(
    value: float,
    total: float,
) -> float:
    """Prozentwert berechnen."""
    if total == 0:
        return 0.0

    return round(
        value / total * 100,
        2,
    )


def calculate_difference(
    first: float,
    second: float,
) -> float:
    """Differenz berechnen."""
    return round(
        second - first,
        2,
    )


def calculate_rr(
    entry: float,
    stop_loss: float,
    take_profit: float,
) -> float:
    """Risk/Reward berechnen."""
    risk = abs(entry - stop_loss)
    reward = abs(take_profit - entry)

    if risk == 0:
        return 0.0

    return round(
        reward / risk,
        2,
    )


def calculate_position_size(
    balance: float,
    risk_percent: float,
    entry: float,
    stop_loss: float,
) -> float:
    """Positionsgröße berechnen."""
    risk_amount = balance * risk_percent / 100
    stop_distance = abs(entry - stop_loss)

    if stop_distance == 0:
        return 0.0

    return round(
        risk_amount / stop_distance,
        4,
    )


def calculate_drawdown(
    equity_curve: list[float],
) -> float:
    """Maximalen Drawdown berechnen."""
    if not equity_curve:
        return 0.0

    peak = equity_curve[0]
    max_dd = 0.0

    for value in equity_curve:
        peak = max(peak, value)

        if peak == 0:
            continue

        drawdown = (
            peak - value
        ) / peak * 100

        max_dd = max(
            max_dd,
            drawdown,
        )

    return round(max_dd, 2)


def average(
    values: list[float],
) -> float:
    """Durchschnitt berechnen."""
    if not values:
        return 0.0

    return round(
        mean(values),
        2,
    )
