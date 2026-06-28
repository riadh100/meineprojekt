from typing import List, Optional

from sqlalchemy.orm import Session

from app.yasin.models.yasin_market_snapshot_model import (
    YasinMarketSnapshotModel,
)


class YasinMarketSnapshotRepository:
    """
    Repository für Market Snapshots.

    Speichert den vollständigen Marktzustand
    zum Zeitpunkt der Signalerstellung.
    """

    def __init__(
        self,
        db: Session,
    ):
        self.db = db

    def create(
        self,
        snapshot: YasinMarketSnapshotModel,
    ) -> YasinMarketSnapshotModel:

        self.db.add(snapshot)
        self.db.commit()
        self.db.refresh(snapshot)

        return snapshot

    def get(
        self,
        snapshot_id: int,
    ) -> Optional[YasinMarketSnapshotModel]:

        return (
            self.db.query(
                YasinMarketSnapshotModel
            )
            .filter(
                YasinMarketSnapshotModel.id == snapshot_id
            )
            .first()
        )

    def get_by_signal(
        self,
        signal_id: int,
    ) -> Optional[YasinMarketSnapshotModel]:

        return (
            self.db.query(
                YasinMarketSnapshotModel
            )
            .filter(
                YasinMarketSnapshotModel.signal_id == signal_id
            )
            .first()
        )

    def get_by_symbol(
        self,
        symbol: str,
    ) -> List[YasinMarketSnapshotModel]:

        return (
            self.db.query(
                YasinMarketSnapshotModel
            )
            .filter(
                YasinMarketSnapshotModel.symbol == symbol
            )
            .order_by(
                YasinMarketSnapshotModel.created_at.desc()
            )
            .all()
        )

    def get_all(
        self,
    ) -> List[YasinMarketSnapshotModel]:

        return (
            self.db.query(
                YasinMarketSnapshotModel
            )
            .order_by(
                YasinMarketSnapshotModel.created_at.desc()
            )
            .all()
        )

    def delete(
        self,
        snapshot_id: int,
    ) -> bool:

        snapshot = self.get(snapshot_id)

        if snapshot is None:
            return False

        self.db.delete(snapshot)
        self.db.commit()

        return True

    def delete_by_signal(
        self,
        signal_id: int,
    ) -> int:

        deleted = (
            self.db.query(
                YasinMarketSnapshotModel
            )
            .filter(
                YasinMarketSnapshotModel.signal_id == signal_id
            )
            .delete()
        )

        self.db.commit()

        return deleted
