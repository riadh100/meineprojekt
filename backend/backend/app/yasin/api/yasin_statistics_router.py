from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db

from app.yasin.repositories.yasin_trade_statistics_repository import (
    YasinTradeStatisticsRepository,
)

router = APIRouter(
    prefix="/api/v9/yasin/statistics",
    tags=["Yasin AI Statistics"],
)


@router.get("/")
def get_all_statistics(
    db: Session = Depends(get_db),
):
    """
    Liefert alle Marktstatistiken.
    """

    repository = YasinTradeStatisticsRepository(db)

    return repository.get_all()


@router.get("/{market}")
def get_market_statistics(
    market: str,
    db: Session = Depends(get_db),
):
    """
    Statistik eines Marktes.
    """

    repository = YasinTradeStatisticsRepository(db)

    statistics = repository.get_market(
        market.upper()
    )

    if statistics is None:
        raise HTTPException(
            status_code=404,
            detail="Statistik nicht gefunden.",
        )

    return statistics


@router.get("/overview/summary")
def get_summary(
    db: Session = Depends(get_db),
):
    """
    Gesamtauswertung aller Märkte.
    """

    repository = YasinTradeStatisticsRepository(db)

    statistics = repository.get_all()

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

    gross_profit = sum(
        item.gross_profit
        for item in statistics
    )

    gross_loss = sum(
        item.gross_loss
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
        "gross_profit": round(gross_profit, 2),
        "gross_loss": round(gross_loss, 2),
        "net_profit": round(net_profit, 2),
    }
