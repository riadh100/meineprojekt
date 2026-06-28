from app.yasin.models.yasin_signal_model import (
    YasinSignalModel,
)

from app.yasin.models.yasin_trade_statistics_model import (
    YasinTradeStatisticsModel,
)


class YasinDashboardMapper:
    """
    Mapper für Dashboard-Daten.

    Trennt Datenbankmodelle von der
    API-/Frontend-Darstellung.
    """

    @staticmethod
    def signal(
        signal: YasinSignalModel,
    ) -> dict:

        return {
            "id": signal.id,
            "market": signal.market,
            "symbol": signal.symbol,
            "direction": signal.direction,
            "entry": signal.entry,
            "stop_loss": signal.stop_loss,
            "tp1": signal.take_profit_1,
            "tp2": signal.take_profit_2,
            "tp3": signal.take_profit_3,
            "quality": signal.quality_score,
            "risk_reward": signal.risk_reward_ratio,
            "status": signal.status,
            "approved": signal.is_approved,
            "telegram_sent": signal.is_sent_to_telegram,
            "closed": signal.is_closed,
            "profit": signal.realized_profit,
            "profit_percent": signal.realized_profit_percent,
            "created_at": signal.created_at,
            "closed_at": signal.closed_at,
        }

    @staticmethod
    def statistics(
        statistics: YasinTradeStatisticsModel,
    ) -> dict:

        return {
            "market": statistics.market,
            "total_trades": statistics.total_trades,
            "winning_trades": statistics.winning_trades,
            "losing_trades": statistics.losing_trades,
            "win_rate": statistics.win_rate,
            "loss_rate": statistics.loss_rate,
            "average_rr": statistics.average_rr,
            "profit_factor": statistics.profit_factor,
            "expectancy": statistics.expectancy,
            "gross_profit": statistics.gross_profit,
            "gross_loss": statistics.gross_loss,
            "net_profit": statistics.net_profit,
            "max_drawdown": statistics.max_drawdown,
            "current_drawdown": statistics.current_drawdown,
            "updated_at": statistics.updated_at,
        }

    @classmethod
    def signals(
        cls,
        signals: list[YasinSignalModel],
    ) -> list[dict]:

        return [
            cls.signal(signal)
            for signal in signals
        ]

    @classmethod
    def statistics_list(
        cls,
        statistics: list[YasinTradeStatisticsModel],
    ) -> list[dict]:

        return [
            cls.statistics(item)
            for item in statistics
        ]

    @classmethod
    def dashboard(
        cls,
        *,
        summary: dict,
        system: dict,
        statistics: list[YasinTradeStatisticsModel],
        open_trades: list[YasinSignalModel],
        latest_signals: list[YasinSignalModel],
    ) -> dict:

        return {
            "summary": summary,
            "system": system,
            "statistics": cls.statistics_list(
                statistics
            ),
            "open_trades": cls.signals(
                open_trades
            ),
            "latest_signals": cls.signals(
                latest_signals
            ),
        }
