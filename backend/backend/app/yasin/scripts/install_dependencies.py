"""
Installiert und überprüft alle Abhängigkeiten
für Yasin AI.
"""

import subprocess
import sys
from pathlib import Path


REQUIREMENTS_FILE = Path("requirements.txt")


def check_python():

    print("Python-Version prüfen...")

    major = sys.version_info.major
    minor = sys.version_info.minor

    if (major, minor) < (3, 12):

        raise RuntimeError(
            "Python 3.12 oder neuer wird benötigt."
        )

    print(
        f"Python {major}.{minor} erkannt."
    )


def install_requirements():

    if not REQUIREMENTS_FILE.exists():

        raise FileNotFoundError(
            "requirements.txt nicht gefunden."
        )

    print("Installiere Abhängigkeiten...")

    subprocess.run(
        [
            sys.executable,
            "-m",
            "pip",
            "install",
            "-U",
            "pip",
        ],
        check=True,
    )

    subprocess.run(
        [
            sys.executable,
            "-m",
            "pip",
            "install",
            "-r",
            str(REQUIREMENTS_FILE),
        ],
        check=True,
    )


def verify_installation():

    packages = [

        "fastapi",

        "uvicorn",

        "sqlalchemy",

        "pydantic",

        "psycopg",

        "apscheduler",

        "requests",

        "openpyxl",

        "reportlab",

    ]

    print()

    print("Installationsprüfung")

    for package in packages:

        __import__(package)

        print(f"OK  {package}")


def print_summary():

    print()

    print("=" * 60)
    print("INSTALLATION ERFOLGREICH")
    print("=" * 60)

    print("Alle Abhängigkeiten wurden installiert.")
    print("Yasin AI ist einsatzbereit.")


def main():

    print("=" * 60)
    print("YASIN AI INSTALLER")
    print("=" * 60)

    check_python()

    install_requirements()

    verify_installation()

    print_summary()


if __name__ == "__main__":

    main()
