from typing import List, Optional

from app.yasin.signals.signal_schema import YasinSignal


class SignalRepository:
    """
    Temporäres Repository für Yasin-Signale.

    Kann später direkt durch ein echtes Datenbank-Repository
    ersetzt werden, ohne die restliche Yasin-Architektur zu ändern.
    """

    def __init__(self):
        self._signals: List[YasinSignal] = []

    def save(self, signal: YasinSignal) -> YasinSignal:
        self._signals.append(signal)
        return signal

    def all(self) -> List[YasinSignal]:
        return self._signals

    def approved(self) -> List[YasinSignal]:
        return [
            signal for signal in self._signals
            if signal.is_approved
        ]

    def open_trades(self) -> List[YasinSignal]:
        return [
            signal for signal in self._signals
            if signal.is_approved and not signal.is_closed
        ]

    def closed_trades(self) -> List[YasinSignal]:
        return [
            signal for signal in self._signals
            if signal.is_closed
        ]

    def find_by_symbol(self, symbol: str) -> List[YasinSignal]:
        return [
            signal for signal in self._signals
            if signal.symbol == symbol
        ]

    def find_latest_by_symbol(self, symbol: str) -> Optional[YasinSignal]:
        matches = self.find_by_symbol(symbol)

        if not matches:
            return None

        return sorted(
            matches,
            key=lambda signal: signal.created_at,
            reverse=True,
        )[0]

    def mark_sent_to_telegram(self, signal: YasinSignal) -> YasinSignal:
        signal.is_sent_to_telegram = True
        return signal

    def close_signal(self, signal: YasinSignal, status: str) -> YasinSignal:
        signal.is_closed = True
        signal.status = status
        return signal
