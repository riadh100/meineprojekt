"""
Unit-Tests für den
YasinMonitorService.
"""

import pytest

from app.yasin.services.yasin_monitor_service import (
    YasinMonitorService,
)


@pytest.fixture
def service():

    return YasinMonitorService()


def test_monitor_runs(service):

    report = service.monitor()

    assert report is not None


def test_open_trades(service):

    report = service.monitor()

    assert report.open_trades >= 0


def test_take_profit_hits(service):

    report = service.monitor()

    assert report.take_profit_hits >= 0


def test_stop_loss_hits(service):

    report = service.monitor()

    assert report.stop_loss_hits >= 0


def test_updated_trades(service):

    report = service.monitor()

    assert report.updated_trades >= 0


def test_timestamp(service):

    report = service.monitor()

    assert report.timestamp is not None
