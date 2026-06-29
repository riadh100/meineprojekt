"""
Unit-Tests für die
Utility-Funktionen.
"""

from app.yasin.utils import (
    utc_now,
    validate_market,
    validate_symbol,
    format_price,
    format_percent,
    sha256,
    round_price,
    calculate_percentage,
    to_json,
    from_json,
    normalize_market,
)


def test_datetime():

    now = utc_now()

    assert now is not None


def test_validate_market():

    assert validate_market("GOLD")
    assert not validate_market("UNKNOWN")


def test_validate_symbol():

    assert validate_symbol("XAUUSD")
    assert not validate_symbol("")


def test_format_price():

    assert (
        format_price(1234.567)
        == "1234.57"
    )


def test_format_percent():

    assert (
        format_percent(87.345)
        == "87.34%"
        or
        format_percent(87.345)
        == "87.35%"
    )


def test_sha256():

    value = sha256("hello")

    assert len(value) == 64


def test_round_price():

    assert (
        round_price(
            12.3456,
            2,
        )
        == 12.35
    )


def test_percentage():

    assert (
        calculate_percentage(
            25,
            100,
        )
        == 25.0
    )


def test_json():

    data = {
        "market": "GOLD",
    }

    encoded = to_json(data)

    decoded = from_json(encoded)

    assert decoded == data


def test_market_normalization():

    assert (
        normalize_market(
            "gold"
        )
        == "GOLD"
    )
