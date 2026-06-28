from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db

from app.yasin.repositories.yasin_strategy_config_repository import (
    YasinStrategyConfigRepository,
)

router = APIRouter(
    prefix="/api/v9/yasin/strategies",
    tags=["Yasin AI Strategies"],
)


@router.get("/")
def get_all_strategies(
    db: Session = Depends(get_db),
):
    """
    Alle Strategien abrufen.
    """

    repository = YasinStrategyConfigRepository(db)

    return repository.get_all()


@router.get("/enabled")
def get_enabled_strategies(
    db: Session = Depends(get_db),
):
    """
    Alle aktiven Strategien.
    """

    repository = YasinStrategyConfigRepository(db)

    return repository.get_enabled()


@router.get("/{strategy_id}")
def get_strategy(
    strategy_id: int,
    db: Session = Depends(get_db),
):
    """
    Einzelne Strategie laden.
    """

    repository = YasinStrategyConfigRepository(db)

    strategy = repository.get(strategy_id)

    if strategy is None:
        raise HTTPException(
            status_code=404,
            detail="Strategie nicht gefunden.",
        )

    return strategy


@router.post("/{strategy_id}/enable")
def enable_strategy(
    strategy_id: int,
    db: Session = Depends(get_db),
):
    """
    Strategie aktivieren.
    """

    repository = YasinStrategyConfigRepository(db)

    strategy = repository.enable(strategy_id)

    if strategy is None:
        raise HTTPException(
            status_code=404,
            detail="Strategie nicht gefunden.",
        )

    return strategy


@router.post("/{strategy_id}/disable")
def disable_strategy(
    strategy_id: int,
    db: Session = Depends(get_db),
):
    """
    Strategie deaktivieren.
    """

    repository = YasinStrategyConfigRepository(db)

    strategy = repository.disable(strategy_id)

    if strategy is None:
        raise HTTPException(
            status_code=404,
            detail="Strategie nicht gefunden.",
        )

    return strategy
