from typing import Dict, List

from app.yasin.analysis.indicator_calculator import (
    IndicatorCalculator,
)
from app.yasin.analysis.indicator_engine import (
    IndicatorEngine,
)
from app.yasin.analysis.market_data_provider import (
    MarketDataProvider,
)


class YasinMarketAnalysisService:
    """
    Zentraler Marktanalyse-Service.

    Verantwortlich für:
    - Abrufen der Marktdaten
    - Berechnung der Indikatoren
    - Bewertung der Indikatoren
    - Bereitstellung einer vollständigen Analyse
    """

    DEFAULT_CANDLE_LIMIT = 300

    def __init__(
        self,
        market_provider: MarketDataProvider,
    ):
        self.market_provider = market_provider

        self.indicator_calculator = IndicatorCalculator()
        self.indicator_engine = IndicatorEngine()

    def analyze(
        self,
        symbol: str,
        timeframe: str = "15m",
    ) -> Dict:

        snapshot = self.market_provider.get_market_snapshot(
            symbol=symbol,
            timeframe=timeframe,
            candle_limit=self.DEFAULT_CANDLE_LIMIT,
        )

        candles = snapshot["candles"]

        indicators = self.indicator_calculator.calculate_all(
            candles
        )

        confirmations = (
            self.indicator_engine.confirmations(
                indicators
            )
        )

        results = self.indicator_engine.evaluate(
            indicators
        )

        return {
            "symbol": symbol,
            "timeframe": timeframe,
            "snapshot": snapshot,
            "candles": candles,
            "indicators": indicators,
            "confirmations": confirmations,
            "indicator_results": results,
        }

    def analyze_many(
        self,
        symbols: List[str],
        timeframe: str = "15m",
    ) -> List[Dict]:

        analyses = []

        for symbol in symbols:
            analyses.append(
                self.analyze(
                    symbol=symbol,
                    timeframe=timeframe,
                )
            )

        return analyses

    def latest_price(
        self,
        symbol: str,
    ) -> float:

        return self.market_provider.get_latest_price(
            symbol
        )
