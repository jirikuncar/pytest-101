"""Simple currency exchange API."""


def init(cur):
    cur.execute("""CREATE TABLE fx (symbol text, value real)""")


def convert(cur, value, source, target):
    result = cur.execute(
        """SELECT ? * s.value / t.value
           FROM fx s, fx t
           WHERE s.symbol=? AND t.symbol=?""",
        (value, source, target)
    ).fetchone()
    return result[0]
