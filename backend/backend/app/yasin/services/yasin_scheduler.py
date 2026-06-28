import logging
import threading
import time

from app.yasin.services.yasin_bootstrap import YasinBootstrap


logger = logging.getLogger(__name__)


class YasinScheduler:
    """
    Führt Yasin AI automatisch aus.

    Aufgaben:
    - Strategien analysieren
    - Signale erzeugen
    - Telegram informieren
    - Offene Trades überwachen
    """

    def __init__(
        self,
        bootstrap: YasinBootstrap,
        analysis_interval: int = 60,
        monitoring_interval: int = 10,
    ):
        self.bootstrap = bootstrap

        self.analysis_interval = analysis_interval
        self.monitoring_interval = monitoring_interval

        self._running = False

    def start(self):
        if self._running:
            return

        self._running = True

        threading.Thread(
            target=self._analysis_loop,
            daemon=True,
        ).start()

        threading.Thread(
            target=self._monitor_loop,
            daemon=True,
        ).start()

        logger.info("Yasin Scheduler gestartet.")

    def stop(self):
        self._running = False
        logger.info("Yasin Scheduler gestoppt.")

    def _analysis_loop(self):
        orchestrator = self.bootstrap.get_orchestrator()
        strategies = self.bootstrap.get_strategies()

        while self._running:

            try:
                signals = orchestrator.run_strategies(
                    strategies
                )

                if signals:
                    logger.info(
                        "%s neue Signale erstellt.",
                        len(signals),
                    )

            except Exception as exc:
                logger.exception(exc)

            time.sleep(self.analysis_interval)

    def _monitor_loop(self):
        trade_monitor = self.bootstrap.get_trade_monitor()
        provider = self.bootstrap.market_provider

        while self._running:

            try:

                prices = {}

                for strategy in self.bootstrap.get_strategies():

                    prices[strategy.SYMBOL] = (
                        provider.get_latest_price(
                            strategy.SYMBOL
                        )
                    )

                trade_monitor.check_open_trades(
                    prices
                )

            except Exception as exc:
                logger.exception(exc)

            time.sleep(self.monitoring_interval)
