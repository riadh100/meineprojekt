"""
Bereinigt und optimiert die Datenbank
für Yasin AI.
"""

from datetime import datetime, timedelta

from sqlalchemy import text

from app.database.session import (
    SessionLocal,
)

from app.models.signal import Signal
from app.models.backtesting import Backtesting
from app.models.system_log import SystemLog
from app.models.dashboard_cache import DashboardCache


RETENTION_DAYS = 90


def cleanup_logs(db):

    limit = datetime.utcnow() - timedelta(
        days=RETENTION_DAYS
    )

    deleted = (
        db.query(SystemLog)
        .filter(
            SystemLog.created_at < limit
        )
        .delete()
    )

    print(f"Logs entfernt: {deleted}")


def cleanup_closed_trades(db):

    limit = datetime.utcnow() - timedelta(
        days=RETENTION_DAYS
    )

    deleted = (
        db.query(Signal)
        .filter(
            Signal.status == "CLOSED",
            Signal.closed_at < limit,
        )
        .delete()
    )

    print(f"Trades entfernt: {deleted}")


def cleanup_backtesting(db):

    deleted = (
        db.query(Backtesting)
        .delete()
    )

    print(
        f"Backtests entfernt: {deleted}"
    )


def cleanup_dashboard_cache(db):

    deleted = (
        db.query(DashboardCache)
        .delete()
    )

    print(
        f"Cache entfernt: {deleted}"
    )


def optimize_database(db):

    db.execute(
        text("VACUUM ANALYZE")
    )

    print(
        "Datenbank optimiert."
    )


def cleanup():

    db = SessionLocal()

    try:

        print("=" * 60)
        print("YASIN AI DATABASE CLEANUP")
        print("=" * 60)

        cleanup_logs(db)

        cleanup_closed_trades(db)

        cleanup_backtesting(db)

        cleanup_dashboard_cache(db)

        db.commit()

        optimize_database(db)

        print()

        print(
            "Bereinigung erfolgreich abgeschlossen."
        )

    finally:

        db.close()


if __name__ == "__main__":

    cleanup()
