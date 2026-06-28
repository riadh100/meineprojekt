from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db

from app.yasin.services.yasin_backtesting_service import (
    YasinBacktestingService,
)

from app.yasin.services.yasin_strategy_service import (
    YasinStrategyService,
)

router = APIRouter(
    prefix="/api/v9/yasin/backtesting",
    tags=["Yasin AI Backtesting"],
)


@router.post("/run/{strategy_name}")
def run_backtest(
    strategy_name: str,
    start_date: str,
    end_date: str,
    timeframe: str = "15m",
    initial_balance: float = 10000.0,
    db: Session = Depends(get_db),
):
    """
    Startet einen Backtest.
    """

    strategy_service = YasinStrategyService(db)

    strategy = strategy_service.get(
        strategy_name.upper()
    )

    if strategy is None:
        raise HTTPException(
            status_code=404,
            detail="Strategie nicht gefunden.",
        )

    backtesting = YasinBacktestingService(
        strategy_service=strategy_service,
    )

    result = backtesting.run(
        strategy=strategy,
        start_date=datetime.fromisoformat(start_date),
        end_date=datetime.fromisoformat(end_date),
        timeframe=timeframe,
        initial_balance=initial_balance,
    )

    return result


@router.get("/strategies")
def available_strategies(
    db: Session = Depends(get_db),
):
    """
    Liefert alle verfügbaren Strategien.
    """

    strategy_service = YasinStrategyService(db)

    return {
        "count": strategy_service.count(),
        "strategies": [
            strategy.__class__.__name__
            for strategy in strategy_service.all()
        ],
    }


@router.get("/health")
def health():
    """
    Healthcheck für Backtesting.
    """

    return {
        "service": "Yasin Backtesting",
        "status": "running",
    }
