from typing import Optional

from app.yasin.signals.signal_schema import SignalMarket
from app.yasin.strategies.yasin_strategy_base import (
    YasinStrategyBase,
)


class CustomStrategyBase(YasinStrategyBase):
    """
    Frei konfigurierbare Strategie.

    Jeder Custom-Slot erhält seine Parameter
    zur Laufzeit aus der Datenbank oder einer
    Konfigurationsdatei.
    """

    MARKET = SignalMarket.CUSTOM_1

    def __init__(
        self,
        market_provider,
        *,
        slot_name: str,
        symbol: str,
        timeframe: str,
        config: dict,
    ):
        super().__init__(market_provider)

        self.slot_name = slot_name
        self.SYMBOL = symbol
        self.TIMEFRAME = timeframe
        self.config = config

    def build_trade(
        self,
        candles: list,
        indicators: dict,
    ) -> Optional[dict]:

        close = float(candles[-1]["close"])

        ema50 = indicators.get("ema50")
        ema200 = indicators.get("ema200")
        rsi = indicators.get("rsi")
        macd = indicators.get("macd")
        macd_signal = indicators.get("macd_signal")
        atr = indicators.get("atr")

        if None in (
            ema50,
            ema200,
            rsi,
            macd,
            macd_signal,
            atr,
        ):
            return None

        buy_rsi_min = self.config.get("buy_rsi_min", 45)
        buy_rsi_max = self.config.get("buy_rsi_max", 65)

        sell_rsi_min = self.config.get("sell_rsi_min", 35)
        sell_rsi_max = self.config.get("sell_rsi_max", 55)

        sl_multiplier = self.config.get("sl_multiplier", 1.5)

        tp1_multiplier = self.config.get("tp1_multiplier", 2.0)
        tp2_multiplier = self.config.get("tp2_multiplier", 3.0)
        tp3_multiplier = self.config.get("tp3_multiplier", 5.0)

        if (
            ema50 > ema200
            and macd > macd_signal
            and buy_rsi_min <= rsi <= buy_rsi_max
        ):
            return self.buy(
                entry=close,
                stop_loss=close - atr * sl_multiplier,
                tp1=close + atr * tp1_multiplier,
                tp2=close + atr * tp2_multiplier,
                tp3=close + atr * tp3_multiplier,
            )

        if (
            ema50 < ema200
            and macd < macd_signal
            and sell_rsi_min <= rsi <= sell_rsi_max
        ):
            return self.sell(
                entry=close,
                stop_loss=close + atr * sl_multiplier,
                tp1=close - atr * tp1_multiplier,
                tp2=close - atr * tp2_multiplier,
                tp3=close - atr * tp3_multiplier,
            )

        return None
