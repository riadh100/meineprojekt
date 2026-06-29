"""
Stellt ein PostgreSQL-Backup
für Yasin AI wieder her.
"""

import shutil
import subprocess
from pathlib import Path


BACKUP_DIR = Path("backups")


def list_backups():

    backups = sorted(
        BACKUP_DIR.glob("database_*.sql")
    )

    if not backups:

        raise FileNotFoundError(
            "Keine Backups gefunden."
        )

    return backups


def restore_database(backup_file):

    command = [

        "psql",

        "-f",

        str(backup_file),

    ]

    subprocess.run(
        command,
        check=True,
    )

    print(
        f"Datenbank wiederhergestellt: {backup_file}"
    )


def restore_configuration():

    source = BACKUP_DIR / "config"

    destination = Path(
        "app/yasin/config"
    )

    if source.exists():

        shutil.copytree(
            source,
            destination,
            dirs_exist_ok=True,
        )

        print(
            "Konfiguration wiederhergestellt."
        )


def restore_exports():

    source = BACKUP_DIR / "exports"

    destination = Path(
        "exports"
    )

    if source.exists():

        shutil.copytree(
            source,
            destination,
            dirs_exist_ok=True,
        )

        print(
            "Exportdaten wiederhergestellt."
        )


def main():

    print("=" * 60)
    print("YASIN AI RESTORE")
    print("=" * 60)

    backups = list_backups()

    print()

    print("Verfügbare Backups:")

    for index, backup in enumerate(
        backups,
        start=1,
    ):

        print(
            f"{index}. {backup.name}"
        )

    print()

    selection = int(
        input(
            "Backup auswählen: "
        )
    )

    restore_database(
        backups[selection - 1]
    )

    restore_configuration()

    restore_exports()

    print()

    print(
        "Wiederherstellung erfolgreich abgeschlossen."
    )


if __name__ == "__main__":

    main()
