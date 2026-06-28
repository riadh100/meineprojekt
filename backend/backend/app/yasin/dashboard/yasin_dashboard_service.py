from app.yasin.repositories.yasin_signal_repository import (
    YasinSignalRepository,
)

from app.yasin.repositories.yasin_trade_statistics_repository import (
    YasinTradeStatisticsRepository,
)

from app.yasin.services.yasin_ai_service import (
    YasinAIService,
)


class YasinDashboardService:
    """
    Zentraler Dashboard-Service.

    Aggregiert alle Daten für das
    Yasin Dashboard.
    """

    def __init__(
        self,
        signal_repository: YasinSignalRepository,
        statistics_repository: YasinTradeStatisticsRepository,
        ai_service: YasinAIService,
    ):
        self.signal_repository = signal_repository
        self.statistics_repository = (
            statistics_repository
        )
        self.ai_service = ai_service

    def dashboard(self) -> dict:

        open_trades = (
            self.signal_repository.get_open_signals()
        )

        closed_trades = (
            self.signal_repository.get_closed_signals()
        )

        latest_signals = (
            self.signal_repository.get_all()[:10]
        )

        statistics = (
            self.statistics_repository.get_all()
        )

        return {
            "system": self.system_status(),
            "summary": self.summary(),
            "statistics": statistics,
            "latest_signals": latest_signals,
            "open_trades": open_trades,
            "closed_trades": closed_trades,
        }

    def summary(self) -> dict:

        open_trades = (
            self.signal_repository.get_open_signals()
        )

        closed_trades = (
            self.signal_repository.get_closed_signals()
        )

        return {
            "total_signals":
                len(open_trades) + len(closed_trades),

            "open_trades":
                len(open_trades),

            "closed_trades":
                len(closed_trades),
        }

    def system_status(self):

        return {
            "scheduler_running":
                self.ai_service.scheduler_running(),

            "open_trades":
                len(
                    self.ai_service.get_open_trades()
                ),

            "closed_trades":
                len(
                    self.ai_service.get_closed_trades()
                ),

            "signals":
                len(
                    self.ai_service.get_all_signals()
                ),
        }

    def latest_signals(
        self,
        limit: int = 10,
    ):

        return self.signal_repository.get_all()[:limit]

    def open_trades(self):

        return (
            self.signal_repository.get_open_signals()
        )

    def closed_trades(self):

        return (
            self.signal_repository.get_closed_signals()
        )

    def statistics(self):

        return (
            self.statistics_repository.get_all()
        )
