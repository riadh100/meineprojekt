"""
Beispiel für den WebSocket-Service
von Yasin AI.
"""

import asyncio

from app.yasin.websocket.yasin_websocket_service import (
    YasinWebSocketService,
)


async def main():

    websocket = YasinWebSocketService()

    print("=" * 60)
    print("YASIN AI WEBSOCKET")
    print("=" * 60)

    print("\nWebSocket-Service wird gestartet...")

    # Beispiel-Dashboard
    dashboard = {
        "status": "ONLINE",
        "signals": 5,
        "open_trades": 2,
        "win_rate": 78.4,
    }

    # Beispiel-Signal
    signal = {
        "market": "GOLD",
        "symbol": "XAUUSD",
        "direction": "BUY",
        "entry": 2500.00,
        "quality": 95.8,
    }

    print("\nDashboard senden...")
    await websocket.broadcast_dashboard(
        dashboard
    )

    print("Signal senden...")
    await websocket.broadcast_signal(
        signal
    )

    print("Systemstatus senden...")
    await websocket.broadcast_system(
        {
            "status": "RUNNING",
            "uptime": "2h 15m",
        }
    )

    print()

    print(
        "Aktive Verbindungen:",
        websocket.connection_count(),
    )

    print("\nWebSocket-Demo abgeschlossen.")


if __name__ == "__main__":
    asyncio.run(main())
