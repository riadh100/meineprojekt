import pytest

from unittest.mock import Mock

from app.yasin.scheduler.yasin_scheduler_service import (
    YasinSchedulerService,
)


@pytest.fixture
def analysis():

    return Mock()


@pytest.fixture
def monitor():

    return Mock()


@pytest.fixture
def statistics():

    return Mock()


@pytest.fixture
def telegram():

    return Mock()


@pytest.fixture
def scheduler():

    return Mock()


@pytest.fixture
def service(
    analysis,
    monitor,
    statistics,
    telegram,
    scheduler,
):

    return YasinSchedulerService(
        analysis_service=analysis,
        monitor_service=monitor,
        statistics_service=statistics,
        telegram_service=telegram,
        scheduler=scheduler,
    )


def test_start_scheduler(
    service,
    scheduler,
):

    service.start()

    scheduler.start.assert_called_once()


def test_stop_scheduler(
    service,
    scheduler,
):

    service.stop()

    scheduler.shutdown.assert_called_once()


def test_run_analysis_job(
    service,
    analysis,
):

    service.run_analysis()

    analysis.run.assert_called_once()


def test_run_monitor_job(
    service,
    monitor,
):

    service.run_monitor()

    monitor.monitor.assert_called_once()


def test_run_statistics_job(
    service,
    statistics,
):

    service.run_statistics()

    statistics.rebuild_all.assert_called_once()


def test_run_telegram_job(
    service,
    telegram,
):

    service.run_telegram()

    telegram.send_statistics.assert_called_once()


def test_scheduler_status(
    service,
):

    result = service.status()

    assert result is not None
