from dataclasses import dataclass, field


@dataclass(frozen=True)
class DashboardConfig:
    """
    Zentrale Dashboard-Konfiguration
    für Yasin AI.
    """

    enabled: bool

    live_updates: bool

    websocket_enabled: bool

    cache_enabled: bool

    cache_ttl_seconds: int

    refresh_interval_seconds: int

    default_layout: str

    theme: str

    show_system_status: bool

    show_performance: bool

    show_statistics: bool

    show_market_overview: bool

    show_open_trades: bool

    show_latest_signals: bool

    show_notifications: bool

    chart_history_limit: int

    max_latest_signals: int

    max_open_trades: int

    widgets: list[str] = field(
        default_factory=list
    )


DASHBOARD_CONFIG = DashboardConfig(

    enabled=True,

    live_updates=True,

    websocket_enabled=True,

    cache_enabled=True,

    cache_ttl_seconds=15,

    refresh_interval_seconds=5,

    default_layout="default",

    theme="dark",

    show_system_status=True,

    show_performance=True,

    show_statistics=True,

    show_market_overview=True,

    show_open_trades=True,

    show_latest_signals=True,

    show_notifications=True,

    chart_history_limit=500,

    max_latest_signals=10,

    max_open_trades=25,

    widgets=[
        "summary",
        "system",
        "performance",
        "statistics",
        "markets",
        "open_trades",
        "latest_signals",
        "notifications",
    ],
)


def get_dashboard_config():

    return DASHBOARD_CONFIG


def dashboard_enabled():

    return DASHBOARD_CONFIG.enabled


def websocket_enabled():

    return (
        DASHBOARD_CONFIG.websocket_enabled
    )


def cache_enabled():

    return (
        DASHBOARD_CONFIG.cache_enabled
    )


def live_updates_enabled():

    return (
        DASHBOARD_CONFIG.live_updates
    )


def widget_enabled(
    widget: str,
):

    return (
        widget
        in DASHBOARD_CONFIG.widgets
    )
