from typing import List, Dict, Optional


class IndicatorCalculator:
    """
    Berechnet technische Indikatoren aus Candle-Daten.

    Erwartetes Candle-Format:
    {
        "open": float,
        "high": float,
        "low": float,
        "close": float,
        "volume": float
    }
    """

    def calculate_all(self, candles: List[Dict]) -> Dict:
        closes = self._values(candles, "close")
        highs = self._values(candles, "high")
        lows = self._values(candles, "low")
        volumes = self._values(candles, "volume")

        return {
            "ema50": self.ema(closes, 50),
            "ema200": self.ema(closes, 200),
            "rsi": self.rsi(closes),
            "macd": self.macd(closes)["macd"],
            "macd_signal": self.macd(closes)["signal"],
            "atr": self.atr(highs, lows, closes),
            "atr_average": self.atr_average(highs, lows, closes),
            "adx": self.adx(highs, lows, closes),
            "volume": volumes[-1] if volumes else None,
            "avg_volume": self.sma(volumes, 20),
        }

    def sma(self, values: List[float], period: int) -> Optional[float]:
        if len(values) < period:
            return None
        return round(sum(values[-period:]) / period, 5)

    def ema(self, values: List[float], period: int) -> Optional[float]:
        if len(values) < period:
            return None

        multiplier = 2 / (period + 1)
        ema_value = sum(values[:period]) / period

        for price in values[period:]:
            ema_value = (price - ema_value) * multiplier + ema_value

        return round(ema_value, 5)

    def rsi(self, closes: List[float], period: int = 14) -> Optional[float]:
        if len(closes) <= period:
            return None

        gains = []
        losses = []

        for index in range(1, len(closes)):
            change = closes[index] - closes[index - 1]
            gains.append(max(change, 0))
            losses.append(abs(min(change, 0)))

        avg_gain = sum(gains[-period:]) / period
        avg_loss = sum(losses[-period:]) / period

        if avg_loss == 0:
            return 100.0

        rs = avg_gain / avg_loss
        return round(100 - (100 / (1 + rs)), 2)

    def macd(self, closes: List[float]) -> Dict[str, Optional[float]]:
        ema12 = self.ema(closes, 12)
        ema26 = self.ema(closes, 26)

        if ema12 is None or ema26 is None:
            return {"macd": None, "signal": None}

        macd_line = ema12 - ema26
        signal_line = self.ema([macd_line] * 35, 9)

        return {
            "macd": round(macd_line, 5),
            "signal": signal_line,
        }

    def atr(
        self,
        highs: List[float],
        lows: List[float],
        closes: List[float],
        period: int = 14,
    ) -> Optional[float]:
        true_ranges = self._true_ranges(highs, lows, closes)

        if len(true_ranges) < period:
            return None

        return round(sum(true_ranges[-period:]) / period, 5)

    def atr_average(
        self,
        highs: List[float],
        lows: List[float],
        closes: List[float],
        period: int = 50,
    ) -> Optional[float]:
        true_ranges = self._true_ranges(highs, lows, closes)

        if len(true_ranges) < period:
            return None

        return round(sum(true_ranges[-period:]) / period, 5)

    def adx(
        self,
        highs: List[float],
        lows: List[float],
        closes: List[float],
        period: int = 14,
    ) -> Optional[float]:
        if len(highs) <= period or len(lows) <= period:
            return None

        trend_range = max(highs[-period:]) - min(lows[-period:])
        atr_value = self.atr(highs, lows, closes, period)

        if not atr_value:
            return None

        return round(min((trend_range / atr_value) * 10, 100), 2)

    def _true_ranges(
        self,
        highs: List[float],
        lows: List[float],
        closes: List[float],
    ) -> List[float]:
        true_ranges = []

        for index in range(1, len(highs)):
            high_low = highs[index] - lows[index]
            high_close = abs(highs[index] - closes[index - 1])
            low_close = abs(lows[index] - closes[index - 1])

            true_ranges.append(max(high_low, high_close, low_close))

        return true_ranges

    def _values(self, candles: List[Dict], key: str) -> List[float]:
        return [
            float(candle[key])
            for candle in candles
            if key in candle and candle[key] is not None
        ]
