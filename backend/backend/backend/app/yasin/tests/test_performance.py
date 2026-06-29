import time
import pytest

from unittest.mock import Mock

from app.yasin.services.yasin_ai_service import (
    YasinAIService,
)


@pytest.fixture
def service():

    return YasinAIService(
        analysis_service=Mock(),
        signal_service=Mock(),
        monitor_service=Mock(),
        statistics_service=Mock(),
        dashboard_service=Mock(),
    )


def test_analysis_speed(
    service,
):

    start = time.perf_counter()

    service.run_analysis()

    duration = (
        time.perf_counter()
        - start
    )

    assert duration < 1.0


def test_signal_generation_speed(
    service,
):

    start = time.perf_counter()

    service.generate_signals()

    duration = (
        time.perf_counter()
        - start
    )

    assert duration < 1.0


def test_dashboard_refresh_speed(
    service,
):

    start = time.perf_counter()

    service.update_dashboard()

    duration = (
        time.perf_counter()
        - start
    )

    assert duration < 1.0


def test_statistics_speed(
    service,
):

    start = time.perf_counter()

    service.update_statistics()

    duration = (
        time.perf_counter()
        - start
    )

    assert duration < 1.0


def test_multiple_analysis_cycles(
    service,
):

    for _ in range(100):

        service.run_analysis()

    assert True


def test_multiple_dashboard_updates(
    service,
):

    for _ in range(100):

        service.update_dashboard()

    assert True


def test_service_status(
    service,
):

    assert service.status() is not None
