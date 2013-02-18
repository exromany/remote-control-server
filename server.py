#!/usr/bin/python3.2
# -*- coding: utf-8 -*-
import http.server
import socketserver
import key

PORT = 9534


class HttpKeyboard(http.server.BaseHTTPRequestHandler):
    server_version = "SimpleHTTP/0.1"

    def do_GET(self):
        """Serve a GET request."""
        path = self.path.split('/')
        if len(path) == 3:
            key.key_events(path[2])
        self.send_head()

    def send_head(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.send_header("Content-Length", 0)
        self.end_headers()

httpd = socketserver.TCPServer(("", PORT), HttpKeyboard)

print("server at port", PORT)
if __name__ == "__main__":
    httpd.serve_forever()
