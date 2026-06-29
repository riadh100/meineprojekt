from datetime import datetime, timedelta, timezone


UTC = timezone.utc


def utc_now() -> datetime:
    """
    Aktuelle UTC-Zeit.
    """
    return datetime.now(UTC)


def utc_timestamp() -> str:
    """
    ISO-8601 UTC-Zeitstempel.
    """
    return utc_now().isoformat()


def unix_timestamp() -> int:
    """
    Unix Timestamp.
    """
    return int(
        utc_now().timestamp()
    )


def is_weekend(
    dt: datetime | None = None,
) -> bool:

    dt = dt or utc_now()

    return dt.weekday() >= 5


def trading_day(
    dt: datetime | None = None,
) -> bool:

    return not is_weekend(dt)


def london_session(
    dt: datetime | None = None,
) -> bool:

    dt = dt or utc_now()

    return 8 <= dt.hour < 17


def new_york_session(
    dt: datetime | None = None,
) -> bool:

    dt = dt or utc_now()

    return 13 <= dt.hour < 22


def tokyo_session(
    dt: datetime | None = None,
) -> bool:

    dt = dt or utc_now()

    return 0 <= dt.hour < 9


def sydney_session(
    dt: datetime | None = None,
) -> bool:

    dt = dt or utc_now()

    return (
        dt.hour >= 21
        or dt.hour < 6
    )


def current_sessions():

    return {
        "london": london_session(),
        "new_york": new_york_session(),
        "tokyo": tokyo_session(),
        "sydney": sydney_session(),
    }


def minutes_ago(
    minutes: int,
):

    return utc_now() - timedelta(
        minutes=minutes
    )


def hours_ago(
    hours: int,
):

    return utc_now() - timedelta(
        hours=hours
    )


def days_ago(
    days: int,
):

    return utc_now() - timedelta(
        days=days
    )


def seconds_until(
    dt: datetime,
):

    return max(
        int(
            (
                dt - utc_now()
            ).total_seconds()
        ),
        0,
    )
