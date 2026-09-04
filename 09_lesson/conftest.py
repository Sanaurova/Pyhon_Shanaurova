import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db import DATABASE_URL


@pytest.fixture(scope="session")
def engine():
    engine = create_engine(DATABASE_URL)
    yield engine


@pytest.fixture(scope="function")
def db_session(engine):
    """
    Каждый тест получает отдельную транзакцию,
    которая откатывается после завершения.
    """
    connection = engine.connect()
    transaction = connection.begin()
    session = sessionmaker(bind=connection)()
    yield session
    session.close()
    transaction.rollback()
    connection.close()
