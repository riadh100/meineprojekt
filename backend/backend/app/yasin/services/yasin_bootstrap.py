from app.yasin.analysis.market_data_provider import MarketDataProvider

from app.yasin.signals.signal_repository import SignalRepository

from app.yasin.telegram.yasin_telegram_sender import (
    YasinTelegramSender,
)

from app.yasin.monitoring.trade_monitor import TradeMonitor

from app.yasin.statistics.yasin_statistics_service import (
    YasinStatisticsService,
)

from app.yasin.services.yasin_orchestrator import (
    YasinOrchestrator,
)

from app.yasin.strategies.gold_strategy import GoldStrategy
from app.yasin.strategies.nas100_strategy import Nas100Strategy
from app.yasin.strategies.forex_strategy import ForexStrategy
from app.yasin.strategies.crypto_strategy import CryptoStrategy

from app.yasin.strategies.custom.custom_strategy_factory import (
    CustomStrategyFactory,
)


class YasinBootstrap:
    """
    Erstellt alle Yasin-Komponenten und verbindet sie
    mit den bestehenden Services aus AI Empire Pro V8.
    """

    def __init__(
        self,
        market_data_service,
        telegram_service,
        custom_strategy_configs=None,
    ):

        if custom_strategy_configs is None:
            custom_strategy_configs = []

        self.market_provider = MarketDataProvider(
            market_data_service
        )

        self.repository = SignalRepository()

        self.telegram_sender = YasinTelegramSender(
            telegram_service=telegram_service,
            repository=self.repository,
        )

        self.trade_monitor = TradeMonitor(
            repository=self.repository,
            telegram_sender=self.telegram_sender,
        )

        self.statistics = YasinStatisticsService(
            repository=self.repository,
        )

        self.orchestrator = YasinOrchestrator(
            repository=self.repository,
            telegram_sender=self.telegram_sender,
        )

        self.custom_factory = CustomStrategyFactory(
            self.market_provider,
        )

        self.strategies = [
            GoldStrategy(self.market_provider),
            Nas100Strategy(self.market_provider),
            ForexStrategy(self.market_provider),
            CryptoStrategy(self.market_provider),
        ]

        self.strategies.extend(
            self.custom_factory.create_many(
                custom_strategy_configs
            )
        )

    def get_orchestrator(self):
        return self.orchestrator

    def get_trade_monitor(self):
        return self.trade_monitor

    def get_statistics(self):
        return self.statistics

    def get_repository(self):
        return self.repository

    def get_strategies(self):
        return self.strategies
