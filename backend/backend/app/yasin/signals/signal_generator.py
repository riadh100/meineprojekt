from datetime import datetime
from typing import Dict, Optional

from .signal_schema import (
    SignalDirection,
    SignalMarket,
    YasinSignal,
)
from .signal_quality_engine import SignalQualityEngine


class SignalGenerator:
    """
    Erstellt standardisierte Yasin-Signale.

    Die eigentliche Marktanalyse (Indikatoren, KI, Orderflow usw.)
    erfolgt in den Analyse-Modulen. Dieser Generator übernimmt
    ausschließlich die Validierung, Qualitätsbewertung und Erstellung
    des Signal-Objekts.
    """

    def __init__(self):
        self.quality_engine = SignalQualityEngine()

    @staticmethod
    def calculate_rr(
        entry: float,
        stop_loss: float,
        take_profit: float,
    ) -> float:
        risk = abs(entry - stop_loss)
        reward = abs(take_profit - entry)

        if risk == 0:
            return 0.0

        return round(reward / risk, 2)

    def create_signal(
        self,
        *,
        market: SignalMarket,
        symbol: str,
        direction: SignalDirection,
        entry: float,
        stop_loss: float,
        tp1: float,
        tp2: float,
        tp3: float,
        confirmations: Dict[str, bool],
        trend_strength: float,
        volatility_score: float,
        ai_analysis: str,
    ) -> Optional[YasinSignal]:

        rr = self.calculate_rr(
            entry=entry,
            stop_loss=stop_loss,
            take_profit=tp3,
        )

        report = self.quality_engine.build_quality_report(
            confirmations=confirmations,
            risk_reward_ratio=rr,
            trend_strength=trend_strength,
            volatility_score=volatility_score,
        )

        signal = YasinSignal(
            market=market,
            symbol=symbol,
            direction=direction,
            entry=entry,
            sl=stop_loss,
            tp1=tp1,
            tp2=tp2,
            tp3=tp3,
            risk_reward_ratio=rr,
            quality_score=report["quality_score"],
            yasin_analysis=ai_analysis,
            created_at=datetime.utcnow(),
            is_approved=report["approved"],
            status="APPROVED" if report["approved"] else "REJECTED",
        )

        if not signal.is_approved:
            return None

        return signal
