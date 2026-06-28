from typing import List, Optional

from sqlalchemy.orm import Session

from app.yasin.models.yasin_indicator_snapshot_model import (
    YasinIndicatorSnapshotModel,
)


class YasinIndicatorSnapshotRepository:
    """
    Repository für Indikator-Snapshots.

    Speichert alle technischen Indikatoren, die
    bei der Erstellung eines Signals berechnet wurden.
    """

    def __init__(
        self,
        db: Session,
    ):
        self.db = db

    def create(
        self,
        snapshot: YasinIndicatorSnapshotModel,
    ) -> YasinIndicatorSnapshotModel:

        self.db.add(snapshot)
        self.db.commit()
        self.db.refresh(snapshot)

        return snapshot

    def get(
        self,
        snapshot_id: int,
    ) -> Optional[YasinIndicatorSnapshotModel]:

        return (
            self.db.query(
                YasinIndicatorSnapshotModel
            )
            .filter(
                YasinIndicatorSnapshotModel.id == snapshot_id
            )
            .first()
        )

    def get_by_signal(
        self,
        signal_id: int,
    ) -> Optional[YasinIndicatorSnapshotModel]:

        return (
            self.db.query(
                YasinIndicatorSnapshotModel
            )
            .filter(
                YasinIndicatorSnapshotModel.signal_id == signal_id
            )
            .first()
        )

    def get_by_symbol(
        self,
        symbol: str,
    ) -> List[YasinIndicatorSnapshotModel]:

        return (
            self.db.query(
                YasinIndicatorSnapshotModel
            )
            .filter(
                YasinIndicatorSnapshotModel.symbol == symbol
            )
            .order_by(
                YasinIndicatorSnapshotModel.created_at.desc()
            )
            .all()
        )

    def get_all(
        self,
    ) -> List[YasinIndicatorSnapshotModel]:

        return (
            self.db.query(
                YasinIndicatorSnapshotModel
            )
            .order_by(
                YasinIndicatorSnapshotModel.created_at.desc()
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
                YasinIndicatorSnapshotModel
            )
            .filter(
                YasinIndicatorSnapshotModel.signal_id == signal_id
            )
            .delete()
        )

        self.db.commit()

        return deleted
