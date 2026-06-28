from typing import Iterable

from app.yasin.signals.signal_repository import SignalRepository
from app.yasin.telegram.yasin_telegram_sender import YasinTelegramSender


class YasinOrchestrator:
    """
    Zentraler Ablaufmanager für Yasin AI.

    Führt Strategien aus, speichert freigegebene Signale
    und sendet sie automatisch an Telegram.
    """

    def __init__(
        self,
        repository: SignalRepository,
        telegram_sender: YasinTelegramSender,
    ):
        self.repository = repository
        self.telegram_sender = telegram_sender

    def run_strategies(self, strategies: Iterable) -> list:
        created_signals = []

        for strategy in strategies:
            signal = strategy.analyze()

            if signal is None:
                continue

            saved_signal = self.repository.save(signal)
            self.telegram_sender.send_new_signal(saved_signal)

            created_signals.append(saved_signal)

        return created_signals
