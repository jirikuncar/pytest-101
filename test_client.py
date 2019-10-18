"""Test FX client library."""

import pytest

import client


@pytest.fixture
def old_fx():
    return client.FX("http://localhost:8000")


@pytest.fixture(scope="session")
def recorder():
    import betamax
    import client

    session = client.FX("http://localhost:8000")
    with betamax.Betamax(session) as vrc:
        yield vrc


@pytest.fixture
def fx(request, recorder):
    from betamax.fixtures.pytest import _casette_name
    recorder.use_cassette(_casette_name(request, True))

    yield recorder.session


def test_client(fx):
    assert fx.convert(100, "EUR", "USD") == 125
