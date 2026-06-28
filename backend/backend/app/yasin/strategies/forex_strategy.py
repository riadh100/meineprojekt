from typing import Optional

from app.yasin.signals.signal_schema import SignalMarket
from app.yasin.strategies.yasin_strategy_base import (
    YasinStrategyBase,
)


class ForexStrategy(YasinStrategyBase):
    """
    Yasin AI Forex Strategie.

    Geeignet für Major- und Minor-Währungspaare.
    Trendfolge mit EMA, MACD, RSI, ADX und ATR.
    """

    MARKET = SignalMarket.FOREX
    SYMBOL = "EURUSD"
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
        adx = indicators["adx"]

        if None in (
            ema50,
            ema200,
            rsi,
            macd,
            macd_signal,
            atr,
            adx,
        ):
            return None

        trend_confirmed = adx >= 25

        # BUY
        if (
            trend_confirmed
            and ema50 > ema200
            and macd > macd_signal
            and 45 <= rsi <= 65
        ):
            return self.buy(
                entry=close,
                stop_loss=close - (atr * 1.5),
                tp1=close + (atr * 2.0),
                tp2=close + (atr * 3.0),
                tp3=close + (atr * 4.5),
            )

        # SELL
        if (
            trend_confirmed
            and ema50 < ema200
            and macd < macd_signal
            and 35 <= rsi <= 55
        ):
            return self.sell(
                entry=close,
                stop_loss=close + (atr * 1.5),
                tp1=close - (atr * 2.0),
                tp2=close - (atr * 3.0),
                tp3=close - (atr * 4.5),
            )

        return None
