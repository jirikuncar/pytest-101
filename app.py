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
