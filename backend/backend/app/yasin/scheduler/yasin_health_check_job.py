from datetime import datetime

from app.yasin.dashboard.yasin_dashboard_live_updater import (
    YasinDashboardLiveUpdater,
)

from app.yasin.telegram.yasin_telegram_service import (
    YasinTelegramService,
)

from app.yasin.websocket.yasin_system_ws import (
    manager as system_ws,
)

from app.yasin.services.yasin_ai_service import (
    YasinAIService,
)


class YasinHealthCheckJob:
    """
    Überwacht den Gesundheitszustand
    aller Yasin AI Komponenten.
    """

    def __init__(
        self,
        ai_service: YasinAIService,
        telegram: YasinTelegramService,
        dashboard: YasinDashboardLiveUpdater,
    ):
        self.ai = ai_service
        self.telegram = telegram
        self.dashboard = dashboard

    async def run(self):

        report = {
            "timestamp": datetime.utcnow().isoformat(),
            "scheduler": self.ai.scheduler_running(),
            "market_data": self.ai.market_data_available(),
            "telegram": self.ai.telegram_available(),
            "database": self.ai.database_available(),
            "websocket": self.ai.websocket_available(),
            "strategies": self.ai.active_strategy_count(),
            "open_trades": len(
                self.ai.get_open_trades()
            ),
        }

        healthy = all(
            [
                report["scheduler"],
                report["market_data"],
                report["telegram"],
                report["database"],
                report["websocket"],
            ]
        )

        await system_ws.publish_status(
            scheduler_running=report["scheduler"],
            active_strategies=report["strategies"],
            open_trades=report["open_trades"],
            closed_trades=len(
                self.ai.get_closed_trades()
            ),
            uptime_seconds=self.ai.uptime_seconds(),
        )

        if not healthy:

            await system_ws.publish_error(
                "Mindestens ein Dienst ist nicht verfügbar."
            )

            self.telegram.send_system_message(
                "⚠️ Yasin AI Health Check meldet Probleme."
            )

        await self.dashboard.refresh()

        return report

    async def quick_check(self):

        return {
            "scheduler": self.ai.scheduler_running(),
            "database": self.ai.database_available(),
            "telegram": self.ai.telegram_available(),
        }

    async def full_check(self):

        return await self.run()
