from dataclasses import dataclass


@dataclass(frozen=True)
class AIConfig:
    """
    Zentrale KI-Konfiguration
    für Yasin AI.
    """

    enabled: bool

    minimum_quality_score: float

    minimum_confidence: float

    minimum_confirmations: int

    confirmation_threshold: float

    use_multi_indicator_confirmation: bool

    use_market_trend_filter: bool

    use_volume_filter: bool

    use_volatility_filter: bool

    use_news_filter: bool

    allow_counter_trend: bool

    max_signals_per_market: int

    max_daily_signals: int

    ai_analysis_timeout: int

    indicator_weights: dict

    market_weights: dict


AI_CONFIG = AIConfig(

    enabled=True,

    minimum_quality_score=85.0,

    minimum_confidence=80.0,

    minimum_confirmations=4,

    confirmation_threshold=75.0,

    use_multi_indicator_confirmation=True,

    use_market_trend_filter=True,

    use_volume_filter=True,

    use_volatility_filter=True,

    use_news_filter=False,

    allow_counter_trend=False,

    max_signals_per_market=5,

    max_daily_signals=50,

    ai_analysis_timeout=10,

    indicator_weights={

        "EMA": 1.20,

        "SMA": 1.00,

        "RSI": 1.10,

        "MACD": 1.30,

        "ADX": 1.20,

        "ATR": 1.00,

        "VWAP": 1.10,

        "SUPERTREND": 1.40,

        "STOCHASTIC": 0.90,

        "BOLLINGER_BANDS": 1.00,
    },

    market_weights={

        "GOLD": 1.20,

        "NAS100": 1.15,

        "FOREX": 1.00,

        "CRYPTO": 1.05,

        "CUSTOM_1": 1.00,

        "CUSTOM_2": 1.00,

        "CUSTOM_3": 1.00,

        "CUSTOM_4": 1.00,
    },
)


def get_ai_config():

    return AI_CONFIG


def ai_enabled():

    return AI_CONFIG.enabled


def required_confirmations():

    return AI_CONFIG.minimum_confirmations


def minimum_quality():

    return AI_CONFIG.minimum_quality_score


def minimum_confidence():

    return AI_CONFIG.minimum_confidence


def indicator_weight(
    indicator: str,
):

    return AI_CONFIG.indicator_weights.get(
        indicator.upper(),
        1.0,
    )


def market_weight(
    market: str,
):

    return AI_CONFIG.market_weights.get(
        market.upper(),
        1.0,
    )
