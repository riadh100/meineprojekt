from math import sqrt
from statistics import mean


def round_to(
    value: float,
    digits: int = 2,
) -> float:
    """
    Rundet einen Wert.
    """

    return round(
        value,
        digits,
    )


def percentage(
    value: float,
    total: float,
) -> float:

    if total == 0:
        return 0.0

    return round(
        value / total * 100,
        2,
    )


def difference(
    value1: float,
    value2: float,
) -> float:

    return round(
        value2 - value1,
        2,
    )


def average(
    values: list[float],
) -> float:

    if not values:
        return 0.0

    return round(
        mean(values),
        2,
    )


def variance(
    values: list[float],
) -> float:

    if len(values) < 2:
        return 0.0

    avg = mean(values)

    return sum(
        (value - avg) ** 2
        for value in values
    ) / len(values)


def standard_deviation(
    values: list[float],
) -> float:

    return round(
        sqrt(
            variance(values)
        ),
        2,
    )


def normalize(
    value: float,
    minimum: float,
    maximum: float,
) -> float:

    if maximum == minimum:
        return 0.0

    return round(
        (
            value - minimum
        )
        /
        (
            maximum - minimum
        ),
        4,
    )


def clamp(
    value: float,
    minimum: float,
    maximum: float,
) -> float:

    return max(
        minimum,
        min(
            value,
            maximum,
        ),
    )


def moving_average(
    values: list[float],
) -> float:

    return average(values)


def risk_reward(
    reward: float,
    risk: float,
) -> float:

    if risk == 0:
        return 0.0

    return round(
        reward / risk,
        2,
    )
