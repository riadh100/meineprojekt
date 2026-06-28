from app.yasin.repositories.yasin_signal_repository import (
    YasinSignalRepository,
)

from app.yasin.repositories.yasin_trade_statistics_repository import (
    YasinTradeStatisticsRepository,
)

from app.yasin.models.yasin_trade_statistics_model import (
    YasinTradeStatisticsModel,
)


class YasinStatisticsServiceV2:
    """
    Erweiterter Statistik-Service für Yasin AI.

    Berechnet Performance-Daten direkt aus den
    gespeicherten Trades und aktualisiert die
    Statistik-Tabelle.
    """

    def __init__(
        self,
        signal_repository: YasinSignalRepository,
        statistics_repository: YasinTradeStatisticsRepository,
    ):
        self.signal_repository = signal_repository
        self.statistics_repository = statistics_repository

    def rebuild_market(
        self,
        market: str,
    ) -> YasinTradeStatisticsModel:

        trades = [
            trade
            for trade in self.signal_repository.get_closed_signals()
            if trade.market == market
        ]

        total = len(trades)

        wins = [
            trade for trade in trades
            if trade.realized_profit is not None
            and trade.realized_profit > 0
        ]

        losses = [
            trade for trade in trades
            if trade.realized_profit is not None
            and trade.realized_profit <= 0
        ]

        gross_profit = sum(
            trade.realized_profit
            for trade in wins
        )

        gross_loss = abs(
            sum(
                trade.realized_profit
                for trade in losses
            )
        )

        average_profit = (
            gross_profit / len(wins)
            if wins else 0.0
        )

        average_loss = (
            gross_loss / len(losses)
            if losses else 0.0
        )

        average_rr = (
            sum(
                trade.risk_reward_ratio
                for trade in trades
            ) / total
            if total else 0.0
        )

        win_rate = (
            (len(wins) / total) * 100
            if total else 0.0
        )

        loss_rate = (
            (len(losses) / total) * 100
            if total else 0.0
        )

        profit_factor = (
            gross_profit / gross_loss
            if gross_loss > 0
            else gross_profit
        )

        expectancy = (
            (
                average_profit * (win_rate / 100)
            ) -
            (
                average_loss * (loss_rate / 100)
            )
        )

        statistics = YasinTradeStatisticsModel(
            market=market,
            total_trades=total,
            winning_trades=len(wins),
            losing_trades=len(losses),
            win_rate=round(win_rate, 2),
            loss_rate=round(loss_rate, 2),
            average_rr=round(average_rr, 2),
            average_profit=round(
                average_profit,
                2,
            ),
            average_loss=round(
                average_loss,
                2,
            ),
            gross_profit=round(
                gross_profit,
                2,
            ),
            gross_loss=round(
                gross_loss,
                2,
            ),
            net_profit=round(
                gross_profit - gross_loss,
                2,
            ),
            profit_factor=round(
                profit_factor,
                2,
            ),
            expectancy=round(
                expectancy,
                2,
            ),
            max_drawdown=0.0,
            current_drawdown=0.0,
        )

        return self.statistics_repository.save(
            statistics
        )

    def rebuild_all(self):

        markets = {
            trade.market
            for trade in self.signal_repository.get_closed_signals()
        }

        return [
            self.rebuild_market(market)
            for market in markets
        ]
