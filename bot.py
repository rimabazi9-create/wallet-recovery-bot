import http.server
import socketserver
import os

PORT = int(os.environ.get("PORT", 10000))
Handler = http.server.SimpleHTTPRequestHandler

print(f"Starting web server on port {PORT}...")
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at port", PORT)
    httpd.serve_forever()
