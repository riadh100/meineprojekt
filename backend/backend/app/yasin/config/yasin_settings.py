from dataclasses import dataclass, field


@dataclass
class YasinSettings:
    """
    Zentrale Konfiguration für Yasin AI.

    Alle Einstellungen werden hier
    zentral verwaltet.
    """

    # Allgemein

    enabled: bool = True
    debug: bool = False

    # Analyse

    analysis_interval_minutes: int = 5
    monitoring_interval_seconds: int = 30
    statistics_interval_minutes: int = 15

    minimum_signal_quality: float = 85.0
    minimum_risk_reward: float = 2.0

    # Trading

    risk_per_trade_percent: float = 1.0
    max_open_positions: int = 3

    default_timeframe: str = "15m"

    # Märkte

    enable_gold: bool = True
    enable_nas100: bool = True
    enable_forex: bool = True
    enable_crypto: bool = True

    enable_custom_1: bool = True
    enable_custom_2: bool = True
    enable_custom_3: bool = True
    enable_custom_4: bool = True

    # Telegram

    telegram_enabled: bool = True
    telegram_send_statistics: bool = True
    telegram_send_system_messages: bool = True

    # Dashboard

    dashboard_cache_seconds: int = 15
    dashboard_live_updates: bool = True

    # WebSocket

    websocket_enabled: bool = True

    # Backtesting

    default_backtest_balance: float = 10000.0

    # Scheduler

    scheduler_enabled: bool = True

    # Performance

    max_candles: int = 300

    # KI

    ai_confirmation_required: int = 4
    ai_analysis_enabled: bool = True

    # Logging

    log_level: str = "INFO"

    # Erweiterbar

    custom: dict = field(
        default_factory=dict
    )


settings = YasinSettings()
