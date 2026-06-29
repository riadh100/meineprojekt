"""
Startet den Demo-Modus
für Yasin AI.
"""

import time

from app.yasin.bootstrap.yasin_bootstrap import (
    YasinBootstrap,
)


def print_banner():

    print("=" * 60)
    print("YASIN AI DEMO MODE")
    print("=" * 60)


def simulate_dashboard():

    print("\nDashboard aktualisiert.")
    print("• Offene Trades : 2")
    print("• Neue Signale  : 3")
    print("• Winrate       : 78.4%")
    print("• Systemstatus  : ONLINE")


def simulate_signals():

    print("\nTrading-Signale")

    signals = [

        ("GOLD", "BUY", 2500.0),

        ("EURUSD", "SELL", 1.0845),

        ("BTCUSDT", "BUY", 64250.0),

    ]

    for market, direction, entry in signals:

        print(
            f"{market:10}"
            f"{direction:6}"
            f"{entry}"
        )


def simulate_websocket():

    print("\nWebSocket Broadcast...")

    time.sleep(1)

    print("Dashboard gesendet.")
    print("Signale gesendet.")


def simulate_telegram():

    print("\nTelegram Nachrichten...")

    print("✓ Signal gesendet")
    print("✓ Tagesbericht gesendet")
    print("✓ Health Report gesendet")


def main():

    print_banner()

    bootstrap = YasinBootstrap()

    print("\nSystem wird gestartet...")

    bootstrap.start()

    simulate_dashboard()

    simulate_signals()

    simulate_websocket()

    simulate_telegram()

    print("\nDemo erfolgreich abgeschlossen.")

    bootstrap.shutdown()


if __name__ == "__main__":

    main()
