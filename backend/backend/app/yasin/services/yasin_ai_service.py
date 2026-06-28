import logging
from typing import Optional

from app.yasin.services.yasin_bootstrap import YasinBootstrap
from app.yasin.services.yasin_scheduler import YasinScheduler


logger = logging.getLogger(__name__)


class YasinAIService:
    """
    Hauptservice von Yasin AI.

    Diese Klasse dient als zentraler Einstiegspunkt für
    Dashboard, REST API, WebSocket, Telegram Bot,
    Assistant und zukünftige Module.
    """

    def __init__(
        self,
        market_data_service,
        telegram_service,
        custom_strategy_configs=None,
    ):

        self.bootstrap = YasinBootstrap(
            market_data_service=market_data_service,
            telegram_service=telegram_service,
            custom_strategy_configs=custom_strategy_configs,
        )

        self.scheduler = YasinScheduler(
            bootstrap=self.bootstrap,
        )

    def start(self):
        logger.info("Starte Yasin AI...")
        self.scheduler.start()

    def stop(self):
        logger.info("Stoppe Yasin AI...")
        self.scheduler.stop()

    def analyze_now(self):
        """
        Führt sofort eine vollständige Analyse aller
        Strategien aus.
        """

        return self.bootstrap.get_orchestrator().run_strategies(
            self.bootstrap.get_strategies()
        )

    def monitor_now(self):
        """
        Überprüft sofort alle offenen Trades.
        """

        prices = {}

        provider = self.bootstrap.market_provider

        for strategy in self.bootstrap.get_strategies():
            prices[strategy.SYMBOL] = provider.get_latest_price(
                strategy.SYMBOL
            )

        self.bootstrap.get_trade_monitor().check_open_trades(
            prices
        )

    def get_statistics(self):
        return self.bootstrap.get_statistics().overview()

    def get_repository(self):
        return self.bootstrap.get_repository()

    def get_open_trades(self):
        return self.bootstrap.get_repository().open_trades()

    def get_closed_trades(self):
        return self.bootstrap.get_repository().closed_trades()

    def get_all_signals(self):
        return self.bootstrap.get_repository().all()

    def find_symbol(self, symbol: str):
        return self.bootstrap.get_repository().find_by_symbol(
            symbol
        )

    def latest_signal(self, symbol: str):
        return self.bootstrap.get_repository().find_latest_by_symbol(
            symbol
        )

    def scheduler_running(self) -> bool:
        return self.scheduler._running
