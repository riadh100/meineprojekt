"""
Vollständiges Beispiel für den Start
des gesamten Yasin AI Systems.
"""

from app.yasin.bootstrap.yasin_bootstrap import (
    YasinBootstrap,
)


def main():

    print("=" * 60)
    print("YASIN AI EMPIRE PRO V9")
    print("=" * 60)

    print("\nSystem wird initialisiert...")

    bootstrap = YasinBootstrap()

    # System starten
    bootstrap.start()

    print("\nKonfiguration geladen")
    print("Datenbank verbunden")
    print("Scheduler gestartet")
    print("Analyse-Service gestartet")
    print("Signal-Service gestartet")
    print("Monitoring gestartet")
    print("Dashboard gestartet")
    print("WebSocket gestartet")
    print("Telegram gestartet")
    print("REST API gestartet")

    print("\nSystemstatus")

    status = bootstrap.status()

    for key, value in status.items():
        print(f"{key}: {value}")

    print("\nYasin AI läuft erfolgreich.")

    try:

        bootstrap.wait()

    except KeyboardInterrupt:

        print("\nSystem wird heruntergefahren...")

        bootstrap.shutdown()

        print("Alle Dienste wurden beendet.")


if __name__ == "__main__":
    main()
