from typing import List, Optional

from sqlalchemy.orm import Session

from app.yasin.models.yasin_trade_event_model import (
    TradeEventType,
    YasinTradeEventModel,
)


class YasinTradeEventRepository:
    """
    Repository für Trade-Events von Yasin AI.
    """

    def __init__(self, db: Session):
        self.db = db

    def create(
        self,
        event: YasinTradeEventModel,
    ) -> YasinTradeEventModel:

        self.db.add(event)
        self.db.commit()
        self.db.refresh(event)

        return event

    def log_event(
        self,
        *,
        signal_id: int,
        event_type: TradeEventType | str,
        title: str,
        description: str | None = None,
    ) -> YasinTradeEventModel:

        event = YasinTradeEventModel(
            signal_id=signal_id,
            event_type=event_type.value
            if isinstance(event_type, TradeEventType)
            else event_type,
            title=title,
            description=description,
        )

        return self.create(event)

    def get(
        self,
        event_id: int,
    ) -> Optional[YasinTradeEventModel]:

        return (
            self.db.query(YasinTradeEventModel)
            .filter(YasinTradeEventModel.id == event_id)
            .first()
        )

    def get_by_signal(
        self,
        signal_id: int,
    ) -> List[YasinTradeEventModel]:

        return (
            self.db.query(YasinTradeEventModel)
            .filter(YasinTradeEventModel.signal_id == signal_id)
            .order_by(YasinTradeEventModel.created_at.asc())
            .all()
        )

    def get_by_type(
        self,
        event_type: TradeEventType | str,
    ) -> List[YasinTradeEventModel]:

        value = (
            event_type.value
            if isinstance(event_type, TradeEventType)
            else event_type
        )

        return (
            self.db.query(YasinTradeEventModel)
            .filter(YasinTradeEventModel.event_type == value)
            .order_by(YasinTradeEventModel.created_at.desc())
            .all()
        )

    def delete(
        self,
        event_id: int,
    ) -> bool:

        event = self.get(event_id)

        if event is None:
            return False

        self.db.delete(event)
        self.db.commit()

        return True
