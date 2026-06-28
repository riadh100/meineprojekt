from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from app.database.session import get_db

from app.yasin.repositories.yasin_signal_repository import (
    YasinSignalRepository,
)

router = APIRouter(
    prefix="/api/v9/yasin/signals",
    tags=["Yasin AI Signals"],
)


@router.get("/")
def get_all_signals(
    db: Session = Depends(get_db),
):
    """
    Alle Signale abrufen.
    """

    repository = YasinSignalRepository(db)

    return repository.get_all()


@router.get("/open")
def get_open_signals(
    db: Session = Depends(get_db),
):
    """
    Offene Trades abrufen.
    """

    repository = YasinSignalRepository(db)

    return repository.get_open_signals()


@router.get("/closed")
def get_closed_signals(
    db: Session = Depends(get_db),
):
    """
    Geschlossene Trades abrufen.
    """

    repository = YasinSignalRepository(db)

    return repository.get_closed_signals()


@router.get("/{signal_id}")
def get_signal(
    signal_id: int,
    db: Session = Depends(get_db),
):
    """
    Einzelnes Signal laden.
    """

    repository = YasinSignalRepository(db)

    signal = repository.get(signal_id)

    if signal is None:
        raise HTTPException(
            status_code=404,
            detail="Signal nicht gefunden.",
        )

    return signal


@router.get("/symbol/{symbol}")
def get_symbol_signals(
    symbol: str,
    db: Session = Depends(get_db),
):
    """
    Alle Signale eines Symbols.
    """

    repository = YasinSignalRepository(db)

    return repository.get_by_symbol(symbol)


@router.delete("/{signal_id}")
def delete_signal(
    signal_id: int,
    db: Session = Depends(get_db),
):
    """
    Signal löschen.
    """

    repository = YasinSignalRepository(db)

    deleted = repository.delete(signal_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Signal nicht gefunden.",
        )

    return {
        "success": True,
        "message": "Signal erfolgreich gelöscht.",
    }
