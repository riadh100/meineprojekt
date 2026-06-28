from fastapi import FastAPI

from app.yasin.api.yasin_backtesting_router import router as backtesting_router
from app.yasin.api.yasin_dashboard_router import router as dashboard_router
from app.yasin.api.yasin_monitoring_router import router as monitoring_router
from app.yasin.api.yasin_signal_router import router as signal_router
from app.yasin.api.yasin_statistics_router import router as statistics_router
from app.yasin.api.yasin_strategy_router import router as strategy_router
from app.yasin.api.yasin_system_router import router as system_router

from app.yasin.websocket.yasin_dashboard_ws import router as dashboard_ws
from app.yasin.websocket.yasin_live_signal_ws import router as signal_ws
from app.yasin.websocket.yasin_notification_ws import router as notification_ws
from app.yasin.websocket.yasin_statistics_ws import router as statistics_ws
from app.yasin.websocket.yasin_system_ws import router as system_ws


class YasinModule:
    """
    Bootstrap-Modul für Yasin AI.

    Registriert alle Router und
    WebSocket-Endpunkte in AI Empire Pro V9.
    """

    def __init__(
        self,
        app: FastAPI,
    ):
        self.app = app

    def register(self):

        self._register_rest_api()
        self._register_websockets()

        return self.app

    def _register_rest_api(self):

        self.app.include_router(
            signal_router
        )

        self.app.include_router(
            statistics_router
        )

        self.app.include_router(
            strategy_router
        )

        self.app.include_router(
            monitoring_router
        )

        self.app.include_router(
            dashboard_router
        )

        self.app.include_router(
            system_router
        )

        self.app.include_router(
            backtesting_router
        )

    def _register_websockets(self):

        self.app.include_router(
            signal_ws
        )

        self.app.include_router(
            dashboard_ws
        )

        self.app.include_router(
            statistics_ws
        )

        self.app.include_router(
            notification_ws
        )

        self.app.include_router(
            system_ws
        )
