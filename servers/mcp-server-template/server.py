from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import os

class MCPHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"status": "ok"}).encode())
        else:
            self.send_response(404)
            self.end_headers()

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))
    server = HTTPServer(("", port), MCPHandler)
    print(f"🚀 MCP Server running on port {port}")
    server.serve_forever()
