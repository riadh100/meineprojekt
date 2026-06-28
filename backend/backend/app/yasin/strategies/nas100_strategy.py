from typing import Optional

from app.yasin.signals.signal_schema import SignalMarket
from app.yasin.strategies.yasin_strategy_base import (
    YasinStrategyBase,
)


class Nas100Strategy(YasinStrategyBase):
    """
    Yasin AI NAS100 Strategie.

    Momentum-/Trendfolge-Strategie mit EMA, MACD,
    RSI und ATR-basierten Zielzonen.
    """

    MARKET = SignalMarket.NAS100
    SYMBOL = "NAS100"
    TIMEFRAME = "15m"

    def build_trade(
        self,
        candles: list,
        indicators: dict,
    ) -> Optional[dict]:

        close = float(candles[-1]["close"])

        ema50 = indicators["ema50"]
        ema200 = indicators["ema200"]
        rsi = indicators["rsi"]
        macd = indicators["macd"]
        macd_signal = indicators["macd_signal"]
        atr = indicators["atr"]
        volume = indicators["volume"]
        avg_volume = indicators["avg_volume"]

        if None in (
            ema50,
            ema200,
            rsi,
            macd,
            macd_signal,
            atr,
            volume,
            avg_volume,
        ):
            return None

        volume_confirmed = volume >= avg_volume

        # BUY
        if (
            ema50 > ema200
            and macd > macd_signal
            and 48 <= rsi <= 68
            and volume_confirmed
        ):
            return self.buy(
                entry=close,
                stop_loss=close - (atr * 1.8),
                tp1=close + (atr * 2.2),
                tp2=close + (atr * 3.4),
                tp3=close + (atr * 5.2),
            )

        # SELL
        if (
            ema50 < ema200
            and macd < macd_signal
            and 32 <= rsi <= 52
            and volume_confirmed
        ):
            return self.sell(
                entry=close,
                stop_loss=close + (atr * 1.8),
                tp1=close - (atr * 2.2),
                tp2=close - (atr * 3.4),
                tp3=close - (atr * 5.2),
            )

        return None
