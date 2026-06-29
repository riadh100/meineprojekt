from app.yasin.config.yasin_indicator_config import (
    get_indicator,
)


def enabled(
    indicator: str,
) -> bool:
    """
    Prüft, ob ein Indikator aktiviert ist.
    """

    return get_indicator(
        indicator
    ).enabled


def weight(
    indicator: str,
) -> float:

    return get_indicator(
        indicator
    ).weight


def parameters(
    indicator: str,
) -> dict:

    config = get_indicator(
        indicator
    )

    return config.parameters or {}


def confirmation_required(
    indicator: str,
) -> bool:

    return get_indicator(
        indicator
    ).confirmation_required


def score(
    indicator: str,
    confirmed: bool,
) -> float:

    if not enabled(indicator):
        return 0.0

    if not confirmed:
        return 0.0

    return weight(indicator)


def confirmation_score(
    confirmations: dict,
) -> float:
    """
    Berechnet den gesamten
    Indikator-Score.
    """

    total = 0.0

    for indicator, confirmed in (
        confirmations.items()
    ):

        total += score(
            indicator,
            confirmed,
        )

    return round(
        total,
        2,
    )


def confirmation_count(
    confirmations: dict,
) -> int:

    return sum(
        1
        for confirmed
        in confirmations.values()
        if confirmed
    )


def confirmation_percent(
    confirmations: dict,
) -> float:

    if not confirmations:
        return 0.0

    confirmed = confirmation_count(
        confirmations
    )

    return round(
        confirmed
        / len(confirmations)
        * 100,
        2,
    )


def passed(
    confirmations: dict,
    minimum: int,
) -> bool:

    return (
        confirmation_count(
            confirmations
        )
        >= minimum
    )
