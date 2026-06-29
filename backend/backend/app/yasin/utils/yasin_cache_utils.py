from datetime import datetime, timedelta


class CacheEntry:
    """
    Repräsentiert einen Cache-Eintrag.
    """

    def __init__(
        self,
        key: str,
        value,
        ttl: int,
    ):
        self.key = key
        self.value = value
        self.created_at = datetime.utcnow()
        self.expires_at = (
            self.created_at
            + timedelta(seconds=ttl)
        )

    def expired(self) -> bool:

        return (
            datetime.utcnow()
            >= self.expires_at
        )

    def remaining_seconds(self):

        return max(
            int(
                (
                    self.expires_at
                    - datetime.utcnow()
                ).total_seconds()
            ),
            0,
        )


class CacheUtils:
    """
    Allgemeine Cache-Hilfsfunktionen.
    """

    def __init__(self):
        self.cache = {}

    def get(
        self,
        key: str,
    ):

        item = self.cache.get(key)

        if item is None:
            return None

        if item.expired():

            del self.cache[key]

            return None

        return item.value

    def set(
        self,
        key: str,
        value,
        ttl: int = 60,
    ):

        self.cache[key] = CacheEntry(
            key,
            value,
            ttl,
        )

    def invalidate(
        self,
        key: str,
    ):

        self.cache.pop(
            key,
            None,
        )

    def clear(self):

        self.cache.clear()

    def cleanup(self):

        expired = [

            key

            for key, item

            in self.cache.items()

            if item.expired()

        ]

        for key in expired:

            del self.cache[key]

    def stats(self):

        self.cleanup()

        return {

            "entries": len(self.cache),

            "keys": list(
                self.cache.keys()
            ),

        }

    @staticmethod
    def dashboard_key():

        return "dashboard"

    @staticmethod
    def statistics_key():

        return "statistics"

    @staticmethod
    def analysis_key(
        symbol: str,
        timeframe: str,
    ):

        return (
            f"analysis:"
            f"{symbol}:"
            f"{timeframe}"
        )
