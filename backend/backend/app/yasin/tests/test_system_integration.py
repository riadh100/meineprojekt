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
def telegram():

    return Mock()


@pytest.fixture
def websocket():

    return Mock()


@pytest.fixture
def scheduler():

    return Mock()


@pytest.fixture
def service(
    analysis,
    signal,
    monitor,
    statistics,
    dashboard,
    telegram,
    websocket,
    scheduler,
):

    return YasinAIService(
        analysis_service=analysis,
        signal_service=signal,
        monitor_service=monitor,
        statistics_service=statistics,
        dashboard_service=dashboard,
        telegram_service=telegram,
        websocket_service=websocket,
        scheduler_service=scheduler,
    )


def test_full_analysis_cycle(
    service,
    analysis,
):

    service.run_analysis()

    analysis.run.assert_called_once()


def test_signal_pipeline(
    service,
    signal,
):

    service.generate_signals()

    signal.generate.assert_called_once()


def test_monitor_pipeline(
    service,
    monitor,
):

    service.monitor_trades()

    monitor.monitor.assert_called_once()


def test_statistics_pipeline(
    service,
    statistics,
):

    service.update_statistics()

    statistics.rebuild_all.assert_called_once()


def test_dashboard_pipeline(
    service,
    dashboard,
):

    service.update_dashboard()

    dashboard.refresh.assert_called_once()


def test_telegram_pipeline(
    service,
    telegram,
):

    service.send_reports()

    telegram.send_statistics.assert_called_once()


def test_websocket_pipeline(
    service,
    websocket,
):

    service.broadcast_dashboard()

    websocket.broadcast_dashboard.assert_called_once()


def test_scheduler_pipeline(
    service,
    scheduler,
):

    service.run_scheduler()

    scheduler.start.assert_called_once()


def test_system_status(
    service,
):

    result = service.status()

    assert result is not None
