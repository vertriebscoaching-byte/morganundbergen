import http.server, socketserver, functools

DIRECTORY = "/Users/jamiemorgan/Desktop/Svenja Agentur /Agentur Webseite/website"
PORT = 4173

Handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=DIRECTORY)
with socketserver.TCPServer(("127.0.0.1", PORT), Handler) as httpd:
    print(f"Serving {DIRECTORY} at http://127.0.0.1:{PORT}")
    httpd.serve_forever()
