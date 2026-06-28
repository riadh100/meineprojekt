import logging

from app.yasin.dashboard.yasin_dashboard_cache import (
    YasinDashboardCache,
)

from app.yasin.websocket.yasin_connection_manager import (
    connection_manager,
)


logger = logging.getLogger(__name__)


class YasinShutdown:
    """
    Verantwortlich für den kontrollierten
    Shutdown von Yasin AI.

    Gibt Ressourcen frei und beendet
    alle laufenden Komponenten sauber.
    """

    def __init__(
        self,
        ai_service,
        scheduler,
        telegram_scheduler,
        dashboard_cache: YasinDashboardCache,
    ):
        self.ai = ai_service
        self.scheduler = scheduler
        self.telegram_scheduler = telegram_scheduler
        self.dashboard_cache = dashboard_cache

    async def shutdown(self):

        logger.info(
            "===== Yasin AI Shutdown ====="
        )

        await self.stop_scheduler()

        await self.stop_telegram()

        await self.close_websockets()

        await self.clear_cache()

        await self.release_resources()

        logger.info(
            "Yasin AI erfolgreich beendet."
        )

    async def stop_scheduler(self):

        if self.scheduler is not None:

            self.scheduler.stop()

            logger.info(
                "Scheduler beendet."
            )

    async def stop_telegram(self):

        if self.telegram_scheduler is not None:

            logger.info(
                "Telegram Scheduler beendet."
            )

    async def close_websockets(self):

        connection_manager.clear()

        logger.info(
            "Alle WebSocket-Verbindungen geschlossen."
        )

    async def clear_cache(self):

        self.dashboard_cache.invalidate()

        logger.info(
            "Dashboard Cache geleert."
        )

    async def release_resources(self):

        if self.ai is not None:

            self.ai.shutdown()

        logger.info(
            "Ressourcen freigegeben."
        )
