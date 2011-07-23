from BaseHTTPServer import BaseHTTPRequestHandler
from parser import TextImageParser, InvalidTextImage

class TextImageRequestHandler(BaseHTTPRequestHandler):
	"""
	Handles requests received by the TextImageServer.
	Author tom@0x101.com
	"""
	__textImageParser = None

	def __getImageParser(self):
		if self.__textImageParser == None:
			self.__textImageParser = TextImageParser(self.path)
		return self.__textImageParser		

	def __setImageHeaders(self):
		self.send_response(200)
		self.send_header('Content-type', 'image/jpg')
		self.end_headers()
	
	def __setErrorHeaders(self):
		self.send_response(500)
		self.send_header('Content-type', 'text/plain')
		self.end_headers()

	def __getImageContent(self):
		imageContent = self.__getImageParser().getTextImage()
		return imageContent 

	def do_GET(self):
		try: 
			imageContent = self.__getImageContent()
			self.__setImageHeaders()
			self.wfile.write(imageContent)
		except InvalidTextImage:
			self.__setErrorHeaders()
