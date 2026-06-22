import http.server
import json
from urllib.parse import urlparse, parse_qs


class UnitConverterHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_url = urlparse(self.path)

        # Endpoint dla pipeline CI/CD
        if parsed_url.path == '/health':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"status": "healthy"}).encode())
            return

        # Główny endpoint -konwerter
        if parsed_url.path == '/convert':
            query_components = parse_qs(parsed_url.query)
            celsius = query_components.get("celsius")

            if celsius:
                try:
                    c = float(celsius[0])
                    f = (c * 9 / 5) + 32
                    response = {"celsius": c, "fahrenheit": f}
                    self.send_response(200)
                except ValueError:
                    response = {"error": "Invalid value for celsius"}
                    self.send_response(400)
            else:
                response = {"message": "Use query parameter ?celsius=X"}
                self.send_response(200)

            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())
            return

        # Domyślny brak strony
        self.send_response(404)
        self.end_headers()


if __name__ == '__main__':
    backend = http.server.HTTPServer(('0.0.0.0', 8080), UnitConverterHandler)
    print("Converter App running on port 8080...")
    backend.serve_forever()