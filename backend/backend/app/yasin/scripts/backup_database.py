"""
Erstellt Datenbank-Backups
für Yasin AI.
"""

import os
import shutil
import subprocess
from datetime import datetime
from pathlib import Path


BACKUP_DIR = Path("backups")

DATABASE_NAME = os.getenv(
    "POSTGRES_DB",
    "yasin_ai",
)

DATABASE_USER = os.getenv(
    "POSTGRES_USER",
    "postgres",
)

DATABASE_HOST = os.getenv(
    "POSTGRES_HOST",
    "localhost",
)

DATABASE_PORT = os.getenv(
    "POSTGRES_PORT",
    "5432",
)


def ensure_backup_directory():

    BACKUP_DIR.mkdir(
        exist_ok=True
    )


def backup_database():

    ensure_backup_directory()

    timestamp = datetime.utcnow().strftime(
        "%Y%m%d_%H%M%S"
    )

    backup_file = (
        BACKUP_DIR /
        f"database_{timestamp}.sql"
    )

    command = [

        "pg_dump",

        "-h", DATABASE_HOST,

        "-p", DATABASE_PORT,

        "-U", DATABASE_USER,

        "-F", "p",

        "-f", str(backup_file),

        DATABASE_NAME,

    ]

    subprocess.run(
        command,
        check=True,
    )

    print(
        f"Datenbank gesichert: {backup_file}"
    )

    return backup_file


def backup_configuration():

    ensure_backup_directory()

    destination = (
        BACKUP_DIR /
        "config"
    )

    shutil.copytree(
        "app/yasin/config",
        destination,
        dirs_exist_ok=True,
    )

    print(
        "Konfiguration gesichert."
    )


def backup_exports():

    if not Path(
        "exports"
    ).exists():

        return

    shutil.copytree(
        "exports",
        BACKUP_DIR / "exports",
        dirs_exist_ok=True,
    )

    print(
        "Exportdaten gesichert."
    )


def cleanup_old_backups(
    keep=10,
):

    backups = sorted(
        BACKUP_DIR.glob(
            "database_*.sql"
        )
    )

    while len(backups) > keep:

        oldest = backups.pop(0)

        oldest.unlink()

        print(
            f"Altes Backup entfernt: {oldest}"
        )


def main():

    print("=" * 60)
    print("YASIN AI BACKUP")
    print("=" * 60)

    backup_database()

    backup_configuration()

    backup_exports()

    cleanup_old_backups()

    print()

    print(
        "Backup erfolgreich abgeschlossen."
    )


if __name__ == "__main__":

    main()
