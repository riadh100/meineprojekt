from app.yasin.services.yasin_ai_service import (
    YasinAIService,
)

from app.yasin.services.yasin_signal_service import (
    YasinSignalService,
)

from app.yasin.services.yasin_trade_event_service import (
    YasinTradeEventService,
)

from app.yasin.telegram.yasin_telegram_service import (
    YasinTelegramService,
)

from app.yasin.dashboard.yasin_dashboard_live_updater import (
    YasinDashboardLiveUpdater,
)


class YasinTradeMonitorJob:
    """
    Überwacht alle offenen Trades
    und verarbeitet TP/SL-Ereignisse.
    """

    def __init__(
        self,
        ai_service: YasinAIService,
        signal_service: YasinSignalService,
        event_service: YasinTradeEventService,
        telegram_service: YasinTelegramService,
        dashboard: YasinDashboardLiveUpdater,
    ):
        self.ai = ai_service
        self.signals = signal_service
        self.events = event_service
        self.telegram = telegram_service
        self.dashboard = dashboard

    async def run(self):

        open_trades = self.ai.get_open_trades()

        for trade in open_trades:

            current_price = (
                self.ai.get_live_price(
                    trade.symbol
                )
            )

            if current_price is None:
                continue

            await self._process_trade(
                trade,
                current_price,
            )

    async def _process_trade(
        self,
        trade,
        price: float,
    ):

        if trade.check_tp1(price):

            self.events.tp1(trade.id)

            self.telegram.send_tp1(trade)

            await self.dashboard.tp1_reached()

        if trade.check_tp2(price):

            self.events.tp2(trade.id)

            self.telegram.send_tp2(trade)

            await self.dashboard.tp2_reached()

        if trade.check_tp3(price):

            self.events.tp3(trade.id)

            self.telegram.send_tp3(trade)

            self.signals.close_trade(
                signal_id=trade.id,
                close_price=price,
                status="TP3",
                realized_profit=trade.calculate_profit(
                    price
                ),
                realized_profit_percent=(
                    trade.calculate_profit_percent(
                        price
                    )
                ),
            )

            await self.dashboard.trade_closed()

            return

        if trade.check_stop_loss(price):

            self.events.stop_loss(trade.id)

            self.telegram.send_stop_loss(
                trade
            )

            self.signals.close_trade(
                signal_id=trade.id,
                close_price=price,
                status="STOP_LOSS",
                realized_profit=trade.calculate_profit(
                    price
                ),
                realized_profit_percent=(
                    trade.calculate_profit_percent(
                        price
                    )
                ),
            )

            await self.dashboard.stop_loss_reached()
