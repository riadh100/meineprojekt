from fastapi import APIRouter, WebSocket, WebSocketDisconnect

router = APIRouter()


class YasinLiveSignalManager:
    """
    Verwaltet alle WebSocket-Verbindungen
    für Live-Signale.
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
        message: dict,
    ):
        disconnected = []

        for connection in self.connections:

            try:
                await connection.send_json(message)

            except Exception:
                disconnected.append(connection)

        for connection in disconnected:
            self.disconnect(connection)

    async def signal_created(
        self,
        signal: dict,
    ):
        await self.broadcast(
            {
                "event": "SIGNAL_CREATED",
                "payload": signal,
            }
        )

    async def tp1(
        self,
        signal: dict,
    ):
        await self.broadcast(
            {
                "event": "TP1_REACHED",
                "payload": signal,
            }
        )

    async def tp2(
        self,
        signal: dict,
    ):
        await self.broadcast(
            {
                "event": "TP2_REACHED",
                "payload": signal,
            }
        )

    async def tp3(
        self,
        signal: dict,
    ):
        await self.broadcast(
            {
                "event": "TP3_REACHED",
                "payload": signal,
            }
        )

    async def stop_loss(
        self,
        signal: dict,
    ):
        await self.broadcast(
            {
                "event": "STOP_LOSS",
                "payload": signal,
            }
        )

    async def trade_closed(
        self,
        signal: dict,
    ):
        await self.broadcast(
            {
                "event": "TRADE_CLOSED",
                "payload": signal,
            }
        )


manager = YasinLiveSignalManager()


@router.websocket("/ws/yasin/live-signals")
async def live_signal_socket(
    websocket: WebSocket,
):
    """
    Live-WebSocket für neue Signale
    und Trade-Updates.
    """

    await manager.connect(websocket)

    try:

        while True:
            await websocket.receive_text()

    except WebSocketDisconnect:
        manager.disconnect(websocket)
