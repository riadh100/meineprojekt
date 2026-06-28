from datetime import datetime

from fastapi import APIRouter, WebSocket, WebSocketDisconnect


router = APIRouter()


class YasinNotificationManager:
    """
    Verwaltet alle Live-Benachrichtigungen
    von Yasin AI.
    """

    def __init__(self):
        self.connections: list[WebSocket] = []

    async def connect(
        self,
        websocket: WebSocket,
    ):
        await websocket.accept()
        self.connections.append(websocket)

    def disconnect(
        self,
        websocket: WebSocket,
    ):
        if websocket in self.connections:
            self.connections.remove(websocket)

    async def broadcast(
        self,
        level: str,
        title: str,
        message: str,
        data: dict | None = None,
    ):

        payload = {
            "event": "NOTIFICATION",
            "timestamp": datetime.utcnow().isoformat(),
            "level": level,
            "title": title,
            "message": message,
            "data": data or {},
        }

        disconnected = []

        for connection in self.connections:

            try:
                await connection.send_json(payload)

            except Exception:
                disconnected.append(connection)

        for connection in disconnected:
            self.disconnect(connection)

    async def signal(
        self,
        signal: dict,
    ):
        await self.broadcast(
            level="success",
            title="Neues Signal",
            message=f"{signal['symbol']} Signal erstellt",
            data=signal,
        )

    async def trade_closed(
        self,
        trade: dict,
    ):
        await self.broadcast(
            level="info",
            title="Trade abgeschlossen",
            message=f"{trade['symbol']} Trade beendet",
            data=trade,
        )

    async def warning(
        self,
        message: str,
    ):
        await self.broadcast(
            level="warning",
            title="Warnung",
            message=message,
        )

    async def error(
        self,
        message: str,
    ):
        await self.broadcast(
            level="error",
            title="Fehler",
            message=message,
        )

    async def system(
        self,
        message: str,
    ):
        await self.broadcast(
            level="system",
            title="System",
            message=message,
        )


manager = YasinNotificationManager()


@router.websocket("/ws/yasin/notifications")
async def notification_socket(
    websocket: WebSocket,
):
    """
    Live Notification WebSocket.
    """

    await manager.connect(websocket)

    try:

        while True:
            await websocket.receive_text()

    except WebSocketDisconnect:
        manager.disconnect(websocket)
