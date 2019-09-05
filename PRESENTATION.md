# PyTest 101

**Introduction to Python testing framework**

*by  @jirikuncar*


## Testing

*   What?
*   Why?
*   When?
* HoW?


## What is a test?

```
   ____    _   _   _ _____ ___ ___  _   _
  / ___|  / \ | | | |_   _|_ _/ _ \| \ | |
 | |     / _ \| | | | | |  | | | | |  \| |
 | |___ / ___ \ |_| | | |  | | |_| | |\  |
  \____/_/   \_\___/  |_| |___\___/|_| \_|

===========================================

         ⚠  TESTING IN PROGRESS ⚠

===========================================
```

### Test definition

> A test is code that runs to check the validity
> of other code.

* _unit_
* integration
* end-to-end
* regression
* performance


## Why to write tests?

```
▒▒▒▒▒▒▒▒▄▄▄▄▄▄▄▄▒▒▒▒▒▒▒▒
▒▒▒▒▒▄█▀▀░░░░░░▀▀█▄▒▒▒▒▒
▒▒▒▄█▀▄██▄░░░░░░░░▀█▄▒▒▒
▒▒█▀░▀░░▄▀░░░░▄▀▀▀▀░▀█▒▒
▒█▀░░░░███░░░░▄█▄░░░░▀█▒
▒█░░░░░░▀░░░░░▀█▀░░░░░█▒
▒█░░░░░░░░░░░░░░░░░░░░█▒
▒█░░██▄░░▀▀▀▀▄▄░░░░░░░█▒
▒▀█░█░█░░░▄▄▄▄▄░░░░░░█▀▒
▒▒▀█▀░▀▀▀▀░▄▄▄▀░░░░▄█▀▒▒
▒▒▒█░░░░░░▀█░░░░░▄█▀▒▒▒▒
▒▒▒█▄░░░░░▀█▄▄▄█▀▀▒▒▒▒▒▒
▒▒▒▒▀▀▀▀▀▀▀▒▒▒▒▒▒▒▒▒▒▒▒▒
```


### Reasons

* Validate behavior
* Documentation/example of usage
* Safety net for future changes
  (Business requirements - regressions)
* Gain confidence
* Reduce the cost of bugs
* It's more fun with them than without


## Pop quizz

📢 Please shout the answer out loud.


### test_equality_1

```python
10 == 10
```


#### Answer

```python
True
```


### test_equality_2

```python
10 == "10"
```


#### Answer

```python
False
```


### test_approx

```python
.6 / .4 == 1.5
```


#### Answer

```python
False
```


### test_set

```python
6 in {0, 2, 4, 5, 8, 10}
```


#### Answer

```python
False
```


### Quizz summary

```python
10 == 10
10 == "10"
.6 / .4 == 1.5
6 in {0, 2, 4, 5, 8, 10}
```


## PyTest API

```python
assert 10 == 10
assert 10 == "10"
assert .6 / .4 == 1.5
assert 6 in {0, 2, 4, 5, 8}
```


## PyTest introduction

> The pytest framework makes it easy to write small tests,
> yet scales to support complex functional testing for applications
> and libraries.
>
> -- https://docs.pytest.org/en/5.1.2/

* magic with AST (`assert`)
* many plugins
* JUnit, coverage, ...
* vs. `unittest` is class/method oriented


## When? `(ﾉ◕ヮ◕)ﾉ`

* _Never_
* After
* During
* Before


### Never `|_・)`

```
┻┳|
┳┻| _
┻┳| •.•) ---{ because I'm ~~brave~~ lazy }
┳┻|⊂ﾉ
┻┳|
```


### After `ヽ(。_°)ノ`

Bad thoughts?


### During `ヽ(´▽｀)ノ`

Oh yeah!


### Before `٩( ᐛ )و `

```
           _____ ____  ____
          |_   _|  _ \|  _ \
            | | | | | | | | |
            | | | |_| | |_| |
            |_| |____/|____/
           /      |       \
         Test   Driven   Development
```

1. define what the code is expected to produce
2. implement just enough code to make it pass

_TDD != unit tests_


### Before push to master! `‿( ́ ̵ _-`)‿`

```
    _  _   _ _____ ___  __  __   _ _____ ___ _______
   /_\| | | |_   _/   \|  \/  | /_\_   _|_ _|_  / __|
  / A \ |U| | |T||  O  | |M | |/ A \|T|  |I| /Z/| E_
 /_/ \_\___/  |_| \___/|_|  |_/_/ \_\_| |___/___|___|
                           --- Continuous Integration

```

* `git merge --ff-only` with _master_ branch protection
  (`git fetch origin master && git rebase -i origin/master`)
* `python setup.py test` ~ `pytest` MUST be commited in
  the CI configuration in the repository

