from datetime import datetime

from sqlalchemy import (
    Column,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    String,
    Text,
)

from app.database.base import Base


class YasinMarketSnapshotModel(Base):
    """
    Speichert den vollständigen Marktzustand zum Zeitpunkt
    der Signalerstellung.

    Diese Daten dienen später für Backtesting,
    KI-Training, Fehleranalyse und Dashboard-Auswertungen.
    """

    __tablename__ = "yasin_market_snapshots"

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

    bid = Column(Float)
    ask = Column(Float)
    last_price = Column(Float)

    spread = Column(Float)

    open_price = Column(Float)
    high_price = Column(Float)
    low_price = Column(Float)
    close_price = Column(Float)

    previous_close = Column(Float)

    day_high = Column(Float)
    day_low = Column(Float)

    volatility = Column(Float)

    session = Column(
        String(30),
        nullable=True,
    )

    trend = Column(
        String(30),
        nullable=True,
    )

    orderbook_bias = Column(
        String(30),
        nullable=True,
    )

    liquidity_score = Column(Float)

    market_sentiment = Column(
        String(30),
        nullable=True,
    )

    snapshot_metadata = Column(
        Text,
        nullable=True,
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )
