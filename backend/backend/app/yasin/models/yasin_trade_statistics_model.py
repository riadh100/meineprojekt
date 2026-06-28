from datetime import datetime

from sqlalchemy import (
    Column,
    DateTime,
    Float,
    Integer,
    String,
)

from app.database.base import Base


class YasinTradeStatisticsModel(Base):
    """
    Aggregierte Performance-Statistiken von Yasin AI.

    Diese Tabelle enthält Snapshots der Performance und
    wird regelmäßig durch den Statistics-Service aktualisiert.
    """

    __tablename__ = "yasin_trade_statistics"

    id = Column(Integer, primary_key=True, index=True)

    market = Column(
        String(30),
        nullable=False,
        index=True,
    )

    total_trades = Column(
        Integer,
        default=0,
        nullable=False,
    )

    winning_trades = Column(
        Integer,
        default=0,
        nullable=False,
    )

    losing_trades = Column(
        Integer,
        default=0,
        nullable=False,
    )

    win_rate = Column(
        Float,
        default=0.0,
        nullable=False,
    )

    loss_rate = Column(
        Float,
        default=0.0,
        nullable=False,
    )

    average_rr = Column(
        Float,
        default=0.0,
        nullable=False,
    )

    average_profit = Column(
        Float,
        default=0.0,
        nullable=False,
    )

    average_loss = Column(
        Float,
        default=0.0,
        nullable=False,
    )

    profit_factor = Column(
        Float,
        default=0.0,
        nullable=False,
    )

    expectancy = Column(
        Float,
        default=0.0,
        nullable=False,
    )

    max_drawdown = Column(
        Float,
        default=0.0,
        nullable=False,
    )

    current_drawdown = Column(
        Float,
        default=0.0,
        nullable=False,
    )

    net_profit = Column(
        Float,
        default=0.0,
        nullable=False,
    )

    gross_profit = Column(
        Float,
        default=0.0,
        nullable=False,
    )

    gross_loss = Column(
        Float,
        default=0.0,
        nullable=False,
    )

    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False,
    )
