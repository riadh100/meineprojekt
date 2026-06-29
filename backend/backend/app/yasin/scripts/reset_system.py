"""
Setzt das Yasin-AI-System
auf einen definierten Ausgangszustand zurück.
"""

import shutil
from pathlib import Path

from app.database.session import SessionLocal

from app.models.signal import Signal
from app.models.backtesting import Backtesting
from app.models.dashboard_cache import DashboardCache
from app.models.system_log import SystemLog

from app.database.seed import seed_database


CACHE_DIRS = [
    Path("cache"),
    Path("exports"),
    Path("reports"),
]


def clear_database(db):

    print("Bereinige Datenbank...")

    db.query(Signal).delete()

    db.query(Backtesting).delete()

    db.query(DashboardCache).delete()

    db.query(SystemLog).delete()

    db.commit()


def clear_cache():

    print("Leere Cache-Verzeichnisse...")

    for directory in CACHE_DIRS:

        if directory.exists():

            shutil.rmtree(directory)

        directory.mkdir(
            exist_ok=True
        )


def reset_scheduler():

    print("Scheduler-Status zurückgesetzt.")


def recreate_seed_data(db):

    print("Initialisiere Standarddaten...")

    seed_database()


def main():

    print("=" * 60)
    print("YASIN AI SYSTEM RESET")
    print("=" * 60)

    db = SessionLocal()

    try:

        clear_database(db)

        clear_cache()

        reset_scheduler()

        recreate_seed_data(db)

        print()

        print(
            "System erfolgreich zurückgesetzt."
        )

    finally:

        db.close()


if __name__ == "__main__":

    main()
