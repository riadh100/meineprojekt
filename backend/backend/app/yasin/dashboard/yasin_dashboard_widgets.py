from app.yasin.dashboard.yasin_dashboard_mapper import (
    YasinDashboardMapper,
)


class YasinDashboardWidgets:
    """
    Erzeugt Dashboard-Widgets für das
    Yasin Dashboard.
    """

    @staticmethod
    def performance(statistics):

        return {
            "type": "performance",
            "title": "Performance",
            "data": YasinDashboardMapper.statistics_list(
                statistics
            ),
        }

    @staticmethod
    def open_trades(signals):

        return {
            "type": "open_trades",
            "title": "Offene Trades",
            "count": len(signals),
            "data": YasinDashboardMapper.signals(
                signals
            ),
        }

    @staticmethod
    def latest_signals(signals):

        return {
            "type": "latest_signals",
            "title": "Letzte Signale",
            "count": len(signals),
            "data": YasinDashboardMapper.signals(
                signals
            ),
        }

    @staticmethod
    def summary(summary):

        return {
            "type": "summary",
            "title": "Übersicht",
            "data": summary,
        }

    @staticmethod
    def system(system):

        return {
            "type": "system",
            "title": "Systemstatus",
            "data": system,
        }

    @staticmethod
    def markets(statistics):

        return {
            "type": "markets",
            "title": "Marktübersicht",
            "markets": [
                {
                    "market": item.market,
                    "win_rate": item.win_rate,
                    "profit_factor": item.profit_factor,
                    "net_profit": item.net_profit,
                }
                for item in statistics
            ],
        }

    @classmethod
    def dashboard(
        cls,
        *,
        summary,
        system,
        statistics,
        open_trades,
        latest_signals,
    ):

        return {
            "summary": cls.summary(summary),
            "system": cls.system(system),
            "performance": cls.performance(
                statistics
            ),
            "markets": cls.markets(
                statistics
            ),
            "open_trades": cls.open_trades(
                open_trades
            ),
            "latest_signals": cls.latest_signals(
                latest_signals
            ),
        }
