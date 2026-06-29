import pytest

from app.database.session import SessionLocal

from app.repositories.signal_repository import (
    SignalRepository,
)

from app.repositories.statistics_repository import (
    StatisticsRepository,
)


@pytest.fixture
def db():

    session = SessionLocal()

    yield session

    session.rollback()

    session.close()


@pytest.fixture
def signal_repository(
    db,
):

    return SignalRepository(db)


@pytest.fixture
def statistics_repository(
    db,
):

    return StatisticsRepository(db)


def test_create_signal(
    signal_repository,
):

    signal = signal_repository.create(
        symbol="XAUUSD",
        market="GOLD",
        direction="BUY",
        entry=2500,
        stop_loss=2490,
        take_profit_1=2510,
    )

    assert signal.id is not None


def test_get_signal(
    signal_repository,
):

    signal = signal_repository.get(
        1
    )

    assert signal is not None


def test_get_all_signals(
    signal_repository,
):

    signals = signal_repository.get_all()

    assert isinstance(
        signals,
        list,
    )


def test_statistics_repository(
    statistics_repository,
):

    result = statistics_repository.get_all()

    assert isinstance(
        result,
        list,
    )


def test_delete_signal(
    signal_repository,
):

    signal_repository.delete(1)

    assert True


def test_market_statistics(
    statistics_repository,
):

    statistics = statistics_repository.get_market(
        "GOLD"
    )

    assert statistics is not None


def test_database_connection(
    db,
):

    assert db is not None
