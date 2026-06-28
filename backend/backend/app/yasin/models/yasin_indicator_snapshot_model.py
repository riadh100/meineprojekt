from datetime import datetime

from sqlalchemy import (
    Column,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    String,
)

from app.database.base import Base


class YasinIndicatorSnapshotModel(Base):
    """
    Speichert alle berechneten Indikatoren zum Zeitpunkt
    der Signalerstellung.

    Dadurch kann jedes Signal später vollständig
    nachvollzogen und für Analysen oder Backtesting
    verwendet werden.
    """

    __tablename__ = "yasin_indicator_snapshots"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    signal_id = Column(
        Integer,
        ForeignKey("yasin_signals.id"),
        nullable=False,
        index=True,
    )

    symbol = Column(
        String(30),
        nullable=False,
        index=True,
    )

    timeframe = Column(
        String(20),
        nullable=False,
    )

    ema50 = Column(Float)
    ema200 = Column(Float)

    sma20 = Column(Float)
    sma50 = Column(Float)
    sma200 = Column(Float)

    rsi = Column(Float)

    macd = Column(Float)
    macd_signal = Column(Float)
    macd_histogram = Column(Float)

    atr = Column(Float)
    atr_average = Column(Float)

    adx = Column(Float)

    bollinger_upper = Column(Float)
    bollinger_middle = Column(Float)
    bollinger_lower = Column(Float)

    stochastic_k = Column(Float)
    stochastic_d = Column(Float)

    vwap = Column(Float)

    volume = Column(Float)
    average_volume = Column(Float)

    spread = Column(Float)

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )
