from dataclasses import dataclass


@dataclass(frozen=True)
class BacktestingConfig:
    """
    Zentrale Backtesting-Konfiguration
    für Yasin AI.
    """

    enabled: bool

    initial_balance: float

    leverage: int

    commission_percent: float

    slippage_points: float

    spread_points: float

    default_position_size: float

    risk_per_trade: float

    max_open_positions: int

    use_compound_growth: bool

    save_trade_history: bool

    generate_equity_curve: bool

    generate_statistics: bool

    export_csv: bool

    export_json: bool

    export_pdf: bool

    max_history_candles: int


BACKTESTING_CONFIG = BacktestingConfig(

    enabled=True,

    initial_balance=10000.0,

    leverage=10,

    commission_percent=0.05,

    slippage_points=0.5,

    spread_points=1.0,

    default_position_size=1.0,

    risk_per_trade=1.0,

    max_open_positions=3,

    use_compound_growth=True,

    save_trade_history=True,

    generate_equity_curve=True,

    generate_statistics=True,

    export_csv=True,

    export_json=True,

    export_pdf=False,

    max_history_candles=10000,
)


def get_backtesting_config():

    return BACKTESTING_CONFIG


def export_enabled():

    return (
        BACKTESTING_CONFIG.export_csv
        or BACKTESTING_CONFIG.export_json
        or BACKTESTING_CONFIG.export_pdf
    )


def statistics_enabled():

    return (
        BACKTESTING_CONFIG.generate_statistics
    )


def equity_curve_enabled():

    return (
        BACKTESTING_CONFIG.generate_equity_curve
    )


def history_limit():

    return (
        BACKTESTING_CONFIG.max_history_candles
    )
