from typing import Optional

from app.yasin.analysis.indicator_engine import IndicatorEngine
from app.yasin.signals.signal_generator import SignalGenerator
from app.yasin.signals.signal_schema import (
    SignalDirection,
    SignalMarket,
    YasinSignal,
)


class MarketAnalyzer:
    """
    Zentrale Analyse-Pipeline für Yasin AI.

    Diese Klasse verbindet:
    - vorbereitete Marktdaten
    - technische Indikatoren
    - Signalqualität
    - Signal-Erstellung
    """

    def __init__(self):
        self.indicator_engine = IndicatorEngine()
        self.signal_generator = SignalGenerator()

    def analyze_market(
        self,
        *,
        market: SignalMarket,
        symbol: str,
        direction: SignalDirection,
        market_data: dict,
        entry: float,
        stop_loss: float,
        tp1: float,
        tp2: float,
        tp3: float,
    ) -> Optional[YasinSignal]:

        confirmations = self.indicator_engine.confirmations(market_data)

        trend_strength = self._calculate_trend_strength(market_data)
        volatility_score = self._calculate_volatility_score(market_data)

        ai_analysis = self._build_yasin_analysis(
            symbol=symbol,
            direction=direction,
            confirmations=confirmations,
            trend_strength=trend_strength,
            volatility_score=volatility_score,
        )

        return self.signal_generator.create_signal(
            market=market,
            symbol=symbol,
            direction=direction,
            entry=entry,
            stop_loss=stop_loss,
            tp1=tp1,
            tp2=tp2,
            tp3=tp3,
            confirmations=confirmations,
            trend_strength=trend_strength,
            volatility_score=volatility_score,
            ai_analysis=ai_analysis,
        )

    def _calculate_trend_strength(self, market_data: dict) -> float:
        adx = market_data.get("adx", 0)

        if adx >= 35:
            return 1.0

        if adx >= 25:
            return 0.75

        if adx >= 20:
            return 0.5

        return 0.25

    def _calculate_volatility_score(self, market_data: dict) -> float:
        atr = market_data.get("atr", 0)
        atr_average = market_data.get("atr_average", atr)

        if atr_average == 0:
            return 0.0

        ratio = atr / atr_average
        return round(min(max(ratio, 0.0), 1.0), 2)

    def _build_yasin_analysis(
        self,
        *,
        symbol: str,
        direction: SignalDirection,
        confirmations: dict,
        trend_strength: float,
        volatility_score: float,
    ) -> str:

        passed = [
            name for name, value in confirmations.items()
            if value
        ]

        failed = [
            name for name, value in confirmations.items()
            if not value
        ]

        return (
            f"Yasin AI Analyse für {symbol}: "
            f"Richtung {direction.value}. "
            f"Bestätigte Faktoren: {', '.join(passed) if passed else 'keine'}. "
            f"Nicht bestätigte Faktoren: {', '.join(failed) if failed else 'keine'}. "
            f"Trendstärke: {trend_strength}. "
            f"Volatilitätsbewertung: {volatility_score}. "
            f"Signal wird nur bei ausreichender Gesamtqualität freigegeben."
        )
