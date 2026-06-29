"""
Unit-Tests für den
YasinBacktestingService.
"""

import pytest

from app.yasin.backtesting.yasin_backtesting_service import (
    YasinBacktestingService,
)


@pytest.fixture
def service():

    return YasinBacktestingService()


def test_backtest_runs(service):

    result = service.run(
        market="GOLD",
        timeframe="15m",
        initial_balance=10000,
        strategy="Trend Following",
    )

    assert result is not None


def test_final_balance(service):

    result = service.run(
        market="GOLD",
        timeframe="15m",
        initial_balance=10000,
        strategy="Trend Following",
    )

    assert result.final_balance > 0


def test_win_rate(service):

    result = service.run(
        market="GOLD",
        timeframe="15m",
        initial_balance=10000,
        strategy="Trend Following",
    )

    assert (
        0
        <= result.win_rate
        <= 100
    )


def test_profit_factor(service):

    result = service.run(
        market="GOLD",
        timeframe="15m",
        initial_balance=10000,
        strategy="Trend Following",
    )

    assert result.profit_factor >= 0


def test_drawdown(service):

    result = service.run(
        market="GOLD",
        timeframe="15m",
        initial_balance=10000,
        strategy="Trend Following",
    )

    assert result.max_drawdown >= 0


def test_export(service):

    service.run(
        market="GOLD",
        timeframe="15m",
        initial_balance=10000,
        strategy="Trend Following",
    )

    service.export_json()
    service.export_csv()
    service.export_excel()
