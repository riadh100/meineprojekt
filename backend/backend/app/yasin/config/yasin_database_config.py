from dataclasses import dataclass


@dataclass(frozen=True)
class DatabaseConfig:
    """
    Zentrale Datenbank-Konfiguration
    für Yasin AI.
    """

    table_prefix: str

    batch_size: int

    max_query_limit: int

    archive_after_days: int

    delete_after_days: int

    enable_indexes: bool

    enable_query_cache: bool

    auto_vacuum: bool

    auto_analyze: bool

    save_market_snapshots: bool

    save_indicator_snapshots: bool

    save_trade_events: bool

    save_statistics_history: bool

    connection_pool_size: int

    connection_timeout: int


DATABASE_CONFIG = DatabaseConfig(

    table_prefix="yasin_",

    batch_size=500,

    max_query_limit=1000,

    archive_after_days=90,

    delete_after_days=365,

    enable_indexes=True,

    enable_query_cache=True,

    auto_vacuum=True,

    auto_analyze=True,

    save_market_snapshots=True,

    save_indicator_snapshots=True,

    save_trade_events=True,

    save_statistics_history=True,

    connection_pool_size=20,

    connection_timeout=30,
)


def get_database_config():

    return DATABASE_CONFIG


def archive_enabled():

    return (
        DATABASE_CONFIG.archive_after_days > 0
    )


def snapshots_enabled():

    return (
        DATABASE_CONFIG.save_market_snapshots
        or DATABASE_CONFIG.save_indicator_snapshots
    )


def statistics_history_enabled():

    return (
        DATABASE_CONFIG.save_statistics_history
    )


def database_prefix():

    return DATABASE_CONFIG.table_prefix
