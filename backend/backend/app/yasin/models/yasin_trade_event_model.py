from datetime import datetime
from enum import Enum

from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Text,
)

from app.database.base import Base


class TradeEventType(str, Enum):
    SIGNAL_CREATED = "SIGNAL_CREATED"
    SIGNAL_APPROVED = "SIGNAL_APPROVED"
    SIGNAL_REJECTED = "SIGNAL_REJECTED"

    TELEGRAM_SENT = "TELEGRAM_SENT"

    TRADE_OPENED = "TRADE_OPENED"

    TP1_REACHED = "TP1_REACHED"
    TP2_REACHED = "TP2_REACHED"
    TP3_REACHED = "TP3_REACHED"

    STOP_LOSS = "STOP_LOSS"

    BREAK_EVEN = "BREAK_EVEN"

    TRAILING_STOP = "TRAILING_STOP"

    TRADE_CLOSED = "TRADE_CLOSED"

    ERROR = "ERROR"


class YasinTradeEventModel(Base):
    """
    Vollständiges Event-Log jedes Trades.

    Jeder Statuswechsel eines Signals wird dauerhaft
    gespeichert und ist später nachvollziehbar.
    """

    __tablename__ = "yasin_trade_events"

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

    event_type = Column(
        String(50),
        nullable=False,
        index=True,
    )

    title = Column(
        String(255),
        nullable=False,
    )

    description = Column(
        Text,
        nullable=True,
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )
