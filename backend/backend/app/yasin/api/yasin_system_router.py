from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db

from app.yasin.services.yasin_ai_service import (
    YasinAIService,
)

router = APIRouter(
    prefix="/api/v9/yasin/system",
    tags=["Yasin AI System"],
)


def get_yasin_service(
    db: Session = Depends(get_db),
) -> YasinAIService:
    """
    Dependency für den zentralen
    Yasin AI Service.

    Die konkrete Initialisierung erfolgt
    über die bestehende V8 Dependency Injection.
    """
    return YasinAIService()


@router.get("/status")
def system_status(
    service: YasinAIService = Depends(
        get_yasin_service
    ),
):
    """
    Aktueller Systemstatus.
    """

    return {
        "scheduler_running": service.scheduler_running(),
        "open_trades": len(
            service.get_open_trades()
        ),
        "closed_trades": len(
            service.get_closed_trades()
        ),
        "signals": len(
            service.get_all_signals()
        ),
    }


@router.post("/start")
def start_system(
    service: YasinAIService = Depends(
        get_yasin_service
    ),
):
    """
    Startet Yasin AI.
    """

    service.start()

    return {
        "success": True,
        "message": "Yasin AI gestartet.",
    }


@router.post("/stop")
def stop_system(
    service: YasinAIService = Depends(
        get_yasin_service
    ),
):
    """
    Stoppt Yasin AI.
    """

    service.stop()

    return {
        "success": True,
        "message": "Yasin AI gestoppt.",
    }


@router.post("/analyze")
def analyze_now(
    service: YasinAIService = Depends(
        get_yasin_service
    ),
):
    """
    Startet sofort eine Marktanalyse.
    """

    return service.analyze_now()


@router.post("/monitor")
def monitor_now(
    service: YasinAIService = Depends(
        get_yasin_service
    ),
):
    """
    Führt sofort ein Monitoring
    aller offenen Trades aus.
    """

    service.monitor_now()

    return {
        "success": True,
        "message": "Monitoring abgeschlossen.",
    }


@router.post("/statistics/rebuild")
def rebuild_statistics(
    service: YasinAIService = Depends(
        get_yasin_service
    ),
):
    """
    Statistiken neu berechnen.
    """

    statistics = service.get_statistics()

    return {
        "success": True,
        "statistics": statistics,
    }


@router.get("/health")
def health():
    """
    Healthcheck.
    """

    return {
        "service": "Yasin AI",
        "status": "running",
        "version": "9.0",
    }
