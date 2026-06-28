from app.yasin.services.yasin_market_analysis_service import (
    YasinMarketAnalysisService,
)

from app.yasin.services.yasin_signal_service import (
    YasinSignalService,
)

from app.yasin.services.yasin_strategy_service import (
    YasinStrategyService,
)


class YasinMarketAnalysisJob:
    """
    Führt die automatische Marktanalyse
    für alle aktivierten Strategien aus.
    """

    def __init__(
        self,
        strategy_service: YasinStrategyService,
        analysis_service: YasinMarketAnalysisService,
        signal_service: YasinSignalService,
    ):
        self.strategy_service = strategy_service
        self.analysis_service = analysis_service
        self.signal_service = signal_service

    def run(self):

        created_signals = []

        strategies = self.strategy_service.all()

        for strategy in strategies:

            if hasattr(strategy, "enabled"):

                if not strategy.enabled:
                    continue

            analysis = self.analysis_service.analyze(
                symbol=strategy.symbol,
                timeframe=strategy.timeframe,
            )

            signal = strategy.generate_signal(
                analysis
            )

            if signal is None:
                continue

            stored = self.signal_service.create(
                signal
            )

            if stored.is_approved:
                self.signal_service.publish(
                    stored
                )

            created_signals.append(
                stored
            )

        return created_signals

    def run_market(
        self,
        market: str,
    ):

        strategies = self.strategy_service.all()

        for strategy in strategies:

            if strategy.market.upper() != market.upper():
                continue

            analysis = self.analysis_service.analyze(
                symbol=strategy.symbol,
                timeframe=strategy.timeframe,
            )

            signal = strategy.generate_signal(
                analysis
            )

            if signal is None:
                return None

            signal = self.signal_service.create(
                signal
            )

            if signal.is_approved:
                self.signal_service.publish(
                    signal
                )

            return signal

        return None

    def active_markets(self):

        return [
            strategy.market
            for strategy in self.strategy_service.all()
        ]

    def active_symbols(self):

        return [
            strategy.symbol
            for strategy in self.strategy_service.all()
        ]
