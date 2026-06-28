from typing import Optional

from app.yasin.signals.signal_schema import SignalMarket
from app.yasin.strategies.yasin_strategy_base import (
    YasinStrategyBase,
)


class CryptoStrategy(YasinStrategyBase):
    """
    Yasin AI Crypto Strategie.

    Optimiert für volatile Kryptowährungen
    wie BTC, ETH, SOL usw.
    """

    MARKET = SignalMarket.CRYPTO
    SYMBOL = "BTCUSDT"
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
        volume = indicators["volume"]
        avg_volume = indicators["avg_volume"]

        if None in (
            ema50,
            ema200,
            rsi,
            macd,
            macd_signal,
            atr,
            adx,
            volume,
            avg_volume,
        ):
            return None

        trend_confirmed = adx >= 25
        volume_confirmed = volume >= avg_volume

        # BUY
        if (
            trend_confirmed
            and volume_confirmed
            and ema50 > ema200
            and macd > macd_signal
            and 45 <= rsi <= 70
        ):
            return self.buy(
                entry=close,
                stop_loss=close - (atr * 2.0),
                tp1=close + (atr * 2.5),
                tp2=close + (atr * 4.0),
                tp3=close + (atr * 6.0),
            )

        # SELL
        if (
            trend_confirmed
            and volume_confirmed
            and ema50 < ema200
            and macd < macd_signal
            and 30 <= rsi <= 55
        ):
            return self.sell(
                entry=close,
                stop_loss=close + (atr * 2.0),
                tp1=close - (atr * 2.5),
                tp2=close - (atr * 4.0),
                tp3=close - (atr * 6.0),
            )

        return None
