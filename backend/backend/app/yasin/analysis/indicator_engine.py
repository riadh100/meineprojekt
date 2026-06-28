from dataclasses import dataclass
from typing import Dict, List


@dataclass
class IndicatorResult:
    name: str
    passed: bool
    value: float | None = None
    message: str = ""


class IndicatorEngine:
    """
    Führt alle technischen Indikatoren aus und erzeugt
    eine standardisierte Liste von Bestätigungen.

    Diese Klasse berechnet bewusst keine Candle- oder
    Marktdaten selbst. Sie arbeitet ausschließlich auf
    bereits vorbereiteten Marktinformationen.
    """

    def evaluate(
        self,
        market_data: dict,
    ) -> List[IndicatorResult]:

        results = []

        results.append(self._ema_trend(market_data))
        results.append(self._rsi(market_data))
        results.append(self._macd(market_data))
        results.append(self._adx(market_data))
        results.append(self._atr(market_data))
        results.append(self._volume(market_data))

        return results

    def confirmations(
        self,
        market_data: dict,
    ) -> Dict[str, bool]:

        return {
            result.name: result.passed
            for result in self.evaluate(market_data)
        }

    def _ema_trend(self, data: dict) -> IndicatorResult:

        ema50 = data.get("ema50")
        ema200 = data.get("ema200")

        passed = (
            ema50 is not None
            and ema200 is not None
            and ema50 > ema200
        )

        return IndicatorResult(
            name="EMA Trend",
            passed=passed,
            value=ema50,
            message="EMA50 über EMA200",
        )

    def _rsi(self, data: dict) -> IndicatorResult:

        rsi = data.get("rsi")

        passed = (
            rsi is not None
            and 40 <= rsi <= 65
        )

        return IndicatorResult(
            name="RSI",
            passed=passed,
            value=rsi,
            message="RSI im Trendbereich",
        )

    def _macd(self, data: dict) -> IndicatorResult:

        macd = data.get("macd")
        signal = data.get("macd_signal")

        passed = (
            macd is not None
            and signal is not None
            and macd > signal
        )

        return IndicatorResult(
            name="MACD",
            passed=passed,
            value=macd,
            message="Bullisches MACD-Signal",
        )

    def _adx(self, data: dict) -> IndicatorResult:

        adx = data.get("adx")

        passed = (
            adx is not None
            and adx >= 25
        )

        return IndicatorResult(
            name="ADX",
            passed=passed,
            value=adx,
            message="Trend ausreichend stark",
        )

    def _atr(self, data: dict) -> IndicatorResult:

        atr = data.get("atr")

        passed = atr is not None and atr > 0

        return IndicatorResult(
            name="ATR",
            passed=passed,
            value=atr,
            message="Volatilität ausreichend",
        )

    def _volume(self, data: dict) -> IndicatorResult:

        volume = data.get("volume")
        avg_volume = data.get("avg_volume")

        passed = (
            volume is not None
            and avg_volume is not None
            and volume >= avg_volume
        )

        return IndicatorResult(
            name="Volume",
            passed=passed,
            value=volume,
            message="Volumen bestätigt Bewegung",
        )
