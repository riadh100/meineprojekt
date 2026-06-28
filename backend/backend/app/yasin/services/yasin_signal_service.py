from typing import Optional

from app.yasin.models.yasin_signal_model import (
    YasinSignalModel,
)

from app.yasin.repositories.yasin_signal_repository import (
    YasinSignalRepository,
)

from app.yasin.services.yasin_trade_event_service import (
    YasinTradeEventService,
)

from app.yasin.telegram.yasin_telegram_sender import (
    YasinTelegramSender,
)


class YasinSignalService:
    """
    Zentrale Business-Logik für alle Yasin-Signale.

    Verantwortlich für:
    - Speichern
    - Freigeben
    - Telegram-Versand
    - Statusänderungen
    - Event-Protokollierung
    """

    def __init__(
        self,
        repository: YasinSignalRepository,
        telegram: YasinTelegramSender,
        events: YasinTradeEventService,
    ):
        self.repository = repository
        self.telegram = telegram
        self.events = events

    def create(
        self,
        signal: YasinSignalModel,
    ) -> YasinSignalModel:

        signal = self.repository.create(signal)

        self.events.signal_created(signal.id)

        if signal.is_approved:
            self.events.signal_approved(signal.id)
        else:
            self.events.signal_rejected(
                signal.id,
                "Signal erfüllt die Mindestqualität nicht.",
            )

        return signal

    def publish(
        self,
        signal: YasinSignalModel,
    ) -> bool:

        if not signal.is_approved:
            return False

        success = self.telegram.send_new_signal(signal)

        if success:
            self.repository.mark_sent(signal.id)
            self.events.telegram_sent(signal.id)

        return success

    def close_trade(
        self,
        signal_id: int,
        *,
        close_price: float,
        status: str,
        realized_profit: float,
        realized_profit_percent: float,
    ) -> Optional[YasinSignalModel]:

        signal = self.repository.close_trade(
            signal_id=signal_id,
            close_price=close_price,
            status=status,
            realized_profit=realized_profit,
            realized_profit_percent=realized_profit_percent,
        )

        if signal is not None:
            self.events.trade_closed(signal.id)

        return signal

    def get_open_signals(self):
        return self.repository.get_open_signals()

    def get_closed_signals(self):
        return self.repository.get_closed_signals()

    def get_all(self):
        return self.repository.get_all()

    def latest(
        self,
        symbol: str,
    ):
        return self.repository.latest(symbol)

    def get(
        self,
        signal_id: int,
    ):
        return self.repository.get(signal_id)