*Automatize before you write tests and code.*


## How? `(⊙_☉)`

Wait! I have to _write tests_ for my *own* code?


### Yes!

```
  _____ _____ _____ _____ _____ _____ _____ _____ _____ _____
 |_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|
   _ _ _          __                                   _ _ _
  | | | |   ___  / _|   ___ ___  _   _ _ __ ___  ___  | | | |
  | | | |  / _ \| |_   / __/ _ \| | | | '__/ __|/ _ \ | | | |
  |_|_|_| | (_) |  _| | (_| (_) | |_| | |  \__ |  __/ |_|_|_|
  (_(_(_)  \___/|_|    \___\___/ \__,_|_|  |___/\___| (_(_(_)
  _____ _____ _____ _____ _____ _____ _____ _____ _____ _____
 |_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|

```


### From assert to suite `(∩｀-´)⊃━☆ﾟ.*･｡ﾟ`

```python
"""test_simple.py"""


def test_equality_1():
    assert 10 == 10


def test_equality_2():
    assert 10 == "10"


def test_approx():
    assert .6 / .4 == 1.5


def test_set():
    assert 6 in {0, 2, 4, 5, 8}
```

[//]: # (:'<,'>w test_simple.py)

```console
$ python3 -m venv venv
$ . venv/bin/activate
(venv) $ pip install pytest
(venv) $ pytest test_simple.py
```


### Understand PyTest results `(ง •̀_•́)ง`

```
========================= test session starts =========================
```
Installed plugins
```
platform darwin -- Python 3.7.4, pytest-5.1.2, py-1.8.0, pluggy-0.12.0
```
Look for tests in this directory
```
rootdir: ~/presentations/pytest-101
```
See what it found and run
```
collected 2 items

test_simple.py .F                                               [100%]

============================== FAILURES ==============================

    def test_equality_2():
>       assert 10 == "10"
E       AssertionError: assert 10 == '10'

test_simple.py:7: AssertionError
===================== 1 failed, 1 passed in 0.04s ====================
```


### Exceptions

```python
"""Validate raised exceptions."""

import pytest


def test_value_error():
    with pytest.raises(ZeroDivisionError) as context:
        1/0

    assert str(context.value) == "division by zero"
```

[//]: # (:'<,'>w test_value_error.py)


## Structure of a test-case `(/¯◡ ‿ ◡)/¯`

```
     _
    / \   _ __ _ __ __ _ _ __   __ _  ___
   / _ \ | '__| '__/ _` | '_ \ / _` |/ _ \
  / ___ \| |  | | | (_| | | | | (_| |  __/
 /_/ _ \_|_|  __|  \__,_|_| |_|\__, |\___|
    / \   ___| |_              |___/
   / _ \ / __| __|
  / ___ | (__| |_           _
 /_// \\_\___|___| ___ _ __| |_
   / _ \ / __/ __|/ _ | '__| __|
  / ___ \\__ \__ |  __| |  | |_
 /_/   \_|___|___/\___|_|   \__|

```
* arrange the environment
* perform an act
* state a fact


### FX API

```python
"""Simple currency exchange service."""


def init(cur):
    cur.execute("""CREATE TABLE fx (symbol text, value real)""")


def convert(cur, value, source, target):
    result = cur.execute(
        """SELECT ? * t.value / s.value
           FROM fx s, fx t
           WHERE s.symbol=? AND t.symbol=?""",
        (value, source, target)
    ).fetchone()
    return result[0]
```

[//]: # (:'<,'>w fx.py)


### Test FX API - happy path

```python
"""Test FX API."""

import sqlite3
import fx


def test_convert():
    """Check happy convertion path."""
    #: Arrange
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()

    fx.init(cur)

    data = {"EUR": 1, "USD": .8}
    cur.executemany("INSERT INTO fx VALUES (?, ?)", data.items())

    #: Act
    result = fx.convert(cur, 100, "EUR", "USD")

    #: Assert
    assert result == 125
```

[//]: # (:'<,'>w test_fx.py)


#### Bug 🐞

```diff
diff --git a/fx.py b/fx.py
index fba7caa..84cb428 100644
--- a/fx.py
+++ b/fx.py
@@ -7,7 +7,7 @@ def init(cur):

 def convert(cur, value, source, target):
     result = cur.execute(
-        """SELECT ? * t.value / s.value
+        """SELECT ? * s.value / t.value
            FROM fx s, fx t
            WHERE s.symbol=? AND t.symbol=?""",
         (value, source, target)
```

[//]: # (:!git add -A)
[//]: # (:'<,'>w !git apply)


### Test FX API - special case

```python


def test_convert_same_currencies():
    """Convert same currencies."""
    #: Arrange
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()

    fx.init(cur)

    data = {"EUR": 1, "USD": .8}
    cur.executemany("INSERT INTO fx VALUES (?, ?)", data.items())

    #: Act
    result = [fx.convert(cur, 1, symbol, symbol) for symbol in data]

    #: Assert
    assert result == [1, 1]
```

[//]: # (:'<,'>w >> test_fx.py)


## Reuse arrangements - Fixtures

> A software test fixture sets up the system for the testing process by
> providing it with all the necessary code to initialize it, thereby
> satisfying whatever preconditions there may be.
>
> --- Pereira da Silva, Lucas (June 10, 2016) doi:10.1109/SERA.2016.7516134

```python
"""Manage test environment."""

import sqlite3

import pytest

import fx


@pytest.fixture(scope="session")
def conn():
    """Create a Connection object that represents the database."""
    connection = sqlite3.connect(":memory:")
    yield connection
    connection.close()


@pytest.fixture(scope="session")
def cur(conn):  # depends on conn
    """Create a Cursor object."""
    cursor = conn.cursor()
    fx.init(cursor)  # create database tables
    return cursor
```

`conftest.py` enables sharing fixtures among test modules.

[//]: # (:'<,'>w conftest.py)


### Fixture lifecycle

> Order: Higher-scoped fixtures are instantiated first
>
> --- https://pytest.org/en/latest/fixture.html#order-higher-scoped-fixtures-are-instantiated-first

```python


@pytest.fixture
def data_source():
    """Define basic FX values."""
    return {"EUR": 1, "USD": .8}


@pytest.fixture
def data(data_source, cur):
    """Load data source to database."""
    cur.execute("BEGIN")
    cur.executemany("INSERT INTO fx VALUES (?, ?)", data_source.items())
    yield data_source
    cur.connection.rollback()
```

[//]: # (:'<,'>w >> conftest.py)

*Quiz:* `def test_quiz(data): pass`


### Refactor tests

```python
def test_convert(cur, data): pass
def test_convert_same_currencies(...): pass
```

```
   ____  _         _   _      ____
  / / / | |    ___| |_( )___  \ \ \
 / / /  | |   / _ \ __|// __|  \ \ \
 \ \ \  | |__|  __/ |_  \__ \  / / /
 _\_\_\ |_____\___|\__|_|___/ /_/_/__
 \ \ \    ___ ___   __| | ___   / / /
  \ \ \  / __/ _ \ / _` |/ _ \ / / /
  / / / | (_| (_) | (_| |  __/ \ \ \
 /_/_/   \___\___/ \__,_|\___|  \_\_\

```

[//]: # (:tabnew test_fx.py)

**BONUS:**
```python
@pytest.mark.parametrize(
    "symbol",
    (
        "EUR",
        "USD",
        pytest.param(
            "XXX",
            marks=pytest.mark.xfail(reason="Unknown symbol", run=True, strict=True),
        ),
    ),
)
```

## FX Service

*Disclamer: only for presentation purposes.*

```python
"""Simple FX Server."""

import sqlite3
from http.server import BaseHTTPRequestHandler

import fx

def handler(connection):
    """Create FX handler with an external db connection."""

    class FXHandler(BaseHTTPRequestHandler):

        def do_GET(self):
            #: Business logic
            source, target, value = self.path.strip('/').split('/')
            cursor = connection.cursor()
            response = fx.convert(cursor, value, source, target)

            #: Headers
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()

            #: Content
            self.wfile.write(str(response).encode("utf-8"))

    return FXHandler
```

[//]: # (:'<,'>w app.py)


### Start server

```python

if __name__ == "__main__":
    from http.server import test

    conn = sqlite3.connect("app.db", check_same_thread=False)
    try:
        fx.init(conn.cursor())
    except Exception as e:
        # or use IF NOT EXISTS in fx.init
        if str(e) != "table fx already exists":
            raise

    try:
        test(HandlerClass=handler(conn))
    finally:
        conn.close()
```

[//]: # (:'<,'>w >> app.py)

```console
$ python -m app
$ curl -X GET http://localhost:8000/EUR/USD/100
$ sqlite3 app.db
sqlite> insert into fx values ('EUR', 1), ('USD', 0.8);
```


### What to test? `¯\_(ツ)_/¯`

1. Running service on http://localhost:8000
2. HTTP handler implementation
3. ...

```
  _                 _
 | |_  __ _ _ _  __| |___  _  _ _ __
 | ' \/ _` | ' \/ _` (_-< | || | '_ \
 |_||_\__,_|_||_\__,_/__/  \_,_| .__/
 and tell me when, why and how |_|

```

### Test FX service

Compose - Reuse - Share

```python
"""Validate request handling."""


def test_simple(get, data):
    result = get("/EUR/USD/1")
    assert result.request.data == b"1.25"
```

*Task:* define `get` fixture factory
*Bonus 🍫:* propose more test-cases

[//]: # (:'<,'>w test_app.py)


### Test handler

*Goal:* answer GET requests using FX app.

```python


class Request:
    """Implement an interface of HTTP request."""

    def __init__(self, path):
        self.path = path
        self.data = b''  # internal state

    def makefile(self, *args, **kwargs):
        from io import BytesIO
        return BytesIO(f"GET {self.path}".encode("utf-8"))

    def sendall(self, data):
        self.data += data


@pytest.fixture
def get(conn):
    """Create HTTP GET request."""
    import app

    handler = app.handler(conn)

    def factory(path):
        return handler(Request(path), (None, 8000), None)

    return factory
```

[//]: # (:'<,'>w >> conftest.py)


## FX client

```python
"""Implement FX client code."""

import requests


class FX(requests.Session):

    def __init__(self, base_url="http://localhost:8000"):
        super().__init__()
        self.base_url = base_url

    def convert(self, value, source, target):
        response = self.get(f"{self.base_url}/{source}/{target}/{value}")
        return float(response.content)
```

[//]: # (:'<,'>w client.py)

```console
(venv) $ pip install requests
```

### Test FX client

```python
"""Test FX client library."""

import pytest

import client


@pytest.fixture
def fx():
    return client.FX("http://localhost:8000")


def test_client(fx):
    assert fx.convert(100, "EUR", "USD") == 125
```

[//]: # (:'<,'>w test_client.py)

Yay. The tests are passing ... for now.

#### Arrange

* Running service
* Mocked the service
* Application code

#### Hide the service `( •_•)>⌐■-■ (⌐■_■)`

*HTTPretty*

https://httpretty.readthedocs.io/en/latest/introduction.html

*Responses*

https://github.com/getsentry/responses

```python

import responses


@pytest.fixture(name="responses")
def mocked_responses():
    with responses.RequestsMock() as rsps:
        rsps.add(
            responses.GET,
            "http://localhost:8000/EUR/EUR/100",
            body="100",
        )
        rsps.add(
            responses.GET,
            "http://localhost:8000/EUR/USD/100",
            body="125",
        )
        yield rsps


def test_client_mock(responses, fx):
    assert fx.convert(100, "EUR", "USD") == 125
    assert len(responses.calls) == 1
```

[//]: # (:`<,'>w >> test_client.py)

```console
(venv) $ pip install responses
```

* `assert_all_requests_are_fired`
* `scope="session"`
* `responses.calls[-1].request.url`


#### Record communication `ლ(ಠ益ಠ)ლ`

*Betamax* `[●▪▪●]`

> Betamax records your HTTP interactions
> so the NSA does not have to.

https://betamax.readthedocs.io/en/latest/index.html

```python


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
```

[//]: # (:'<,'>w >> conftest.py)

```console
(venv) $ pip install betamax
(venv) $ mkdir vrc/cassettes
(venv) $ pytest test_client.py
# stop python app.py and rerun pytest
```


## Test Doubles: fake | stub | mock

*Quiz:* Can you find any in the past examples?


### Definitions

Fake
: an object with a working implementation,
: but same as production one

* implementation of an interface
  (usually takes some shortcut)
* handles state
* `:memory:` database, `Request`
* examples: payment gateway -> "paid"

Stub
: an object that holds predefined data
: and uses it to answer calls during tests

* avoid using real data or side effects
* REST responses that do not change the state of the system


Mock
: an object that register calls they receive

* replays trained behavior
* verify that actions were performed
* usually stateless
* examples: emails, "commands"


## Level-up `ᕙ(⇀‸↼‶)ᕗ`

*Hypothesis* testing

https://hypothesis.readthedocs.io/en/latest/index.html


```python
"""Hypothesis testing."""

import pytest

import hypothesis.strategies as st
from hypothesis import given, settings

import fx


@given(value=st.floats(allow_nan=False, allow_infinity=True))
@settings(max_examples=1000)
def test_convert_hypothesis(cur, data, value):
    """Check convertion path."""
    result = fx.convert(cur, value, "EUR", "USD")
    assert result == pytest.approx(value * 1.25)
```

[//]: # (:'<,'>w test_hypothesis.py)

```console
(venv) $ pip install hypothesis
(venv) $ pytest --hypothesis-show-statistics test_hypothesis.py
```


## Feedback and questions

* Is there a topic that wasn''t covered?
* Too fast, too ~~furious~~ slow?
* I am lost and I want to go home.
* I ~~don't understand~~ ♡  PyTest.

---
contact me @jirikuncar (twitter, github, jiri@kuncar.dev)


<!--
vim:tw=60:ft=markdown:
-->
