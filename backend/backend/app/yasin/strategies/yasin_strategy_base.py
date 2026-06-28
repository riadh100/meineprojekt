from abc import ABC, abstractmethod
from typing import Optional

from app.yasin.analysis.market_analyzer import MarketAnalyzer
from app.yasin.analysis.market_data_provider import MarketDataProvider
from app.yasin.analysis.indicator_calculator import IndicatorCalculator
from app.yasin.signals.signal_schema import (
    SignalDirection,
    SignalMarket,
    YasinSignal,
)


class YasinStrategyBase(ABC):
    """
    Basisklasse aller Yasin-Strategien.

    Jede Strategie (Gold, NAS100, Forex, Crypto usw.)
    implementiert lediglich ihre Handelslogik.
    """

    MARKET: SignalMarket
    SYMBOL: str
    TIMEFRAME: str = "15m"

    def __init__(
        self,
        market_provider: MarketDataProvider,
    ):
        self.market_provider = market_provider
        self.indicator_calculator = IndicatorCalculator()
        self.market_analyzer = MarketAnalyzer()

    def analyze(self) -> Optional[YasinSignal]:
        """
        Einstiegspunkt einer Strategie.
        """

        snapshot = self.market_provider.get_market_snapshot(
            symbol=self.SYMBOL,
            timeframe=self.TIMEFRAME,
        )

        candles = snapshot["candles"]

        if not candles:
            return None

        indicators = self.indicator_calculator.calculate_all(candles)

        trade = self.build_trade(
            candles=candles,
            indicators=indicators,
        )

        if trade is None:
            return None

        return self.market_analyzer.analyze_market(
            market=self.MARKET,
            symbol=self.SYMBOL,
            direction=trade["direction"],
            market_data=indicators,
            entry=trade["entry"],
            stop_loss=trade["stop_loss"],
            tp1=trade["tp1"],
            tp2=trade["tp2"],
            tp3=trade["tp3"],
        )

    @abstractmethod
    def build_trade(
        self,
        candles: list,
        indicators: dict,
    ) -> Optional[dict]:
        """
        Muss von jeder Strategie implementiert werden.

        Rückgabe:

        {
            "direction": SignalDirection.BUY,
            "entry": ...,
            "stop_loss": ...,
            "tp1": ...,
            "tp2": ...,
            "tp3": ...
        }
        """
        raise NotImplementedError

    @staticmethod
    def buy(
        entry: float,
        stop_loss: float,
        tp1: float,
        tp2: float,
        tp3: float,
    ) -> dict:
        return {
            "direction": SignalDirection.BUY,
            "entry": entry,
            "stop_loss": stop_loss,
            "tp1": tp1,
            "tp2": tp2,
            "tp3": tp3,
        }

    @staticmethod
    def sell(
        entry: float,
        stop_loss: float,
        tp1: float,
        tp2: float,
        tp3: float,
    ) -> dict:
        return {
            "direction": SignalDirection.SELL,
            "entry": entry,
            "stop_loss": stop_loss,
            "tp1": tp1,
            "tp2": tp2,
            "tp3": tp3,
        }
