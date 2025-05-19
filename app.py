from http.server import SimpleHTTPRequestHandler, HTTPServer

PORT = 8000
handler = SimpleHTTPRequestHandler

with HTTPServer(("0.0.0.0", PORT), handler) as httpd:
    print(f"Serveur démarré sur http://localhost:{PORT}")
    httpd.serve_forever()