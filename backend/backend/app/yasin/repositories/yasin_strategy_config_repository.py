from typing import List, Optional

from sqlalchemy.orm import Session

from app.yasin.models.yasin_strategy_config_model import (
    YasinStrategyConfigModel,
)


class YasinStrategyConfigRepository:
    """
    Repository für Yasin-Strategie-Konfigurationen.
    """

    def __init__(self, db: Session):
        self.db = db

    def create(
        self,
        config: YasinStrategyConfigModel,
    ) -> YasinStrategyConfigModel:

        self.db.add(config)
        self.db.commit()
        self.db.refresh(config)

        return config

    def update(
        self,
        config: YasinStrategyConfigModel,
    ) -> YasinStrategyConfigModel:

        self.db.commit()
        self.db.refresh(config)

        return config

    def get(
        self,
        config_id: int,
    ) -> Optional[YasinStrategyConfigModel]:

        return (
            self.db.query(YasinStrategyConfigModel)
            .filter(YasinStrategyConfigModel.id == config_id)
            .first()
        )

    def get_by_name(
        self,
        name: str,
    ) -> Optional[YasinStrategyConfigModel]:

        return (
            self.db.query(YasinStrategyConfigModel)
            .filter(YasinStrategyConfigModel.name == name)
            .first()
        )

    def get_enabled(self) -> List[YasinStrategyConfigModel]:

        return (
            self.db.query(YasinStrategyConfigModel)
            .filter(YasinStrategyConfigModel.enabled.is_(True))
            .order_by(YasinStrategyConfigModel.market.asc())
            .all()
        )

    def get_all(self) -> List[YasinStrategyConfigModel]:

        return (
            self.db.query(YasinStrategyConfigModel)
            .order_by(YasinStrategyConfigModel.market.asc())
            .all()
        )

    def enable(
        self,
        config_id: int,
    ) -> Optional[YasinStrategyConfigModel]:

        config = self.get(config_id)

        if config is None:
            return None

        config.enabled = True

        return self.update(config)

    def disable(
        self,
        config_id: int,
    ) -> Optional[YasinStrategyConfigModel]:

        config = self.get(config_id)

        if config is None:
            return None

        config.enabled = False

        return self.update(config)

    def delete(
        self,
        config_id: int,
    ) -> bool:

        config = self.get(config_id)

        if config is None:
            return False

        self.db.delete(config)
        self.db.commit()

        return True
