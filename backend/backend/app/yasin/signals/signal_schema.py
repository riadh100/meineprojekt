from datetime import datetime
from enum import Enum
from pydantic import BaseModel, Field
from typing import Optional


class SignalDirection(str, Enum):
    BUY = "BUY"
    SELL = "SELL"


class SignalMarket(str, Enum):
    GOLD = "GOLD"
    NAS100 = "NAS100"
    FOREX = "FOREX"
    CRYPTO = "CRYPTO"
    CUSTOM_1 = "CUSTOM_1"
    CUSTOM_2 = "CUSTOM_2"
    CUSTOM_3 = "CUSTOM_3"
    CUSTOM_4 = "CUSTOM_4"


class YasinSignal(BaseModel):
    market: SignalMarket
    symbol: str

    direction: SignalDirection

    entry: float
    stop_loss: float = Field(..., alias="sl")

    take_profit_1: float = Field(..., alias="tp1")
    take_profit_2: float = Field(..., alias="tp2")
    take_profit_3: float = Field(..., alias="tp3")

    risk_reward_ratio: float
    quality_score: float

    yasin_analysis: str

    created_at: datetime = Field(default_factory=datetime.utcnow)

    is_approved: bool = False
    is_sent_to_telegram: bool = False
    is_closed: bool = False

    status: Optional[str] = "PENDING"
