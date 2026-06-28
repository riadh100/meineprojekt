from dataclasses import dataclass
from typing import Any, Dict, List


@dataclass
class BacktestResult:
    total_trades: int
    winning_trades: int
    losing_trades: int
    win_rate: float
    loss_rate: float
    profit_factor: float
    net_profit: float
    max_drawdown: float
    equity_curve: List[float]


class YasinBacktestingService:
    """
    Führt Backtests für Yasin-Strategien durch.

    Nutzt historische Candles und die vorhandenen
    Strategien, ohne Live-Trading auszuführen.
    """

    def __init__(
        self,
        market_analysis_service: Any,
        strategy_service: Any,
    ):
        self.market_analysis_service = market_analysis_service
        self.strategy_service = strategy_service

    def run(
        self,
        strategy: Any,
        candles: List[Dict],
        initial_balance: float = 10000.0,
    ) -> BacktestResult:

        balance = initial_balance
        equity_curve = [balance]

        total = 0
        wins = 0
        losses = 0

        gross_profit = 0.0
        gross_loss = 0.0

        for candle in candles:

            trade = strategy.build_trade(
                candles=[candle],
                indicators={},
            )

            if trade is None:
                continue

            total += 1

            pnl = self._simulate_trade(
                candle,
                trade,
            )

            balance += pnl
            equity_curve.append(balance)

            if pnl > 0:
                wins += 1
                gross_profit += pnl
            else:
                losses += 1
                gross_loss += abs(pnl)

        win_rate = (
            wins / total * 100
            if total else 0
        )

        loss_rate = (
            losses / total * 100
            if total else 0
        )

        profit_factor = (
            gross_profit / gross_loss
            if gross_loss > 0
            else gross_profit
        )

        return BacktestResult(
            total_trades=total,
            winning_trades=wins,
            losing_trades=losses,
            win_rate=round(win_rate, 2),
            loss_rate=round(loss_rate, 2),
            profit_factor=round(profit_factor, 2),
            net_profit=round(
                balance - initial_balance,
                2,
            ),
            max_drawdown=self._drawdown(
                equity_curve
            ),
            equity_curve=equity_curve,
        )

    def _simulate_trade(
        self,
        candle: Dict,
        trade: Dict,
    ) -> float:
        """
        Vereinfachte Trade-Simulation.
        """

        close = float(candle["close"])
        entry = trade["entry"]
        tp3 = trade["tp3"]

        direction = trade["direction"].value

        if direction == "BUY":
            return tp3 - entry if close > entry else -(
                entry - close
            )

        return entry - tp3 if close < entry else -(
            close - entry
        )

    def _drawdown(
        self,
        equity_curve: List[float],
    ) -> float:

        peak = equity_curve[0]
        max_dd = 0.0

        for equity in equity_curve:

            if equity > peak:
                peak = equity

            dd = (
                (peak - equity) / peak * 100
                if peak > 0
                else 0
            )

            max_dd = max(
                max_dd,
                dd,
            )

        return round(max_dd, 2)
