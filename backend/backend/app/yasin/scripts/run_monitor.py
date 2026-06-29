"""
Überwacht aktive Trades
für Yasin AI.
"""

import argparse
import time

from app.yasin.services.yasin_monitor_service import (
    YasinMonitorService,
)


def parse_arguments():

    parser = argparse.ArgumentParser(
        description="Yasin AI Trade Monitor"
    )

    parser.add_argument(
        "--interval",
        type=int,
        default=30,
        help="Überwachungsintervall in Sekunden",
    )

    parser.add_argument(
        "--once",
        action="store_true",
        help="Nur einen Überwachungszyklus ausführen",
    )

    return parser.parse_args()


def print_report(report):

    print("-" * 60)

    print(f"Zeitpunkt          : {report.timestamp}")
    print(f"Offene Trades      : {report.open_trades}")
    print(f"TP erreicht        : {report.take_profit_hits}")
    print(f"SL erreicht        : {report.stop_loss_hits}")
    print(f"Aktualisierte Trades: {report.updated_trades}")

    print("-" * 60)


def main():

    args = parse_arguments()

    monitor = YasinMonitorService()

    print("=" * 60)
    print("YASIN AI TRADE MONITOR")
    print("=" * 60)

    try:

        while True:

            report = monitor.monitor()

            print_report(report)

            if args.once:

                break

            time.sleep(args.interval)

    except KeyboardInterrupt:

        print()

        print("Monitoring beendet.")

    finally:

        monitor.shutdown()


if __name__ == "__main__":

    main()
