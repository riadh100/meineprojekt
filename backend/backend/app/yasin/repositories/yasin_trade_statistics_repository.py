from datetime import datetime
from typing import List, Optional

from sqlalchemy.orm import Session

from app.yasin.models.yasin_trade_statistics_model import (
    YasinTradeStatisticsModel,
)


class YasinTradeStatisticsRepository:
    """
    Repository für aggregierte Trading-Statistiken.
    """

    def __init__(self, db: Session):
        self.db = db

    def create(
        self,
        statistics: YasinTradeStatisticsModel,
    ) -> YasinTradeStatisticsModel:

        self.db.add(statistics)
        self.db.commit()
        self.db.refresh(statistics)

        return statistics

    def update(
        self,
        statistics: YasinTradeStatisticsModel,
    ) -> YasinTradeStatisticsModel:

        statistics.updated_at = datetime.utcnow()

        self.db.commit()
        self.db.refresh(statistics)

        return statistics

    def get(
        self,
        statistics_id: int,
    ) -> Optional[YasinTradeStatisticsModel]:

        return (
            self.db.query(YasinTradeStatisticsModel)
            .filter(
                YasinTradeStatisticsModel.id == statistics_id
            )
            .first()
        )

    def get_market(
        self,
        market: str,
    ) -> Optional[YasinTradeStatisticsModel]:

        return (
            self.db.query(YasinTradeStatisticsModel)
            .filter(
                YasinTradeStatisticsModel.market == market
            )
            .first()
        )

    def get_all(self) -> List[YasinTradeStatisticsModel]:

        return (
            self.db.query(YasinTradeStatisticsModel)
            .order_by(
                YasinTradeStatisticsModel.market.asc()
            )
            .all()
        )

    def save(
        self,
        statistics: YasinTradeStatisticsModel,
    ) -> YasinTradeStatisticsModel:

        existing = self.get_market(
            statistics.market
        )

        if existing is None:
            return self.create(statistics)

        existing.total_trades = statistics.total_trades
        existing.winning_trades = statistics.winning_trades
        existing.losing_trades = statistics.losing_trades

        existing.win_rate = statistics.win_rate
        existing.loss_rate = statistics.loss_rate

        existing.average_rr = statistics.average_rr
        existing.average_profit = statistics.average_profit
        existing.average_loss = statistics.average_loss

        existing.profit_factor = statistics.profit_factor
        existing.expectancy = statistics.expectancy

        existing.max_drawdown = statistics.max_drawdown
        existing.current_drawdown = statistics.current_drawdown

        existing.net_profit = statistics.net_profit
        existing.gross_profit = statistics.gross_profit
        existing.gross_loss = statistics.gross_loss

        return self.update(existing)

    def delete(
        self,
        statistics_id: int,
    ) -> bool:

        statistics = self.get(statistics_id)

        if statistics is None:
            return False

        self.db.delete(statistics)
        self.db.commit()

        return True
