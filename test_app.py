"""Validate request handling."""


def test_simple(get, data):
    result = get("/EUR/USD/1")
    assert result.request.data == b"1.25"
