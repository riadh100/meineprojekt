from datetime import datetime

from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Float,
    Integer,
    String,
)

from app.database.base import Base


class YasinStrategyConfigModel(Base):
    """
    Konfiguration aller Yasin-Strategien.

    Jede Strategie kann vollständig über die Datenbank
    konfiguriert werden, ohne den Code zu ändern.
    """

    __tablename__ = "yasin_strategy_configs"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    name = Column(
        String(100),
        nullable=False,
        unique=True,
    )

    market = Column(
        String(30),
        nullable=False,
        index=True,
    )

    symbol = Column(
        String(30),
        nullable=False,
    )

    timeframe = Column(
        String(20),
        default="15m",
        nullable=False,
    )

    enabled = Column(
        Boolean,
        default=True,
        nullable=False,
    )

    minimum_quality = Column(
        Float,
        default=75.0,
        nullable=False,
    )

    buy_rsi_min = Column(
        Float,
        default=45.0,
        nullable=False,
    )

    buy_rsi_max = Column(
        Float,
        default=65.0,
        nullable=False,
    )

    sell_rsi_min = Column(
        Float,
        default=35.0,
        nullable=False,
    )

    sell_rsi_max = Column(
        Float,
        default=55.0,
        nullable=False,
    )

    minimum_adx = Column(
        Float,
        default=25.0,
        nullable=False,
    )

    stop_loss_multiplier = Column(
        Float,
        default=1.5,
        nullable=False,
    )

    tp1_multiplier = Column(
        Float,
        default=2.0,
        nullable=False,
    )

    tp2_multiplier = Column(
        Float,
        default=3.0,
        nullable=False,
    )

    tp3_multiplier = Column(
        Float,
        default=5.0,
        nullable=False,
    )

    risk_per_trade = Column(
        Float,
        default=1.0,
        nullable=False,
    )

    max_open_positions = Column(
        Integer,
        default=1,
        nullable=False,
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
