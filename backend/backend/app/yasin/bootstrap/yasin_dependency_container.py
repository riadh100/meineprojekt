from sqlalchemy.orm import Session

from app.yasin.repositories.yasin_signal_repository import (
    YasinSignalRepository,
)
from app.yasin.repositories.yasin_trade_statistics_repository import (
    YasinTradeStatisticsRepository,
)
from app.yasin.repositories.yasin_strategy_config_repository import (
    YasinStrategyConfigRepository,
)
from app.yasin.repositories.yasin_trade_event_repository import (
    YasinTradeEventRepository,
)
from app.yasin.repositories.yasin_indicator_snapshot_repository import (
    YasinIndicatorSnapshotRepository,
)
from app.yasin.repositories.yasin_market_snapshot_repository import (
    YasinMarketSnapshotRepository,
)

from app.yasin.services.yasin_signal_service import (
    YasinSignalService,
)
from app.yasin.services.yasin_trade_event_service import (
    YasinTradeEventService,
)
from app.yasin.services.yasin_statistics_service_v2 import (
    YasinStatisticsServiceV2,
)
from app.yasin.services.yasin_strategy_service import (
    YasinStrategyService,
)
from app.yasin.services.yasin_market_analysis_service import (
    YasinMarketAnalysisService,
)
from app.yasin.services.yasin_risk_management_service import (
    YasinRiskManagementService,
)


class YasinDependencyContainer:
    """
    Zentraler Dependency Container
    für AI Empire Pro V9.

    Erstellt alle Repositories und Services
    einmalig und stellt sie der Anwendung
    zur Verfügung.
    """

    def __init__(
        self,
        db: Session,
    ):
        self.db = db

        # Repositories

        self.signal_repository = (
            YasinSignalRepository(db)
        )

        self.statistics_repository = (
            YasinTradeStatisticsRepository(db)
        )

        self.strategy_repository = (
            YasinStrategyConfigRepository(db)
        )

        self.trade_event_repository = (
            YasinTradeEventRepository(db)
        )

        self.indicator_snapshot_repository = (
            YasinIndicatorSnapshotRepository(db)
        )

        self.market_snapshot_repository = (
            YasinMarketSnapshotRepository(db)
        )

        # Services

        self.trade_event_service = (
            YasinTradeEventService(
                self.trade_event_repository
            )
        )

        self.market_analysis_service = (
            YasinMarketAnalysisService(
                market_provider=None,
            )
        )

        self.strategy_service = (
            YasinStrategyService(
                provider=None,
                repository=self.strategy_repository,
            )
        )

        self.risk_service = (
            YasinRiskManagementService()
        )

        self.signal_service = (
            YasinSignalService(
                repository=self.signal_repository,
                telegram=None,
                events=self.trade_event_service,
            )
        )

        self.statistics_service = (
            YasinStatisticsServiceV2(
                signal_repository=self.signal_repository,
                statistics_repository=self.statistics_repository,
            )
        )

    def repositories(self):

        return {
            "signal": self.signal_repository,
            "statistics": self.statistics_repository,
            "strategy": self.strategy_repository,
            "trade_events": self.trade_event_repository,
            "indicator_snapshots":
                self.indicator_snapshot_repository,
            "market_snapshots":
                self.market_snapshot_repository,
        }

    def services(self):

        return {
            "signal": self.signal_service,
            "statistics": self.statistics_service,
            "strategy": self.strategy_service,
            "market_analysis":
                self.market_analysis_service,
            "risk": self.risk_service,
            "trade_events":
                self.trade_event_service,
        }
