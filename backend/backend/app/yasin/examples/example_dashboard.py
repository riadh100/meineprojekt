"""
Beispiel für das Dashboard
von Yasin AI.
"""

from app.yasin.services.yasin_dashboard_service import (
    YasinDashboardService,
)


def main():

    dashboard = YasinDashboardService()

    print("=" * 60)
    print("YASIN AI DASHBOARD")
    print("=" * 60)

    print("\nDashboard wird geladen...")

    data = dashboard.get_dashboard()

    print()

    print("SYSTEMSTATUS")
    print("-" * 60)
    print(data.system)

    print()

    print("PERFORMANCE")
    print("-" * 60)
    print(data.performance)

    print()

    print("STATISTIKEN")
    print("-" * 60)
    print(data.statistics)

    print()

    print("OFFENE TRADES")
    print("-" * 60)

    for trade in data.open_trades:

        print(
            f"{trade.symbol} "
            f"{trade.direction} "
            f"{trade.entry}"
        )

    print()

    print("LETZTE SIGNALE")
    print("-" * 60)

    for signal in data.latest_signals:

        print(
            f"{signal.market} "
            f"{signal.direction} "
            f"{signal.quality_score}%"
        )

    print()

    print("Dashboard aktualisieren...")

    dashboard.refresh()

    print("WebSocket Broadcast...")

    dashboard.broadcast()

    print()

    print("Dashboard erfolgreich aktualisiert.")


if __name__ == "__main__":
    main()
