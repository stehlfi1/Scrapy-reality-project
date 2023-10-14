from http.server import BaseHTTPRequestHandler, HTTPServer
import psycopg2

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        
        conn = psycopg2.connect(
            host="db",
            database="sreality_dat",
            user="admin",
            password="admin1"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT title, image_url FROM scraped_data LIMIT 500")
        records = cursor.fetchall()

        # title and test
        self.wfile.write(f"<h1>Sreality</h1>".encode('utf-8'))

        for record in records:
            title, image_url = record
            self.wfile.write(f"<h1>{title}</h1><img src='{image_url}'></img>".encode('utf-8'))

if __name__ == '__main__':
    print("i am launched")
    httpd = HTTPServer(('0.0.0.0', 8070), SimpleHTTPRequestHandler)
    httpd.serve_forever()
