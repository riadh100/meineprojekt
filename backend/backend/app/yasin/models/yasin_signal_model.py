from datetime import datetime

from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Float,
    Integer,
    String,
    Text,
)

from app.database.base import Base


class YasinSignalModel(Base):
    """
    Persistentes Signalmodell für Yasin AI.
    """

    __tablename__ = "yasin_signals"

    id = Column(Integer, primary_key=True, index=True)

    market = Column(String(30), nullable=False)
    symbol = Column(String(30), nullable=False)

    direction = Column(String(10), nullable=False)

    entry = Column(Float, nullable=False)

    stop_loss = Column(Float, nullable=False)

    take_profit_1 = Column(Float, nullable=False)
    take_profit_2 = Column(Float, nullable=False)
    take_profit_3 = Column(Float, nullable=False)

    risk_reward_ratio = Column(Float, nullable=False)

    quality_score = Column(Float, nullable=False)

    yasin_analysis = Column(Text, nullable=False)

    status = Column(
        String(30),
        default="PENDING",
        nullable=False,
    )

    is_approved = Column(
        Boolean,
        default=False,
        nullable=False,
    )

    is_sent_to_telegram = Column(
        Boolean,
        default=False,
        nullable=False,
    )

    is_closed = Column(
        Boolean,
        default=False,
        nullable=False,
    )

    opened_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )

    closed_at = Column(
        DateTime,
        nullable=True,
    )

    close_price = Column(
        Float,
        nullable=True,
    )

    realized_profit = Column(
        Float,
        nullable=True,
    )

    realized_profit_percent = Column(
        Float,
        nullable=True,
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )

    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False,
    )
