from datetime import datetime, timedelta


class YasinTelegramScheduler:
    """
    Führt zeitgesteuerte Telegram-Aufgaben aus.

    Diese Klasse arbeitet mit dem Scheduler aus
    AI Empire Pro V8 zusammen.
    """

    def __init__(
        self,
        telegram_service,
        statistics_service,
        ai_service,
    ):
        self.telegram = telegram_service
        self.statistics = statistics_service
        self.ai = ai_service

        self._last_daily_report = None
        self._last_statistics = None
        self._last_status = None

    def run(self):
        """
        Wird regelmäßig vom V8 Scheduler aufgerufen.
        """

        now = datetime.utcnow()

        self._daily_report(now)
        self._statistics_report(now)
        self._system_status(now)

    def _daily_report(
        self,
        now: datetime,
    ):

        if (
            self._last_daily_report
            and self._last_daily_report.date() == now.date()
        ):
            return

        stats = self.statistics.overview()

        self.telegram.send_statistics(stats)

        self._last_daily_report = now

    def _statistics_report(
        self,
        now: datetime,
    ):

        if (
            self._last_statistics
            and now - self._last_statistics
            < timedelta(hours=4)
        ):
            return

        stats = self.statistics.overview()

        self.telegram.send_statistics(stats)

        self._last_statistics = now

    def _system_status(
        self,
        now: datetime,
    ):

        if (
            self._last_status
            and now - self._last_status
            < timedelta(hours=1)
        ):
            return

        running = self.ai.scheduler_running()

        message = (
            "🟢 Yasin AI läuft."
            if running
            else "🔴 Yasin AI ist gestoppt."
        )

        self.telegram.send_system_message(
            message
        )

        self._last_status = now

    def force_daily_report(self):

        stats = self.statistics.overview()

        return self.telegram.send_statistics(
            stats
        )

    def force_system_status(self):

        running = self.ai.scheduler_running()

        return self.telegram.send_system_message(
            "🟢 Aktiv"
            if running
            else "🔴 Gestoppt"
        )

    def force_statistics(self):

        return self.telegram.send_statistics(
            self.statistics.overview()
        )
