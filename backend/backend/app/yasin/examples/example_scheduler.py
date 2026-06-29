"""
Beispiel für den Scheduler
von Yasin AI.
"""

import time

from app.yasin.scheduler.yasin_scheduler_service import (
    YasinSchedulerService,
)


def main():

    scheduler = YasinSchedulerService()

    print("=" * 60)
    print("YASIN AI SCHEDULER")
    print("=" * 60)

    print("\nScheduler wird gestartet...")

    scheduler.start()

    print()

    print("Scheduler läuft.")

    try:

        while True:

            status = scheduler.status()

            print("-" * 60)

            print(f"Status        : {status['status']}")
            print(f"Jobs          : {status['jobs']}")
            print(f"Laufend       : {status['running']}")
            print(f"Nächster Job  : {status['next_job']}")

            time.sleep(10)

    except KeyboardInterrupt:

        print()

        print("Scheduler wird beendet...")

        scheduler.stop()

        print("Scheduler gestoppt.")


if __name__ == "__main__":
    main()
