from datetime import datetime, timedelta

from app.yasin.services.yasin_ai_service import (
    YasinAIService,
)

from app.yasin.dashboard.yasin_dashboard_live_updater import (
    YasinDashboardLiveUpdater,
)

from app.yasin.telegram.yasin_telegram_scheduler import (
    YasinTelegramScheduler,
)


class YasinSchedulerService:
    """
    Scheduler-Service für Yasin AI.

    Arbeitet mit dem bestehenden Scheduler
    aus AI Empire Pro V8 zusammen.
    """

    ANALYSIS_INTERVAL = timedelta(minutes=5)
    MONITOR_INTERVAL = timedelta(seconds=30)
    STATISTICS_INTERVAL = timedelta(minutes=15)

    def __init__(
        self,
        ai_service: YasinAIService,
        dashboard: YasinDashboardLiveUpdater,
        telegram: YasinTelegramScheduler,
    ):
        self.ai = ai_service
        self.dashboard = dashboard
        self.telegram = telegram

        now = datetime.utcnow()

        self._last_analysis = now
        self._last_monitor = now
        self._last_statistics = now

    async def tick(self):
        """
        Wird regelmäßig vom V8 Scheduler aufgerufen.
        """

        now = datetime.utcnow()

        if self._should_run(
            self._last_analysis,
            self.ANALYSIS_INTERVAL,
        ):
            await self.run_analysis()
            self._last_analysis = now

        if self._should_run(
            self._last_monitor,
            self.MONITOR_INTERVAL,
        ):
            await self.run_monitoring()
            self._last_monitor = now

        if self._should_run(
            self._last_statistics,
            self.STATISTICS_INTERVAL,
        ):
            await self.run_statistics()
            self._last_statistics = now

        self.telegram.run()

    async def run_analysis(self):

        self.ai.analyze_now()

        await self.dashboard.signal_updated()

    async def run_monitoring(self):

        self.ai.monitor_now()

        await self.dashboard.refresh()

    async def run_statistics(self):

        self.ai.rebuild_statistics()

        await self.dashboard.statistics_updated()

    def _should_run(
        self,
        last_run: datetime,
        interval: timedelta,
    ) -> bool:

        return (
            datetime.utcnow() - last_run
        ) >= interval
