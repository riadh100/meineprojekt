from dataclasses import dataclass


@dataclass(frozen=True)
class TelegramConfig:
    """
    Zentrale Telegram-Konfiguration
    für Yasin AI.
    """

    enabled: bool

    bot_enabled: bool

    channel_enabled: bool

    channel_id: str

    parse_mode: str

    disable_preview: bool

    send_signals: bool

    send_tp_updates: bool

    send_stop_loss: bool

    send_trade_closed: bool

    send_statistics: bool

    send_system_messages: bool

    send_health_reports: bool

    rate_limit_seconds: int

    retry_attempts: int

    retry_delay_seconds: int

    message_prefix: str


TELEGRAM_CONFIG = TelegramConfig(

    enabled=True,

    bot_enabled=True,

    channel_enabled=True,

    channel_id="@your_channel",

    parse_mode="HTML",

    disable_preview=True,

    send_signals=True,

    send_tp_updates=True,

    send_stop_loss=True,

    send_trade_closed=True,

    send_statistics=True,

    send_system_messages=True,

    send_health_reports=True,

    rate_limit_seconds=2,

    retry_attempts=3,

    retry_delay_seconds=5,

    message_prefix="🤖 YASIN AI",
)


def get_telegram_config():

    return TELEGRAM_CONFIG


def telegram_enabled():

    return TELEGRAM_CONFIG.enabled


def can_send_signal():

    return (
        TELEGRAM_CONFIG.enabled
        and TELEGRAM_CONFIG.send_signals
    )


def can_send_statistics():

    return (
        TELEGRAM_CONFIG.enabled
        and TELEGRAM_CONFIG.send_statistics
    )


def can_send_system():

    return (
        TELEGRAM_CONFIG.enabled
        and TELEGRAM_CONFIG.send_system_messages
    )


def can_send_health():

    return (
        TELEGRAM_CONFIG.enabled
        and TELEGRAM_CONFIG.send_health_reports
    )
