from typing import Optional

from app.yasin.signals.signal_schema import SignalMarket
from app.yasin.strategies.yasin_strategy_base import (
    YasinStrategyBase,
)


class GoldStrategy(YasinStrategyBase):
    """
    Yasin AI Gold (XAU/USD)

    Trendfolge-Strategie mit EMA + RSI + MACD.
    """

    MARKET = SignalMarket.GOLD
    SYMBOL = "XAUUSD"
    TIMEFRAME = "15m"

    def build_trade(
        self,
        candles: list,
        indicators: dict,
    ) -> Optional[dict]:

        close = candles[-1]["close"]

        ema50 = indicators["ema50"]
        ema200 = indicators["ema200"]
        rsi = indicators["rsi"]
        macd = indicators["macd"]
        macd_signal = indicators["macd_signal"]
        atr = indicators["atr"]

        if None in (
            ema50,
            ema200,
            rsi,
            macd,
            macd_signal,
            atr,
        ):
            return None

        # BUY
        if (
            ema50 > ema200
            and macd > macd_signal
            and 45 <= rsi <= 65
        ):
            return self.buy(
                entry=close,
                stop_loss=close - (atr * 1.5),
                tp1=close + (atr * 2),
                tp2=close + (atr * 3),
                tp3=close + (atr * 5),
            )

        # SELL
        if (
            ema50 < ema200
            and macd < macd_signal
            and 35 <= rsi <= 55
        ):
            return self.sell(
                entry=close,
                stop_loss=close + (atr * 1.5),
                tp1=close - (atr * 2),
                tp2=close - (atr * 3),
                tp3=close - (atr * 5),
            )

        return None
