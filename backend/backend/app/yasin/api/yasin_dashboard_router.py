from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db

from app.yasin.repositories.yasin_signal_repository import (
    YasinSignalRepository,
)

from app.yasin.repositories.yasin_trade_statistics_repository import (
    YasinTradeStatisticsRepository,
)

router = APIRouter(
    prefix="/api/v9/yasin/dashboard",
    tags=["Yasin AI Dashboard"],
)


@router.get("/")
def dashboard(
    db: Session = Depends(get_db),
):
    """
    Liefert alle Dashboard-Daten in einer Antwort.
    """

    signal_repository = YasinSignalRepository(db)
    statistics_repository = (
        YasinTradeStatisticsRepository(db)
    )

    open_trades = signal_repository.get_open_signals()
    closed_trades = signal_repository.get_closed_signals()

    latest_signals = signal_repository.get_all()[:10]

    statistics = statistics_repository.get_all()

    return {
        "summary": {
            "open_trades": len(open_trades),
            "closed_trades": len(closed_trades),
            "total_signals": len(
                open_trades
            ) + len(closed_trades),
        },
        "statistics": statistics,
        "latest_signals": latest_signals,
        "open_trades": open_trades,
    }


@router.get("/overview")
def overview(
    db: Session = Depends(get_db),
):
    """
    Übersicht aller Kennzahlen.
    """

    statistics_repository = (
        YasinTradeStatisticsRepository(db)
    )

    statistics = statistics_repository.get_all()

    total_trades = sum(
        item.total_trades
        for item in statistics
    )

    winning_trades = sum(
        item.winning_trades
        for item in statistics
    )

    losing_trades = sum(
        item.losing_trades
        for item in statistics
    )

    net_profit = sum(
        item.net_profit
        for item in statistics
    )

    return {
        "markets": len(statistics),
        "total_trades": total_trades,
        "winning_trades": winning_trades,
        "losing_trades": losing_trades,
        "net_profit": round(
            net_profit,
            2,
        ),
    }


@router.get("/health")
def health():
    """
    Healthcheck für Dashboard.
    """

    return {
        "service": "Yasin Dashboard",
        "status": "running",
    }
