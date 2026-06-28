from app.yasin.dashboard.yasin_dashboard_cache import (
    YasinDashboardCache,
)

from app.yasin.dashboard.yasin_dashboard_service import (
    YasinDashboardService,
)

from app.yasin.dashboard.yasin_dashboard_widgets import (
    YasinDashboardWidgets,
)

from app.yasin.websocket.yasin_dashboard_ws import (
    manager as dashboard_ws,
)


class YasinDashboardLiveUpdater:
    """
    Synchronisiert Dashboard, Cache und WebSocket.

    Aktualisiert automatisch das Dashboard
    nach Änderungen im Trading-System.
    """

    def __init__(
        self,
        dashboard_service: YasinDashboardService,
        cache: YasinDashboardCache,
    ):
        self.dashboard_service = dashboard_service
        self.cache = cache

    async def refresh(self):

        dashboard = self.dashboard_service.dashboard()

        self.cache.refresh(dashboard)

        widgets = YasinDashboardWidgets.dashboard(
            summary=dashboard["summary"],
            system=dashboard["system"],
            statistics=dashboard["statistics"],
            open_trades=dashboard["open_trades"],
            latest_signals=dashboard["latest_signals"],
        )

        await dashboard_ws.send_dashboard(
            widgets
        )

        return widgets

    async def signal_created(
        self,
    ):
        return await self.refresh()

    async def signal_updated(
        self,
    ):
        return await self.refresh()

    async def trade_closed(
        self,
    ):
        return await self.refresh()

    async def statistics_updated(
        self,
    ):
        return await self.refresh()

    async def tp1_reached(
        self,
    ):
        return await self.refresh()

    async def tp2_reached(
        self,
    ):
        return await self.refresh()

    async def tp3_reached(
        self,
    ):
        return await self.refresh()

    async def stop_loss_reached(
        self,
    ):
        return await self.refresh()

    async def force_refresh(
        self,
    ):
        return await self.refresh()
