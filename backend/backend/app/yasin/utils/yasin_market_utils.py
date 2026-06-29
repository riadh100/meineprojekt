from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass(frozen=True)
class IndicatorResult:
    name: str
    passed: bool
    value: Optional[float] = None
    message: str = ""


class IndicatorEngine:
    """
    Führt technische Indikator-Prüfungen aus und erzeugt
    eine standardisierte Liste von Bestätigungen.

    Die Klasse berechnet keine Candle- oder Marktdaten selbst.
    Sie arbeitet ausschließlich mit bereits vorbereiteten
    Marktinformationen.
    """

    def evaluate(self, market_data: Dict[str, Any]) -> List[IndicatorResult]:
        if not isinstance(market_data, dict):
            return []

        return [
            self._ema_trend(market_data),
            self._rsi(market_data),
            self._macd(market_data),
            self._adx(market_data),
            self._atr(market_data),
            self._volume(market_data),
        ]

    def confirmations(self, market_data: Dict[str, Any]) -> Dict[str, bool]:
        return {
            result.name: result.passed
            for result in self.evaluate(market_data)
        }

    def _ema_trend(self, data: Dict[str, Any]) -> IndicatorResult:
        ema50 = self._to_float(data.get("ema50"))
        ema200 = self._to_float(data.get("ema200"))

        passed = ema50 is not None and ema200 is not None and ema50 > ema200

        return IndicatorResult(
            name="EMA Trend",
            passed=passed,
            value=ema50,
            message="EMA50 über EMA200" if passed else "EMA-Trend nicht bestätigt",
        )

    def _rsi(self, data: Dict[str, Any]) -> IndicatorResult:
        rsi = self._to_float(data.get("rsi"))

        passed = rsi is not None and 40 <= rsi <= 65

        return IndicatorResult(
            name="RSI",
            passed=passed,
            value=rsi,
            message="RSI im Trendbereich" if passed else "RSI außerhalb des Trendbereichs",
        )

    def _macd(self, data: Dict[str, Any]) -> IndicatorResult:
        macd = self._to_float(data.get("macd"))
        signal = self._to_float(data.get("macd_signal"))

        passed = macd is not None and signal is not None and macd > signal

        return IndicatorResult(
            name="MACD",
            passed=passed,
            value=macd,
            message="Bullisches MACD-Signal" if passed else "MACD-Signal nicht bullisch",
        )

    def _adx(self, data: Dict[str, Any]) -> IndicatorResult:
        adx = self._to_float(data.get("adx"))

        passed = adx is not None and adx >= 25

        return IndicatorResult(
            name="ADX",
            passed=passed,
            value=adx,
            message="Trend ausreichend stark" if passed else "Trend zu schwach",
        )

    def _atr(self, data: Dict[str, Any]) -> IndicatorResult:
        atr = self._to_float(data.get("atr"))

        passed = atr is not None and atr > 0

        return IndicatorResult(
            name="ATR",
            passed=passed,
            value=atr,
            message="Volatilität ausreichend" if passed else "Volatilität nicht ausreichend",
        )

    def _volume(self, data: Dict[str, Any]) -> IndicatorResult:
        volume = self._to_float(data.get("volume"))
        avg_volume = self._to_float(data.get("avg_volume"))

        passed = volume is not None and avg_volume is not None and volume >= avg_volume

        return IndicatorResult(
            name="Volume",
            passed=passed,
            value=volume,
            message="Volumen bestätigt Bewegung" if passed else "Volumen bestätigt Bewegung nicht",
        )

    @staticmethod
    def _to_float(value: Any) -> Optional[float]:
        if value is None:
            return None

        try:
            return float(value)
        except (TypeError, ValueError):
            return None
