from fastapi import APIRouter, WebSocket, WebSocketDisconnect


router = APIRouter()


class YasinDashboardManager:
    """
    WebSocket Manager für das komplette
    Yasin Dashboard.
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

    async def send_dashboard(
        self,
        dashboard: dict,
    ):

        disconnected = []

        for connection in self.connections:

            try:
                await connection.send_json(
                    {
                        "event": "DASHBOARD_UPDATE",
                        "payload": dashboard,
                    }
                )

            except Exception:
                disconnected.append(connection)

        for connection in disconnected:
            self.disconnect(connection)

    async def system_status(
        self,
        status: dict,
    ):
        await self.send_dashboard(
            {
                "type": "system",
                "data": status,
            }
        )

    async def statistics(
        self,
        statistics: dict,
    ):
        await self.send_dashboard(
            {
                "type": "statistics",
                "data": statistics,
            }
        )

    async def open_trades(
        self,
        trades: list,
    ):
        await self.send_dashboard(
            {
                "type": "open_trades",
                "data": trades,
            }
        )

    async def latest_signals(
        self,
        signals: list,
    ):
        await self.send_dashboard(
            {
                "type": "latest_signals",
                "data": signals,
            }
        )

    async def performance(
        self,
        performance: dict,
    ):
        await self.send_dashboard(
            {
                "type": "performance",
                "data": performance,
            }
        )


manager = YasinDashboardManager()


@router.websocket("/ws/yasin/dashboard")
async def dashboard_socket(
    websocket: WebSocket,
):
    """
    Dashboard Live WebSocket.
    """

    await manager.connect(websocket)

    try:

        while True:
            await websocket.receive_text()

    except WebSocketDisconnect:
        manager.disconnect(websocket)
