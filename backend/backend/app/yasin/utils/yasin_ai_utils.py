from app.yasin.config.yasin_ai_config import (
    get_ai_config,
)


def confidence_score(
    confirmations: int,
    total_indicators: int,
) -> float:
    """
    Berechnet den KI-Confidence-Wert.
    """

    if total_indicators == 0:
        return 0.0

    return round(
        confirmations
        / total_indicators
        * 100,
        2,
    )


def weighted_score(
    confirmations: dict,
    weights: dict,
) -> float:

    total = 0.0

    maximum = 0.0

    for indicator, weight in weights.items():

        maximum += weight

        if confirmations.get(indicator, False):
            total += weight

    if maximum == 0:
        return 0.0

    return round(
        total / maximum * 100,
        2,
    )


def market_score(
    quality: float,
    market_weight: float,
) -> float:

    return round(
        quality * market_weight,
        2,
    )


def approve_signal(
    *,
    quality: float,
    confidence: float,
    confirmations: int,
) -> bool:

    config = get_ai_config()

    return (
        quality
        >= config.minimum_quality_score
        and confidence
        >= config.minimum_confidence
        and confirmations
        >= config.minimum_confirmations
    )


def decision(
    *,
    quality: float,
    confidence: float,
    confirmations: int,
) -> str:

    if approve_signal(
        quality=quality,
        confidence=confidence,
        confirmations=confirmations,
    ):
        return "APPROVED"

    config = get_ai_config()

    if (
        quality
        >= config.minimum_quality_score * 0.8
    ):
        return "REVIEW"

    return "REJECTED"


def score_summary(
    *,
    quality: float,
    confidence: float,
    confirmations: int,
) -> dict:

    return {
        "quality": quality,
        "confidence": confidence,
        "confirmations": confirmations,
        "approved": approve_signal(
            quality=quality,
            confidence=confidence,
            confirmations=confirmations,
        ),
        "decision": decision(
            quality=quality,
            confidence=confidence,
            confirmations=confirmations,
        ),
    }
