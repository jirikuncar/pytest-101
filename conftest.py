import sqlite3

import pytest

import fx


@pytest.fixture(scope="session")
def conn():
    connection = sqlite3.connect(":memory:")
    yield connection
    connection.close()


@pytest.fixture(scope="session")
def cur(conn):
    """Cursor with initialized DB table."""
    cursor = conn.cursor()
    fx.init(cursor)

    return cursor


@pytest.fixture
def data_source():
    return {"EUR": 1, "USD": .8}


@pytest.fixture
def data(cur, data_source):
    cur.execute("BEGIN")
    cur.executemany("INSERT INTO fx VALUES (?, ?)", data_source.items())
    yield data_source
    cur.connection.rollback()
