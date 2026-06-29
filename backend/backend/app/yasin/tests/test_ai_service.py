import pytest

from unittest.mock import Mock

from app.yasin.services.yasin_ai_service import (
    YasinAIService,
)


@pytest.fixture
def analysis():

    return Mock()


@pytest.fixture
def signal():

    return Mock()


@pytest.fixture
def monitor():

    return Mock()


@pytest.fixture
def statistics():

    return Mock()


@pytest.fixture
def dashboard():

    return Mock()


@pytest.fixture
def service(
    analysis,
    signal,
    monitor,
    statistics,
    dashboard,
):

    return YasinAIService(
        analysis_service=analysis,
        signal_service=signal,
        monitor_service=monitor,
        statistics_service=statistics,
        dashboard_service=dashboard,
    )


def test_run_analysis(
    service,
    analysis,
):

    analysis.run.return_value = []

    result = service.run_analysis()

    analysis.run.assert_called_once()

    assert result == []


def test_generate_signals(
    service,
    signal,
):

    service.generate_signals()

    signal.generate.assert_called_once()


def test_monitor_trades(
    service,
    monitor,
):

    service.monitor_trades()

    monitor.monitor.assert_called_once()


def test_update_statistics(
    service,
    statistics,
):

    service.update_statistics()

    statistics.rebuild_all.assert_called_once()


def test_update_dashboard(
    service,
    dashboard,
):

    service.update_dashboard()

    dashboard.refresh.assert_called_once()


def test_shutdown(
    service,
):

    service.shutdown()

    assert True
