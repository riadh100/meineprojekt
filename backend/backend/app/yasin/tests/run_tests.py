"""
Zentraler Test-Runner
für Yasin AI.
"""

import argparse
import subprocess
import sys


def run_pytest(
    args: list[str],
) -> int:
    """
    Führt pytest mit den
    angegebenen Argumenten aus.
    """
    return subprocess.call(
        [
            sys.executable,
            "-m",
            "pytest",
            *args,
        ]
    )


def main():

    parser = argparse.ArgumentParser(
        description="Yasin AI Test Runner"
    )

    parser.add_argument(
        "--unit",
        action="store_true",
        help="Nur Unit-Tests ausführen",
    )

    parser.add_argument(
        "--integration",
        action="store_true",
        help="Nur Integrationstests ausführen",
    )

    parser.add_argument(
        "--e2e",
        action="store_true",
        help="Nur End-to-End-Tests ausführen",
    )

    parser.add_argument(
        "--coverage",
        action="store_true",
        help="Coverage-Bericht erzeugen",
    )

    options = parser.parse_args()

    pytest_args = []

    if options.unit:
        pytest_args.extend(
            [
                "-m",
                "unit",
            ]
        )

    if options.integration:
        pytest_args.extend(
            [
                "-m",
                "integration",
            ]
        )

    if options.e2e:
        pytest_args.extend(
            [
                "-m",
                "e2e",
            ]
        )

    if options.coverage:
        pytest_args.extend(
            [
                "--cov=app",
                "--cov-report=term",
                "--cov-report=html",
            ]
        )

    raise SystemExit(
        run_pytest(pytest_args)
    )


if __name__ == "__main__":
    main()
