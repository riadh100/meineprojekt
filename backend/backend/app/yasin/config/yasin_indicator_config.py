from dataclasses import dataclass


@dataclass(frozen=True)
class IndicatorConfig:
    """
    Standardkonfiguration eines Indikators.
    """

    enabled: bool = True
    weight: float = 1.0
    confirmation_required: bool = True
    parameters: dict | None = None


INDICATORS = {

    "EMA": IndicatorConfig(
        weight=1.2,
        parameters={
            "fast": 20,
            "slow": 50,
            "trend": 200,
        },
    ),

    "SMA": IndicatorConfig(
        weight=1.0,
        parameters={
            "period": 200,
        },
    ),

    "RSI": IndicatorConfig(
        weight=1.1,
        parameters={
            "period": 14,
            "overbought": 70,
            "oversold": 30,
        },
    ),

    "MACD": IndicatorConfig(
        weight=1.3,
        parameters={
            "fast": 12,
            "slow": 26,
            "signal": 9,
        },
    ),

    "BOLLINGER_BANDS": IndicatorConfig(
        weight=1.0,
        parameters={
            "period": 20,
            "std_dev": 2,
        },
    ),

    "ATR": IndicatorConfig(
        weight=1.0,
        parameters={
            "period": 14,
        },
    ),

    "ADX": IndicatorConfig(
        weight=1.2,
        parameters={
            "period": 14,
            "minimum_strength": 25,
        },
    ),

    "STOCHASTIC": IndicatorConfig(
        weight=0.9,
        parameters={
            "k": 14,
            "d": 3,
            "smooth": 3,
        },
    ),

    "VWAP": IndicatorConfig(
        weight=1.1,
        parameters={},
    ),

    "SUPERTREND": IndicatorConfig(
        weight=1.4,
        parameters={
            "period": 10,
            "multiplier": 3.0,
        },
    ),
}


def get_indicator(
    name: str,
) -> IndicatorConfig:

    return INDICATORS[name.upper()]


def all_indicators():

    return INDICATORS


def enabled_indicators():

    return {
        name: indicator
        for name, indicator
        in INDICATORS.items()
        if indicator.enabled
    }


def confirmation_score():

    return sum(
        indicator.weight
        for indicator
        in enabled_indicators().values()
        if indicator.confirmation_required
    )
