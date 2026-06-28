from collections import defaultdict
from typing import Dict, List

from fastapi import WebSocket


class YasinConnectionManager:
    """
    Zentraler WebSocket Connection Manager.

    Verwaltet alle WebSocket-Verbindungen
    von Yasin AI.
    """

    def __init__(self):
        self.channels: Dict[str, List[WebSocket]] = (
            defaultdict(list)
        )

    async def connect(
        self,
        channel: str,
        websocket: WebSocket,
    ):
        await websocket.accept()

        self.channels[channel].append(
            websocket
        )

    def disconnect(
        self,
        channel: str,
        websocket: WebSocket,
    ):

        if channel not in self.channels:
            return

        if websocket in self.channels[channel]:
            self.channels[channel].remove(
                websocket
            )

    async def broadcast(
        self,
        channel: str,
        payload: dict,
    ):

        if channel not in self.channels:
            return

        disconnected = []

        for websocket in self.channels[channel]:

            try:
                await websocket.send_json(
                    payload
                )

            except Exception:
                disconnected.append(
                    websocket
                )

        for websocket in disconnected:
            self.disconnect(
                channel,
                websocket,
            )

    async def broadcast_all(
        self,
        payload: dict,
    ):

        for channel in self.channels.keys():

            await self.broadcast(
                channel,
                payload,
            )

    def count(
        self,
        channel: str,
    ) -> int:

        return len(
            self.channels.get(
                channel,
                [],
            )
        )

    def total_connections(
        self,
    ) -> int:

        return sum(
            len(clients)
            for clients in self.channels.values()
        )

    def active_channels(
        self,
    ) -> list[str]:

        return list(
            self.channels.keys()
        )

    def clear(
        self,
    ):

        self.channels.clear()


connection_manager = YasinConnectionManager()
