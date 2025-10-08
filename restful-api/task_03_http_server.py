#!/usr/bin/env python3
"""
task_03_http_server.py
A simple HTTP API using Python's builtin http.server module.
It demonstrates basic API endpoints and JSON responses.

Endpoints:
  GET /        -> "Hello, this is a simple API!"
  GET /status  -> "OK"
  GET /data    -> JSON: {"name":"John","age":30,"city":"New York"}
  GET /info    -> JSON with version and short description.
  other paths  -> 404 JSON: {"error":"Endpoint not found"}

Optional:
  POST /echo   -> Echoes back the JSON body you send.
"""

from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse
import json
import os
from typing import Tuple


HOST = "127.0.0.1"
PORT = int(os.environ.get("PORT", "8000"))


def _json_bytes(payload: dict) -> bytes:
    """Serialize a dict to pretty JSON bytes (UTF-8)."""
    return json.dumps(payload, ensure_ascii=False).encode("utf-8")


class SimpleAPIHandler(BaseHTTPRequestHandler):
    server_version = "SimpleAPI/1.0"

    def _send_plain(self, code: int, text: str) -> None:
        """Send a plain text response."""
        data = text.encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def _send_json(self, code: int, payload: dict) -> None:
        """Send a JSON response."""
        data = _json_bytes(payload)
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def _read_json_body(self) -> Tuple[dict, str]:
        """Read and parse JSON body for POST/PUT requests."""
        length = int(self.headers.get("Content-Length", "0") or 0)
        if length == 0:
            return {}, "Empty body"
        raw = self.rfile.read(length)
        try:
            return json.loads(raw.decode("utf-8")), ""
        except json.JSONDecodeError as exc:
            return {}, f"Invalid JSON: {exc.msg}"

    def do_GET(self) -> None:
        """Handle GET requests."""
        parsed = urlparse(self.path)
        path = parsed.path

        if path == "/":
            self._send_plain(200, "Hello, this is a simple API!")
            return

        if path == "/status":
            self._send_plain(200, "OK")
            return

        if path == "/data":
            payload = {"name": "John", "age": 30, "city": "New York"}
            self._send_json(200, payload)
            return

        if path == "/info":
            payload = {
                "version": "1.0",
                "description": "A simple API built with http.server",
            }
            self._send_json(200, payload)
            return

        self._send_json(404, {"error": "Endpoint not found"})

    def do_POST(self) -> None:
        """Handle POST requests."""
        parsed = urlparse(self.path)
        if parsed.path == "/echo":
            body, err = self._read_json_body()
            if err:
                self._send_json(400, {"error": err})
                return
            self._send_json(200, {"echo": body})
            return

        self._send_json(404, {"error": "Endpoint not found"})

    def log_message(self, fmt: str, *args) -> None:
        """Customize server log output."""
        super().log_message(fmt, *args)


def run() -> None:
    """Run the HTTP server."""
    server_address = (HOST, PORT)
    httpd = ThreadingHTTPServer(server_address, SimpleAPIHandler)
    print(f"Serving on http://{HOST}:{PORT}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down...")
    finally:
        httpd.server_close()


if __name__ == "__main__":
    run()
