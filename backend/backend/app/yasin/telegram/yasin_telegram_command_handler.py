from app.yasin.services.yasin_ai_service import (
    YasinAIService,
)

from app.yasin.telegram.yasin_telegram_service import (
    YasinTelegramService,
)


class YasinTelegramCommandHandler:
    """
    Verarbeitet Telegram-Kommandos
    für Yasin AI.
    """

    def __init__(
        self,
        yasin_service: YasinAIService,
        telegram_service: YasinTelegramService,
    ):
        self.yasin = yasin_service
        self.telegram = telegram_service

    def handle(
        self,
        command: str,
    ) -> bool:

        command = command.strip().lower()

        handlers = {
            "/help": self.help,
            "/status": self.status,
            "/signals": self.signals,
            "/stats": self.statistics,
            "/start": self.start,
            "/stop": self.stop,
            "/analyze": self.analyze,
        }

        handler = handlers.get(command)

        if handler is None:
            return self.telegram.send_system_message(
                "❌ Unbekannter Befehl. Nutze /help."
            )

        return handler()

    def help(self):

        return self.telegram.send_system_message(
            """
📖 Verfügbare Befehle

/help
/status
/signals
/stats
/start
/stop
/analyze
"""
        )

    def status(self):

        running = self.yasin.scheduler_running()

        return self.telegram.send_system_message(
            f"🤖 Scheduler: {'Aktiv' if running else 'Gestoppt'}"
        )

    def signals(self):

        signals = self.yasin.get_open_trades()

        return self.telegram.send_system_message(
            f"📊 Offene Trades: {len(signals)}"
        )

    def statistics(self):

        statistics = self.yasin.get_statistics()

        return self.telegram.send_statistics(
            statistics
        )

    def start(self):

        self.yasin.start()

        return self.telegram.send_system_message(
            "▶️ Yasin AI wurde gestartet."
        )

    def stop(self):

        self.yasin.stop()

        return self.telegram.send_system_message(
            "⏹️ Yasin AI wurde gestoppt."
        )

    def analyze(self):

        created = self.yasin.analyze_now()

        return self.telegram.send_system_message(
            f"🧠 Analyse abgeschlossen. Neue Signale: {len(created)}"
        )
