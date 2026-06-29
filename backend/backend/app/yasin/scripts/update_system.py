"""
Aktualisiert das gesamte
Yasin-AI-System.
"""

import subprocess
import sys


def run(command, description):

    print(f"\n{description}...")

    subprocess.run(
        command,
        check=True,
    )


def update_source():

    run(
        ["git", "pull"],
        "Quellcode aktualisieren",
    )


def update_dependencies():

    run(
        [
            sys.executable,
            "-m",
            "pip",
            "install",
            "-U",
            "-r",
            "requirements.txt",
        ],
        "Python-Abhängigkeiten aktualisieren",
    )


def migrate_database():

    run(
        [
            "alembic",
            "upgrade",
            "head",
        ],
        "Datenbankmigration ausführen",
    )


def restart_services():

    services = [

        "yasin-api",

        "yasin-scheduler",

        "nginx",

    ]

    for service in services:

        run(
            [
                "systemctl",
                "restart",
                service,
            ],
            f"Dienst {service} neu starten",
        )


def verify_system():

    run(
        [
            sys.executable,
            "app/yasin/scripts/check_system.py",
        ],
        "System überprüfen",
    )


def print_summary():

    print()
    print("=" * 60)
    print("UPDATE ABGESCHLOSSEN")
    print("=" * 60)

    print("✓ Quellcode aktualisiert")
    print("✓ Abhängigkeiten aktualisiert")
    print("✓ Datenbank migriert")
    print("✓ Dienste neu gestartet")
    print("✓ Systemprüfung erfolgreich")


def main():

    print("=" * 60)
    print("YASIN AI UPDATE")
    print("=" * 60)

    update_source()

    update_dependencies()

    migrate_database()

    restart_services()

    verify_system()

    print_summary()


if __name__ == "__main__":

    main()
