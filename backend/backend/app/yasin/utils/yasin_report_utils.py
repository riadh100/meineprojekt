from datetime import datetime

from app.yasin.utils.yasin_statistics_utils import (
    win_rate,
    profit_factor,
    net_profit,
)


def performance_report(
    statistics,
) -> dict:
    """
    Erstellt einen Performance-Bericht.
    """

    return {
        "generated_at": datetime.utcnow().isoformat(),
        "market": statistics.market,
        "total_trades": statistics.total_trades,
        "winning_trades": statistics.winning_trades,
        "losing_trades": statistics.losing_trades,
        "win_rate": win_rate(
            statistics.winning_trades,
            statistics.total_trades,
        ),
        "profit_factor": profit_factor(
            statistics.gross_profit,
            statistics.gross_loss,
        ),
        "net_profit": net_profit(
            statistics.gross_profit,
            statistics.gross_loss,
        ),
    }


def daily_summary(
    statistics_list,
):

    return {
        "generated_at": datetime.utcnow().isoformat(),
        "markets": len(statistics_list),
        "reports": [
            performance_report(item)
            for item in statistics_list
        ],
    }


def weekly_summary(
    statistics_list,
):

    report = daily_summary(
        statistics_list
    )

    report["period"] = "weekly"

    return report


def telegram_summary(
    statistics,
) -> str:

    report = performance_report(
        statistics
    )

    return (
        f"📊 {report['market']}\n\n"
        f"Trades: {report['total_trades']}\n"
        f"Winrate: {report['win_rate']}%\n"
        f"Profit Factor: {report['profit_factor']}\n"
        f"Net Profit: {report['net_profit']}"
    )


def dashboard_summary(
    statistics_list,
):

    return [
        performance_report(item)
        for item in statistics_list
    ]


def export_json(
    report,
):

    return report
