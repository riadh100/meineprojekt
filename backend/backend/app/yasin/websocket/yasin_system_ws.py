import asyncio
from datetime import datetime

from fastapi import APIRouter, WebSocket, WebSocketDisconnect


router = APIRouter()


class YasinSystemManager:
    """
    WebSocket für den Live-Systemstatus
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
        payload: dict,
    ):

        disconnected = []

        for connection in self.connections:

            try:
                await connection.send_json(payload)

            except Exception:
                disconnected.append(connection)

        for connection in disconnected:
            self.disconnect(connection)

    async def publish_status(
        self,
        *,
        scheduler_running: bool,
        active_strategies: int,
        open_trades: int,
        closed_trades: int,
        uptime_seconds: int,
    ):

        await self.broadcast(
            {
                "event": "SYSTEM_STATUS",
                "timestamp": datetime.utcnow().isoformat(),
                "data": {
                    "scheduler_running": scheduler_running,
                    "active_strategies": active_strategies,
                    "open_trades": open_trades,
                    "closed_trades": closed_trades,
                    "uptime_seconds": uptime_seconds,
                },
            }
        )

    async def publish_error(
        self,
        message: str,
    ):
        await self.broadcast(
            {
                "event": "SYSTEM_ERROR",
                "timestamp": datetime.utcnow().isoformat(),
                "message": message,
            }
        )


manager = YasinSystemManager()


@router.websocket("/ws/yasin/system")
async def system_socket(
    websocket: WebSocket,
):
    """
    Live-Systemstatus von Yasin AI.
    """

    await manager.connect(websocket)

    try:

        while True:
            await websocket.receive_text()

            await asyncio.sleep(0.1)

    except WebSocketDisconnect:
        manager.disconnect(websocket)
