"""
Datums- und Zeitfunktionen
für Yasin AI.
"""

from datetime import (
    datetime,
    timedelta,
    timezone,
)


UTC = timezone.utc


def utc_now() -> datetime:
    """Aktuelle UTC-Zeit."""
    return datetime.now(UTC)


def format_datetime(
    value: datetime,
    fmt: str = "%Y-%m-%d %H:%M:%S UTC",
) -> str:
    """Datetime formatieren."""
    return value.astimezone(UTC).strftime(fmt)


def parse_datetime(
    value: str,
    fmt: str = "%Y-%m-%d %H:%M:%S",
) -> datetime:
    """String in Datetime umwandeln."""
    return datetime.strptime(
        value,
        fmt,
    ).replace(
        tzinfo=UTC,
    )


def seconds_between(
    start: datetime,
    end: datetime,
) -> int:
    """Sekunden zwischen zwei Zeitpunkten."""
    return int(
        (end - start).total_seconds()
    )


def minutes_between(
    start: datetime,
    end: datetime,
) -> int:
    """Minuten zwischen zwei Zeitpunkten."""
    return (
        seconds_between(start, end) // 60
    )


def hours_between(
    start: datetime,
    end: datetime,
) -> float:
    """Stunden zwischen zwei Zeitpunkten."""
    return (
        end - start
    ).total_seconds() / 3600


def days_between(
    start: datetime,
    end: datetime,
) -> int:
    """Tage zwischen zwei Zeitpunkten."""
    return (end - start).days


def add_minutes(
    value: datetime,
    minutes: int,
) -> datetime:
    """Minuten hinzufügen."""
    return value + timedelta(
        minutes=minutes
    )


def add_hours(
    value: datetime,
    hours: int,
) -> datetime:
    """Stunden hinzufügen."""
    return value + timedelta(
        hours=hours
    )


def add_days(
    value: datetime,
    days: int,
) -> datetime:
    """Tage hinzufügen."""
    return value + timedelta(
        days=days
    )


def is_market_open(
    now: datetime | None = None,
) -> bool:
    """
    Vereinfachte Handelszeit:
    Montag–Freitag.
    """

    current = now or utc_now()

    return current.weekday() < 5
