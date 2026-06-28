from dataclasses import dataclass, field


@dataclass(frozen=True)
class StrategyConfig:
    """
    Zentrale Konfiguration einer
    Yasin AI Strategie.
    """

    name: str

    enabled: bool

    markets: list[str]

    indicators: list[str]

    minimum_confirmations: int

    minimum_quality: float

    minimum_rr: float

    allow_counter_trend: bool = False

    timeframes: list[str] = field(
        default_factory=lambda: [
            "5m",
            "15m",
            "1h",
        ]
    )


STRATEGIES = {

    "GOLD": StrategyConfig(
        name="Gold Strategy",
        enabled=True,
        markets=["GOLD"],
        indicators=[
            "EMA",
            "RSI",
            "MACD",
            "VWAP",
            "SUPERTREND",
        ],
        minimum_confirmations=4,
        minimum_quality=90.0,
        minimum_rr=2.5,
    ),

    "NAS100": StrategyConfig(
        name="NAS100 Strategy",
        enabled=True,
        markets=["NAS100"],
        indicators=[
            "EMA",
            "MACD",
            "ADX",
            "SUPERTREND",
        ],
        minimum_confirmations=4,
        minimum_quality=88.0,
        minimum_rr=2.3,
    ),

    "FOREX": StrategyConfig(
        name="Forex Strategy",
        enabled=True,
        markets=["FOREX"],
        indicators=[
            "EMA",
            "RSI",
            "ATR",
            "ADX",
        ],
        minimum_confirmations=4,
        minimum_quality=85.0,
        minimum_rr=2.0,
    ),

    "CRYPTO": StrategyConfig(
        name="Crypto Strategy",
        enabled=True,
        markets=["CRYPTO"],
        indicators=[
            "EMA",
            "MACD",
            "VWAP",
            "ATR",
            "SUPERTREND",
        ],
        minimum_confirmations=4,
        minimum_quality=86.0,
        minimum_rr=2.2,
    ),

    "CUSTOM": StrategyConfig(
        name="Custom Strategy",
        enabled=True,
        markets=[
            "CUSTOM_1",
            "CUSTOM_2",
            "CUSTOM_3",
            "CUSTOM_4",
        ],
        indicators=[
            "EMA",
            "RSI",
            "MACD",
        ],
        minimum_confirmations=3,
        minimum_quality=85.0,
        minimum_rr=2.0,
    ),
}


def get_strategy(
    name: str,
) -> StrategyConfig:

    return STRATEGIES[
        name.upper()
    ]


def enabled_strategies():

    return {
        name: strategy
        for name, strategy
        in STRATEGIES.items()
        if strategy.enabled
    }


def all_strategies():

    return STRATEGIES


def strategy_names():

    return list(
        STRATEGIES.keys()
    )
