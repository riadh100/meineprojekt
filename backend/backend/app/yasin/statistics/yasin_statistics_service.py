from collections import defaultdict
from typing import Dict

from app.yasin.signals.signal_repository import SignalRepository


class YasinStatisticsService:
    """
    Erstellt Performance-Statistiken für Yasin AI.
    """

    def __init__(self, repository: SignalRepository):
        self.repository = repository

    def overview(self) -> Dict:
        closed = self.repository.closed_trades()
        total = len(closed)

        wins = [
            signal for signal in closed
            if signal.status in ["TP1", "TP2", "TP3"]
        ]

        losses = [
            signal for signal in closed
            if signal.status == "STOP_LOSS"
        ]

        return {
            "total_closed_trades": total,
            "wins": len(wins),
            "losses": len(losses),
            "win_rate": self._percentage(len(wins), total),
            "loss_rate": self._percentage(len(losses), total),
            "profit_factor": self._profit_factor(wins, losses),
            "performance_by_market": self.performance_by_market(),
        }

    def performance_by_market(self) -> Dict:
        result = defaultdict(lambda: {
            "total": 0,
            "wins": 0,
            "losses": 0,
            "win_rate": 0.0,
        })

        for signal in self.repository.closed_trades():
            market = signal.market.value
            result[market]["total"] += 1

            if signal.status in ["TP1", "TP2", "TP3"]:
                result[market]["wins"] += 1

            if signal.status == "STOP_LOSS":
                result[market]["losses"] += 1

        for market, stats in result.items():
            stats["win_rate"] = self._percentage(
                stats["wins"],
                stats["total"],
            )

        return dict(result)

    def _percentage(self, value: int, total: int) -> float:
        if total == 0:
            return 0.0

        return round((value / total) * 100, 2)

    def _profit_factor(self, wins, losses) -> float:
        if not losses:
            return float("inf") if wins else 0.0

        return round(len(wins) / len(losses), 2)
