from app.yasin.signals.signal_schema import YasinSignal
from app.yasin.telegram.yasin_telegram_formatter import (
    YasinTelegramFormatter,
)
from app.yasin.signals.signal_repository import SignalRepository


class YasinTelegramSender:
    """
    Versandservice für alle Yasin-Nachrichten.

    Nutzt den bestehenden Telegram-Service aus V8.
    Diese Klasse erzeugt keine Nachrichten selbst,
    sondern verwendet den YasinTelegramFormatter.
    """

    def __init__(
        self,
        telegram_service,
        repository: SignalRepository,
    ):
        self.telegram = telegram_service
        self.repository = repository

    def send_new_signal(
        self,
        signal: YasinSignal,
    ) -> bool:

        if signal.is_sent_to_telegram:
            return False

        message = YasinTelegramFormatter.format_new_signal(signal)

        success = self.telegram.send_message(message)

        if success:
            self.repository.mark_sent_to_telegram(signal)

        return success

    def send_tp1(self, signal: YasinSignal) -> bool:

        return self.telegram.send_message(
            YasinTelegramFormatter.format_tp1(signal)
        )

    def send_tp2(self, signal: YasinSignal) -> bool:

        return self.telegram.send_message(
            YasinTelegramFormatter.format_tp2(signal)
        )

    def send_tp3(self, signal: YasinSignal) -> bool:

        return self.telegram.send_message(
            YasinTelegramFormatter.format_tp3(signal)
        )

    def send_stop_loss(self, signal: YasinSignal) -> bool:

        return self.telegram.send_message(
            YasinTelegramFormatter.format_stop_loss(signal)
        )

    def send_trade_closed(self, signal: YasinSignal) -> bool:

        return self.telegram.send_message(
            YasinTelegramFormatter.format_trade_closed(signal)
        )
