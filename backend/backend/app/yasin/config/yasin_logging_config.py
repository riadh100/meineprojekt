from dataclasses import dataclass


@dataclass(frozen=True)
class LoggingConfig:
    """
    Zentrale Logging-Konfiguration
    für Yasin AI.
    """

    enabled: bool

    level: str

    log_directory: str

    application_log: str

    error_log: str

    scheduler_log: str

    analysis_log: str

    telegram_log: str

    websocket_log: str

    max_file_size_mb: int

    backup_count: int

    console_logging: bool

    file_logging: bool

    log_analysis: bool

    log_scheduler: bool

    log_signals: bool

    log_database: bool

    log_websocket: bool

    log_telegram: bool

    log_performance: bool


LOGGING_CONFIG = LoggingConfig(

    enabled=True,

    level="INFO",

    log_directory="logs/yasin",

    application_log="application.log",

    error_log="errors.log",

    scheduler_log="scheduler.log",

    analysis_log="analysis.log",

    telegram_log="telegram.log",

    websocket_log="websocket.log",

    max_file_size_mb=20,

    backup_count=10,

    console_logging=True,

    file_logging=True,

    log_analysis=True,

    log_scheduler=True,

    log_signals=True,

    log_database=True,

    log_websocket=True,

    log_telegram=True,

    log_performance=True,
)


def get_logging_config():

    return LOGGING_CONFIG


def logging_enabled():

    return LOGGING_CONFIG.enabled


def console_enabled():

    return LOGGING_CONFIG.console_logging


def file_logging_enabled():

    return LOGGING_CONFIG.file_logging


def log_level():

    return LOGGING_CONFIG.level


def log_directory():

    return LOGGING_CONFIG.log_directory
