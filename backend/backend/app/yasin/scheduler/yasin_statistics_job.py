from app.yasin.dashboard.yasin_dashboard_live_updater import (
    YasinDashboardLiveUpdater,
)

from app.yasin.services.yasin_statistics_service_v2 import (
    YasinStatisticsServiceV2,
)

from app.yasin.telegram.yasin_telegram_service import (
    YasinTelegramService,
)

from app.yasin.websocket.yasin_statistics_ws import (
    manager as statistics_ws,
)


class YasinStatisticsJob:
    """
    Aktualisiert regelmäßig alle
    Trading-Statistiken von Yasin AI.
    """

    def __init__(
        self,
        statistics_service: YasinStatisticsServiceV2,
        dashboard: YasinDashboardLiveUpdater,
        telegram: YasinTelegramService,
    ):
        self.statistics_service = statistics_service
        self.dashboard = dashboard
        self.telegram = telegram

    async def run(self):

        statistics = (
            self.statistics_service.rebuild_all()
        )

        for market in statistics:

            await statistics_ws.market_statistics_updated(
                {
                    "market": market.market,
                    "win_rate": market.win_rate,
                    "profit_factor": market.profit_factor,
                    "net_profit": market.net_profit,
                    "drawdown": market.max_drawdown,
                }
            )

        await statistics_ws.statistics_updated(
            {
                "markets": len(statistics),
            }
        )

        await self.dashboard.statistics_updated()

        self._send_reports(
            statistics
        )

        return statistics

    def _send_reports(
        self,
        statistics,
    ):

        for market in statistics:

            self.telegram.send_statistics(
                market
            )

    async def rebuild_market(
        self,
        market: str,
    ):

        statistics = (
            self.statistics_service.rebuild_market(
                market
            )
        )

        await statistics_ws.market_statistics_updated(
            {
                "market": statistics.market,
                "win_rate": statistics.win_rate,
                "profit_factor": statistics.profit_factor,
                "net_profit": statistics.net_profit,
            }
        )

        await self.dashboard.statistics_updated()

        self.telegram.send_statistics(
            statistics
        )

        return statistics
