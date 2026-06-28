from app.yasin.strategies.custom.custom_strategy_base import (
    CustomStrategyBase,
)


class CustomStrategyFactory:
    """
    Erstellt frei konfigurierbare Custom-Strategien
    für Yasin AI.
    """

    def __init__(self, market_provider):
        self.market_provider = market_provider

    def create(self, config: dict) -> CustomStrategyBase:
        return CustomStrategyBase(
            market_provider=self.market_provider,
            slot_name=config["slot_name"],
            symbol=config["symbol"],
            timeframe=config.get("timeframe", "15m"),
            config=config,
        )

    def create_many(self, configs: list) -> list[CustomStrategyBase]:
        return [
            self.create(config)
            for config in configs
            if config.get("enabled", True)
        ]
