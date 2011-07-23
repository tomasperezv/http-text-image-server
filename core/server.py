from BaseHTTPServer import HTTPServer
from handler import TextImageRequestHandler
from parser import InvalidTextImage

class TextImageServer():

	"""
	Simple server for generating images encoded as text.
	Author tom@0x101.com
	"""
	__port = 8080
	__server = None

	def __init__(self, port):
		self.__port = port

	def start(self):
		self.__server = HTTPServer(('', 8080), TextImageRequestHandler)
		self.__server.serve_forever()

	def stop(self):
		self.__server.socket.close()
