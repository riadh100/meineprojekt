"""
Diagnose- und Health-Check-Skript
für Yasin AI.
"""

import platform
import psutil

from sqlalchemy import text

from app.database.session import engine

from app.yasin.config.yasin_ai_config import (
    get_ai_config,
)


def check_database():

    try:

        with engine.connect() as connection:

            connection.execute(
                text("SELECT 1")
            )

        return True

    except Exception:

        return False


def check_memory():

    memory = psutil.virtual_memory()

    return {
        "total": memory.total,
        "used": memory.used,
        "available": memory.available,
        "percent": memory.percent,
    }


def check_cpu():

    return {
        "usage": psutil.cpu_percent(1),
        "cores": psutil.cpu_count(),
    }


def check_disk():

    disk = psutil.disk_usage("/")

    return {
        "total": disk.total,
        "used": disk.used,
        "free": disk.free,
        "percent": disk.percent,
    }


def print_report():

    print("=" * 60)
    print("YASIN AI SYSTEM CHECK")
    print("=" * 60)

    print()

    print(
        f"System        : {platform.system()}"
    )

    print(
        f"Version       : {platform.release()}"
    )

    print(
        f"Python        : {platform.python_version()}"
    )

    print()

    print(
        "Database      :",
        "OK" if check_database() else "ERROR",
    )

    print()

    memory = check_memory()

    cpu = check_cpu()

    disk = check_disk()

    print(f"CPU Usage     : {cpu['usage']}%")
    print(f"CPU Cores     : {cpu['cores']}")

    print()

    print(f"RAM Usage     : {memory['percent']}%")

    print()

    print(f"Disk Usage    : {disk['percent']}%")

    print()

    print("AI Config")

    print(get_ai_config())

    print()

    print("Systemcheck erfolgreich abgeschlossen.")


if __name__ == "__main__":

    print_report()
