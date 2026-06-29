import pytest

from unittest.mock import Mock

from app.yasin.services.yasin_dashboard_service import (
    YasinDashboardService,
)


@pytest.fixture
def dashboard_repository():

    return Mock()


@pytest.fixture
def cache():

    return Mock()


@pytest.fixture
def websocket():

    return Mock()


@pytest.fixture
def statistics():

    return Mock()


@pytest.fixture
def service(
    dashboard_repository,
    cache,
    websocket,
    statistics,
):

    return YasinDashboardService(
        dashboard_repository=dashboard_repository,
        dashboard_cache=cache,
        websocket_manager=websocket,
        statistics_service=statistics,
    )


def test_refresh_dashboard(
    service,
    cache,
):

    service.refresh()

    cache.invalidate.assert_called_once()


def test_get_dashboard(
    service,
    dashboard_repository,
):

    dashboard = Mock()

    dashboard_repository.get_dashboard.return_value = dashboard

    result = service.get_dashboard()

    assert result == dashboard


def test_update_cache(
    service,
    cache,
):

    service.update_cache()

    cache.refresh.assert_called_once()


def test_broadcast_dashboard(
    service,
    websocket,
):

    service.broadcast()

    websocket.broadcast_dashboard.assert_called_once()


def test_statistics_refresh(
    service,
    statistics,
):

    service.refresh_statistics()

    statistics.rebuild_all.assert_called_once()


def test_dashboard_status(
    service,
):

    result = service.status()

    assert result is not None
