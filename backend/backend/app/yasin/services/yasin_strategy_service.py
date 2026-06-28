from typing import Dict, List, Optional

from app.yasin.analysis.market_data_provider import (
    MarketDataProvider,
)

from app.yasin.repositories.yasin_strategy_config_repository import (
    YasinStrategyConfigRepository,
)

from app.yasin.strategies.crypto_strategy import (
    CryptoStrategy,
)
from app.yasin.strategies.forex_strategy import (
    ForexStrategy,
)
from app.yasin.strategies.gold_strategy import (
    GoldStrategy,
)
from app.yasin.strategies.nas100_strategy import (
    Nas100Strategy,
)
from app.yasin.strategies.custom.custom_strategy_factory import (
    CustomStrategyFactory,
)


class YasinStrategyService:
    """
    Verwaltet alle verfügbaren Strategien.

    Verantwortlich für:
    - Laden der Strategie-Konfigurationen
    - Erstellen der Strategien
    - Aktivieren / Deaktivieren
    - Bereitstellung für den Orchestrator
    """

    def __init__(
        self,
        provider: MarketDataProvider,
        repository: YasinStrategyConfigRepository,
    ):
        self.provider = provider
        self.repository = repository

        self.custom_factory = CustomStrategyFactory(
            provider
        )

        self._strategies: Dict[str, object] = {}

    def load(self) -> List[object]:

        self._strategies = {}

        self._strategies["GOLD"] = GoldStrategy(
            self.provider
        )

        self._strategies["NAS100"] = Nas100Strategy(
            self.provider
        )

        self._strategies["FOREX"] = ForexStrategy(
            self.provider
        )

        self._strategies["CRYPTO"] = CryptoStrategy(
            self.provider
        )

        configs = self.repository.get_enabled()

        custom = self.custom_factory.create_many(
            [
                {
                    "slot_name": c.name,
                    "symbol": c.symbol,
                    "timeframe": c.timeframe,
                    "enabled": c.enabled,
                    "buy_rsi_min": c.buy_rsi_min,
                    "buy_rsi_max": c.buy_rsi_max,
                    "sell_rsi_min": c.sell_rsi_min,
                    "sell_rsi_max": c.sell_rsi_max,
                    "sl_multiplier": c.stop_loss_multiplier,
                    "tp1_multiplier": c.tp1_multiplier,
                    "tp2_multiplier": c.tp2_multiplier,
                    "tp3_multiplier": c.tp3_multiplier,
                }
                for c in configs
                if c.market.startswith("CUSTOM")
            ]
        )

        for strategy in custom:
            self._strategies[
                strategy.slot_name
            ] = strategy

        return list(
            self._strategies.values()
        )

    def all(self) -> List[object]:
        return list(
            self._strategies.values()
        )

    def get(
        self,
        name: str,
    ) -> Optional[object]:
        return self._strategies.get(name)

    def reload(self) -> List[object]:
        return self.load()

    def count(self) -> int:
        return len(self._strategies)
