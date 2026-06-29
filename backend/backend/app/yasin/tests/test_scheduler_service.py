"""
Unit-Tests für den
YasinSchedulerService.
"""

import pytest

from app.yasin.scheduler.yasin_scheduler_service import (
    YasinSchedulerService,
)


@pytest.fixture
def service():

    return YasinSchedulerService()


def test_scheduler_start(service):

    service.start()

    status = service.status()

    assert status["running"] is True

    service.stop()


def test_scheduler_stop(service):

    service.start()

    service.stop()

    status = service.status()

    assert status["running"] is False


def test_scheduler_status(service):

    status = service.status()

    assert "status" in status
    assert "jobs" in status
    assert "running" in status


def test_registered_jobs(service):

    status = service.status()

    assert status["jobs"] >= 0


def test_next_job(service):

    status = service.status()

    assert "next_job" in status


def test_last_job(service):

    status = service.status()

    assert "last_job" in status
