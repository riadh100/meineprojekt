"""
Zeigt Versions- und Buildinformationen
für Yasin AI an.
"""

import platform
import subprocess
from datetime import datetime

import pkg_resources


VERSION = "9.0.0"
BUILD = "AI Empire Pro V9"


def get_git_commit():

    try:

        return (
            subprocess.check_output(
                [
                    "git",
                    "rev-parse",
                    "--short",
                    "HEAD",
                ]
            )
            .decode()
            .strip()
        )

    except Exception:

        return "Unbekannt"


def get_build_date():

    return datetime.utcnow().strftime(
        "%Y-%m-%d %H:%M:%S UTC"
    )


def print_dependencies():

    print("\nInstallierte Pakete")

    print("-" * 60)

    packages = sorted(
        pkg_resources.working_set,
        key=lambda p: p.project_name.lower(),
    )

    for package in packages:

        print(
            f"{package.project_name}"
            f"=={package.version}"
        )


def print_system():

    print("=" * 60)
    print("YASIN AI VERSION")
    print("=" * 60)

    print(f"Version        : {VERSION}")
    print(f"Build          : {BUILD}")
    print(f"Build-Datum    : {get_build_date()}")
    print(f"Git Commit     : {get_git_commit()}")

    print()

    print(f"Python         : {platform.python_version()}")
    print(f"Betriebssystem : {platform.system()}")
    print(f"Release        : {platform.release()}")
    print(f"Architektur    : {platform.machine()}")

    print_dependencies()


if __name__ == "__main__":

    print_system()
