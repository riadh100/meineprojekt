from app.yasin.signals.signal_schema import (
    SignalDirection,
    YasinSignal,
)
from app.yasin.signals.signal_repository import SignalRepository
from app.yasin.telegram.yasin_telegram_sender import YasinTelegramSender


class TradeMonitor:
    """
    Überwacht offene Yasin-Trades und sendet automatische Updates.
    """

    def __init__(
        self,
        repository: SignalRepository,
        telegram_sender: YasinTelegramSender,
    ):
        self.repository = repository
        self.telegram_sender = telegram_sender

    def check_open_trades(self, prices: dict) -> None:
        for signal in self.repository.open_trades():
            current_price = prices.get(signal.symbol)

            if current_price is None:
                continue

            self._check_signal(signal, current_price)

    def _check_signal(
        self,
        signal: YasinSignal,
        current_price: float,
    ) -> None:

        if signal.direction == SignalDirection.BUY:
            self._check_buy(signal, current_price)
        else:
            self._check_sell(signal, current_price)

    def _check_buy(
        self,
        signal: YasinSignal,
        price: float,
    ) -> None:

        if price <= signal.stop_loss:
            self.telegram_sender.send_stop_loss(signal)
            self.repository.close_signal(signal, "STOP_LOSS")
            self.telegram_sender.send_trade_closed(signal)
            return

        if price >= signal.take_profit_3:
            self.telegram_sender.send_tp3(signal)
            self.repository.close_signal(signal, "TP3")
            self.telegram_sender.send_trade_closed(signal)
            return

        if price >= signal.take_profit_2:
            self.telegram_sender.send_tp2(signal)
            signal.status = "TP2_REACHED"
            return

        if price >= signal.take_profit_1:
            self.telegram_sender.send_tp1(signal)
            signal.status = "TP1_REACHED"

    def _check_sell(
        self,
        signal: YasinSignal,
        price: float,
    ) -> None:

        if price >= signal.stop_loss:
            self.telegram_sender.send_stop_loss(signal)
            self.repository.close_signal(signal, "STOP_LOSS")
            self.telegram_sender.send_trade_closed(signal)
            return

        if price <= signal.take_profit_3:
            self.telegram_sender.send_tp3(signal)
            self.repository.close_signal(signal, "TP3")
            self.telegram_sender.send_trade_closed(signal)
            return

        if price <= signal.take_profit_2:
            self.telegram_sender.send_tp2(signal)
            signal.status = "TP2_REACHED"
            return

        if price <= signal.take_profit_1:
            self.telegram_sender.send_tp1(signal)
            signal.status = "TP1_REACHED"
