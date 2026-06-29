"""
Startet den Yasin-AI-Server
mit FastAPI und Uvicorn.
"""

import uvicorn

from app.yasin.bootstrap.yasin_bootstrap import (
    YasinBootstrap,
)


def initialize():

    print("=" * 60)
    print("YASIN AI SERVER")
    print("=" * 60)

    print("\nInitialisiere System...")

    bootstrap = YasinBootstrap()

    bootstrap.start()

    print("Konfiguration geladen.")
    print("Datenbank verbunden.")
    print("Scheduler gestartet.")
    print("REST API aktiviert.")
    print("WebSocket aktiviert.")

    return bootstrap


def main():

    bootstrap = initialize()

    try:

        print("\nStarte FastAPI Server...")

        uvicorn.run(
            "app.main:app",
            host="0.0.0.0",
            port=8000,
            reload=False,
            workers=1,
        )

    except KeyboardInterrupt:

        print("\nServer wird beendet...")

    finally:

        bootstrap.shutdown()

        print("Server erfolgreich gestoppt.")


if __name__ == "__main__":

    main()
