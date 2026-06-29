import pytest

from unittest.mock import Mock

from app.yasin.backtesting.yasin_backtesting_service import (
    YasinBacktestingService,
)


@pytest.fixture
def strategy():

    return Mock()


@pytest.fixture
def statistics():

    return Mock()


@pytest.fixture
def repository():

    return Mock()


@pytest.fixture
def service(
    strategy,
    statistics,
    repository,
):

    return YasinBacktestingService(
        strategy_service=strategy,
        statistics_service=statistics,
        repository=repository,
    )


def test_run_backtest(
    service,
    strategy,
):

    strategy.run.return_value = []

    result = service.run(
        market="GOLD",
        timeframe="15m",
    )

    assert result is not None


def test_equity_curve(
    service,
):

    curve = service.equity_curve()

    assert isinstance(
        curve,
        list,
    )


def test_profit_factor(
    service,
):

    result = service.profit_factor()

    assert result >= 0


def test_drawdown(
    service,
):

    result = service.max_drawdown()

    assert result >= 0


def test_statistics(
    service,
    statistics,
):

    service.update_statistics()

    statistics.rebuild_all.assert_called_once()


def test_export_results(
    service,
    repository,
):

    service.export_json()

    repository.export_json.assert_called_once()


def test_backtest_status(
    service,
):

    result = service.status()

    assert result is not None
