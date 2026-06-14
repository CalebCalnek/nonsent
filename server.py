from http.server import HTTPServer, SimpleHTTPRequestHandler
from productions import Sentence

HOST: str = "0.0.0.0"
PORT: int = 5327

class Handler(SimpleHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)
		self.send_header("Content-Type", "text/plain")
		self.end_headers()
		sentence: str = str(Sentence())
		sentence_encoded: bytes = sentence.encode()
		self.wfile.write(sentence_encoded)

if __name__ == "__main__":
	server = HTTPServer((HOST, PORT), Handler)
	server.serve_forever()

