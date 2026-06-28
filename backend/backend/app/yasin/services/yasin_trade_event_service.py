from app.yasin.models.yasin_trade_event_model import (
    TradeEventType,
    YasinTradeEventModel,
)

from app.yasin.repositories.yasin_trade_event_repository import (
    YasinTradeEventRepository,
)


class YasinTradeEventService:
    """
    Zentraler Service für alle Trade-Ereignisse.

    Alle Module (SignalGenerator, Telegram,
    TradeMonitor usw.) verwenden ausschließlich
    diesen Service zum Schreiben von Events.
    """

    def __init__(
        self,
        repository: YasinTradeEventRepository,
    ):
        self.repository = repository

    def signal_created(
        self,
        signal_id: int,
    ) -> YasinTradeEventModel:

        return self.repository.log_event(
            signal_id=signal_id,
            event_type=TradeEventType.SIGNAL_CREATED,
            title="Signal erstellt",
        )

    def signal_approved(
        self,
        signal_id: int,
    ) -> YasinTradeEventModel:

        return self.repository.log_event(
            signal_id=signal_id,
            event_type=TradeEventType.SIGNAL_APPROVED,
            title="Signal freigegeben",
        )

    def signal_rejected(
        self,
        signal_id: int,
        reason: str,
    ) -> YasinTradeEventModel:

        return self.repository.log_event(
            signal_id=signal_id,
            event_type=TradeEventType.SIGNAL_REJECTED,
            title="Signal verworfen",
            description=reason,
        )

    def telegram_sent(
        self,
        signal_id: int,
    ) -> YasinTradeEventModel:

        return self.repository.log_event(
            signal_id=signal_id,
            event_type=TradeEventType.TELEGRAM_SENT,
            title="Telegram Signal versendet",
        )

    def trade_opened(
        self,
        signal_id: int,
    ) -> YasinTradeEventModel:

        return self.repository.log_event(
            signal_id=signal_id,
            event_type=TradeEventType.TRADE_OPENED,
            title="Trade eröffnet",
        )

    def tp1(
        self,
        signal_id: int,
    ) -> YasinTradeEventModel:

        return self.repository.log_event(
            signal_id=signal_id,
            event_type=TradeEventType.TP1_REACHED,
            title="TP1 erreicht",
        )

    def tp2(
        self,
        signal_id: int,
    ) -> YasinTradeEventModel:

        return self.repository.log_event(
            signal_id=signal_id,
            event_type=TradeEventType.TP2_REACHED,
            title="TP2 erreicht",
        )

    def tp3(
        self,
        signal_id: int,
    ) -> YasinTradeEventModel:

        return self.repository.log_event(
            signal_id=signal_id,
            event_type=TradeEventType.TP3_REACHED,
            title="TP3 erreicht",
        )

    def stop_loss(
        self,
        signal_id: int,
    ) -> YasinTradeEventModel:

        return self.repository.log_event(
            signal_id=signal_id,
            event_type=TradeEventType.STOP_LOSS,
            title="Stop Loss erreicht",
        )

    def break_even(
        self,
        signal_id: int,
    ) -> YasinTradeEventModel:

        return self.repository.log_event(
            signal_id=signal_id,
            event_type=TradeEventType.BREAK_EVEN,
            title="Break Even aktiviert",
        )

    def trailing_stop(
        self,
        signal_id: int,
    ) -> YasinTradeEventModel:

        return self.repository.log_event(
            signal_id=signal_id,
            event_type=TradeEventType.TRAILING_STOP,
            title="Trailing Stop aktualisiert",
        )

    def trade_closed(
        self,
        signal_id: int,
    ) -> YasinTradeEventModel:

        return self.repository.log_event(
            signal_id=signal_id,
            event_type=TradeEventType.TRADE_CLOSED,
            title="Trade abgeschlossen",
        )

    def error(
        self,
        signal_id: int,
        message: str,
    ) -> YasinTradeEventModel:

        return self.repository.log_event(
            signal_id=signal_id,
            event_type=TradeEventType.ERROR,
            title="Fehler",
            description=message,
        )
