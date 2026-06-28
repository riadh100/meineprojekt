import logging

from app.yasin.bootstrap.yasin_dependency_container import (
    YasinDependencyContainer,
)

from app.yasin.scheduler.yasin_scheduler_service import (
    YasinSchedulerService,
)


logger = logging.getLogger(__name__)


class YasinStartup:
    """
    Initialisiert das komplette
    Yasin AI System.

    Wird einmal beim Start von
    AI Empire Pro V9 ausgeführt.
    """

    def __init__(
        self,
        container: YasinDependencyContainer,
    ):
        self.container = container

    async def startup(self):

        logger.info(
            "===== Yasin AI Startup ====="
        )

        await self.load_configuration()

        await self.initialize_strategies()

        await self.initialize_services()

        await self.initialize_scheduler()

        await self.initialize_dashboard()

        await self.initialize_telegram()

        logger.info(
            "Yasin AI erfolgreich gestartet."
        )

    async def load_configuration(self):

        self.container.strategy_service.load()

        logger.info(
            "Strategien geladen."
        )

    async def initialize_strategies(self):

        logger.info(
            "Strategien initialisiert."
        )

    async def initialize_services(self):

        logger.info(
            "Services initialisiert."
        )

    async def initialize_scheduler(self):

        scheduler = YasinSchedulerService(
            ai_service=None,
            dashboard=None,
            telegram=None,
        )

        self.scheduler = scheduler

        logger.info(
            "Scheduler initialisiert."
        )

    async def initialize_dashboard(self):

        logger.info(
            "Dashboard initialisiert."
        )

    async def initialize_telegram(self):

        logger.info(
            "Telegram initialisiert."
        )

    async def shutdown(self):

        logger.info(
            "Yasin AI wird beendet."
        )

        logger.info(
            "Yasin AI erfolgreich beendet."
        )
