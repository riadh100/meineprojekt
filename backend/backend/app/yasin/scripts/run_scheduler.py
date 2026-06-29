"""
Startet den Scheduler
für Yasin AI.
"""

import time
import argparse

from app.yasin.scheduler.yasin_scheduler_service import (
    YasinSchedulerService,
)


def parse_arguments():

    parser = argparse.ArgumentParser(
        description="Yasin AI Scheduler"
    )

    parser.add_argument(
        "--status",
        action="store_true",
        help="Nur Status anzeigen",
    )

    parser.add_argument(
        "--interval",
        type=int,
        default=60,
        help="Statusintervall in Sekunden",
    )

    return parser.parse_args()


def print_status(status):

    print("-" * 60)

    print(f"Status          : {status['status']}")
    print(f"Aktive Jobs     : {status['jobs']}")
    print(f"Laufend         : {status['running']}")
    print(f"Nächster Job    : {status['next_job']}")
    print(f"Letzter Job     : {status['last_job']}")

    print("-" * 60)


def main():

    args = parse_arguments()

    scheduler = YasinSchedulerService()

    print("=" * 60)
    print("YASIN AI SCHEDULER")
    print("=" * 60)

    if args.status:

        print_status(
            scheduler.status()
        )

        return

    scheduler.start()

    print("\nScheduler gestartet.\n")

    try:

        while True:

            status = scheduler.status()

            print_status(status)

            time.sleep(args.interval)

    except KeyboardInterrupt:

        print()

        print("Scheduler wird beendet...")

    finally:

        scheduler.stop()

        print("Scheduler erfolgreich gestoppt.")


if __name__ == "__main__":

    main()
