from datetime import datetime
from typing import List, Optional

from sqlalchemy.orm import Session

from app.yasin.models.yasin_signal_model import YasinSignalModel


class YasinSignalRepository:
    """
    Datenbank-Repository für alle Yasin-Signale.
    """

    def __init__(self, db: Session):
        self.db = db

    def create(self, signal: YasinSignalModel) -> YasinSignalModel:
        self.db.add(signal)
        self.db.commit()
        self.db.refresh(signal)
        return signal

    def update(self, signal: YasinSignalModel) -> YasinSignalModel:
        signal.updated_at = datetime.utcnow()

        self.db.commit()
        self.db.refresh(signal)

        return signal

    def get(self, signal_id: int) -> Optional[YasinSignalModel]:
        return (
            self.db.query(YasinSignalModel)
            .filter(YasinSignalModel.id == signal_id)
            .first()
        )

    def get_all(self) -> List[YasinSignalModel]:
        return (
            self.db.query(YasinSignalModel)
            .order_by(YasinSignalModel.created_at.desc())
            .all()
        )

    def get_open_signals(self) -> List[YasinSignalModel]:
        return (
            self.db.query(YasinSignalModel)
            .filter(YasinSignalModel.is_closed.is_(False))
            .all()
        )

    def get_closed_signals(self) -> List[YasinSignalModel]:
        return (
            self.db.query(YasinSignalModel)
            .filter(YasinSignalModel.is_closed.is_(True))
            .all()
        )

    def get_by_symbol(
        self,
        symbol: str,
    ) -> List[YasinSignalModel]:

        return (
            self.db.query(YasinSignalModel)
            .filter(YasinSignalModel.symbol == symbol)
            .order_by(YasinSignalModel.created_at.desc())
            .all()
        )

    def latest(
        self,
        symbol: str,
    ) -> Optional[YasinSignalModel]:

        return (
            self.db.query(YasinSignalModel)
            .filter(YasinSignalModel.symbol == symbol)
            .order_by(YasinSignalModel.created_at.desc())
            .first()
        )

    def mark_sent(
        self,
        signal_id: int,
    ) -> Optional[YasinSignalModel]:

        signal = self.get(signal_id)

        if signal is None:
            return None

        signal.is_sent_to_telegram = True

        return self.update(signal)

    def close_trade(
        self,
        signal_id: int,
        close_price: float,
        status: str,
        realized_profit: float,
        realized_profit_percent: float,
    ) -> Optional[YasinSignalModel]:

        signal = self.get(signal_id)

        if signal is None:
            return None

        signal.is_closed = True
        signal.status = status
        signal.close_price = close_price
        signal.closed_at = datetime.utcnow()

        signal.realized_profit = realized_profit
        signal.realized_profit_percent = realized_profit_percent

        return self.update(signal)

    def delete(
        self,
        signal_id: int,
    ) -> bool:

        signal = self.get(signal_id)

        if signal is None:
            return False

        self.db.delete(signal)
        self.db.commit()

        return True
