import pytest

from unittest.mock import Mock

from app.yasin.services.yasin_statistics_service_v2 import (
    YasinStatisticsServiceV2,
)


@pytest.fixture
def signal_repository():

    return Mock()


@pytest.fixture
def statistics_repository():

    return Mock()


@pytest.fixture
def service(
    signal_repository,
    statistics_repository,
):

    return YasinStatisticsServiceV2(
        signal_repository=signal_repository,
        statistics_repository=statistics_repository,
    )


def test_rebuild_all(
    service,
    statistics_repository,
):

    statistics_repository.rebuild_all.return_value = [
        Mock(),
    ]

    result = service.rebuild_all()

    statistics_repository.rebuild_all.assert_called_once()

    assert len(result) == 1


def test_rebuild_market(
    service,
    statistics_repository,
):

    statistics = Mock()

    statistics_repository.rebuild_market.return_value = (
        statistics
    )

    result = service.rebuild_market(
        "GOLD"
    )

    assert result == statistics


def test_get_all_statistics(
    service,
    statistics_repository,
):

    statistics_repository.get_all.return_value = [
        Mock(),
        Mock(),
    ]

    result = service.get_all()

    assert len(result) == 2


def test_store_statistics(
    service,
    statistics_repository,
):

    statistics = Mock()

    service.save(statistics)

    statistics_repository.save.assert_called_once()


def test_delete_statistics(
    service,
    statistics_repository,
):

    service.delete_market(
        "FOREX"
    )

    statistics_repository.delete_market.assert_called_once_with(
        "FOREX"
    )


def test_statistics_exist(
    service,
    statistics_repository,
):

    statistics_repository.exists.return_value = True

    assert service.exists(
        "NAS100"
    ) is True
