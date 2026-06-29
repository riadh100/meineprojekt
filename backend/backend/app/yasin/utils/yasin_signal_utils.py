from app.yasin.config.yasin_risk_config import (
    get_risk_config,
)


def risk_reward_ratio(
    entry: float,
    stop_loss: float,
    take_profit: float,
) -> float:
    """
    Berechnet das Risk/Reward-Verhältnis.
    """

    risk = abs(entry - stop_loss)

    reward = abs(take_profit - entry)

    if risk == 0:
        return 0.0

    return round(
        reward / risk,
        2,
    )


def signal_quality(
    *,
    confirmations: int,
    confidence: float,
) -> float:
    """
    Berechnet die Signalqualität.
    """

    config = get_risk_config()

    confirmation_score = min(
        confirmations
        / config.minimum_confirmations,
        1,
    )

    quality = (
        confirmation_score * 50
        + confidence * 0.5
    )

    return round(
        min(
            quality,
            100,
        ),
        2,
    )


def validate_signal(
    *,
    quality: float,
    confirmations: int,
    rr: float,
) -> bool:
    """
    Prüft, ob ein Signal
    freigegeben werden darf.
    """

    config = get_risk_config()

    return (
        quality
        >= config.minimum_signal_quality
        and confirmations
        >= config.minimum_confirmations
        and rr
        >= config.minimum_rr
    )


def tp_hit(
    direction: str,
    current_price: float,
    target: float,
) -> bool:

    direction = direction.upper()

    if direction == "BUY":
        return current_price >= target

    return current_price <= target


def sl_hit(
    direction: str,
    current_price: float,
    stop_loss: float,
) -> bool:

    direction = direction.upper()

    if direction == "BUY":
        return current_price <= stop_loss

    return current_price >= stop_loss


def format_signal(
    signal,
):

    return {
        "symbol": signal.symbol,
        "market": signal.market,
        "direction": signal.direction,
        "entry": signal.entry,
        "stop_loss": signal.stop_loss,
        "tp1": signal.take_profit_1,
        "tp2": signal.take_profit_2,
        "tp3": signal.take_profit_3,
        "quality": signal.quality_score,
        "rr": signal.risk_reward_ratio,
        "status": signal.status,
        "created_at": signal.created_at,
    }


def approved(
    signal,
):

    return (
        signal.is_approved
        and not signal.is_closed
    )
