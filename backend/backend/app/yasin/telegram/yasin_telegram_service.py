from app.services.telegram.telegram_service import TelegramService

from app.yasin.telegram.yasin_telegram_message_builder import (
    YasinTelegramMessageBuilder,
)


class YasinTelegramService:
    """
    Zentraler Telegram-Service für Yasin AI.

    Erstellt alle Nachrichten und versendet sie
    über den bestehenden Telegram-Service aus V8.
    """

    def __init__(
        self,
        telegram_service: TelegramService,
    ):
        self.telegram = telegram_service

    def send_signal(
        self,
        signal,
    ) -> bool:

        message = (
            YasinTelegramMessageBuilder.new_signal(
                signal
            )
        )

        return self.telegram.send_message(
            message
        )

    def send_tp1(
        self,
        signal,
    ) -> bool:

        return self.telegram.send_message(
            YasinTelegramMessageBuilder.tp1(
                signal
            )
        )

    def send_tp2(
        self,
        signal,
    ) -> bool:

        return self.telegram.send_message(
            YasinTelegramMessageBuilder.tp2(
                signal
            )
        )

    def send_tp3(
        self,
        signal,
    ) -> bool:

        return self.telegram.send_message(
            YasinTelegramMessageBuilder.tp3(
                signal
            )
        )

    def send_stop_loss(
        self,
        signal,
    ) -> bool:

        return self.telegram.send_message(
            YasinTelegramMessageBuilder.stop_loss(
                signal
            )
        )

    def send_trade_closed(
        self,
        signal,
    ) -> bool:

        return self.telegram.send_message(
            YasinTelegramMessageBuilder.trade_closed(
                signal
            )
        )

    def send_statistics(
        self,
        statistics,
    ) -> bool:

        return self.telegram.send_message(
            YasinTelegramMessageBuilder.statistics(
                statistics
            )
        )

    def send_system_message(
        self,
        message: str,
    ) -> bool:

        return self.telegram.send_message(
            YasinTelegramMessageBuilder.system(
                message
            )
        )
