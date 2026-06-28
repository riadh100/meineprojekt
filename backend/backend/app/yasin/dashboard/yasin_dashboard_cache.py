from datetime import datetime, timedelta
from threading import Lock


class YasinDashboardCache:
    """
    Cache für Dashboard-Daten.

    Reduziert Datenbankzugriffe und beschleunigt
    die Darstellung im Dashboard.
    """

    DEFAULT_TTL = 15  # Sekunden

    def __init__(
        self,
        ttl: int = DEFAULT_TTL,
    ):
        self.ttl = ttl

        self._lock = Lock()

        self._cache = None
        self._expires_at = None

    def has_valid_cache(self) -> bool:

        with self._lock:

            if self._cache is None:
                return False

            if self._expires_at is None:
                return False

            return (
                datetime.utcnow()
                < self._expires_at
            )

    def get(self):

        with self._lock:

            if not self.has_valid_cache():
                return None

            return self._cache

    def set(
        self,
        dashboard: dict,
    ):

        with self._lock:

            self._cache = dashboard

            self._expires_at = (
                datetime.utcnow()
                + timedelta(seconds=self.ttl)
            )

    def invalidate(self):

        with self._lock:

            self._cache = None
            self._expires_at = None

    def refresh(
        self,
        dashboard: dict,
    ):

        self.invalidate()
        self.set(dashboard)

    def expires_in(self) -> int:

        with self._lock:

            if self._expires_at is None:
                return 0

            seconds = int(
                (
                    self._expires_at
                    - datetime.utcnow()
                ).total_seconds()
            )

            return max(seconds, 0)

    def info(self):

        return {
            "cached": self.has_valid_cache(),
            "ttl": self.ttl,
            "expires_in": self.expires_in(),
        }
