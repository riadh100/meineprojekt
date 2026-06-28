import asyncio
from datetime import datetime

from fastapi import APIRouter, WebSocket, WebSocketDisconnect


router = APIRouter()


class YasinStatisticsManager:
    """
    WebSocket für Live-Statistiken
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
        event: str,
        payload: dict,
    ):

        disconnected = []

        for connection in self.connections:

            try:
                await connection.send_json(
                    {
                        "event": event,
                        "timestamp": datetime.utcnow().isoformat(),
                        "payload": payload,
                    }
                )

            except Exception:
                disconnected.append(connection)

        for connection in disconnected:
            self.disconnect(connection)

    async def statistics_updated(
        self,
        statistics: dict,
    ):
        await self.broadcast(
            "STATISTICS_UPDATED",
            statistics,
        )

    async def performance_updated(
        self,
        performance: dict,
    ):
        await self.broadcast(
            "PERFORMANCE_UPDATED",
            performance,
        )

    async def drawdown_updated(
        self,
        drawdown: dict,
    ):
        await self.broadcast(
            "DRAWDOWN_UPDATED",
            drawdown,
        )

    async def equity_updated(
        self,
        equity: dict,
    ):
        await self.broadcast(
            "EQUITY_UPDATED",
            equity,
        )

    async def market_statistics_updated(
        self,
        market: dict,
    ):
        await self.broadcast(
            "MARKET_STATISTICS_UPDATED",
            market,
        )


manager = YasinStatisticsManager()


@router.websocket("/ws/yasin/statistics")
async def statistics_socket(
    websocket: WebSocket,
):
    """
    Live Statistik WebSocket.
    """

    await manager.connect(websocket)

    try:

        while True:
            await websocket.receive_text()

            await asyncio.sleep(0.1)

    except WebSocketDisconnect:
        manager.disconnect(websocket)
