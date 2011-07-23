import base64
from irequestparser import IRequestParser

class TextImageParser(IRequestParser):
	"""
	Parse and decode images encoded as text.
	Author tom@0x101.com
	"""

	__rawRequest = None

	def __init__(self, rawRequest):
		self.__rawRequest = rawRequest

	def getRequestContent(self):
		"""
		Return the part of the URL which contains the encoded image.
		"""
		requestContent = ''
		urlParts = self.__splitPath()

		if len(urlParts) > 1:
			requestContent = urlParts[1]

		return requestContent

	def __splitPath(self):
		return self.__rawRequest.split('/', 1)

	def __decodeImage(self, imageContent):
		"""
		The current version only supports images encoded as base64.		
		"""
		try:
			# Decode the request
			decodedImage = base64.b64encode(decodedImage)
			return decodedImage
		except Exception:
			raise InvalidTextImage('Error decoding image')

	def getTextImage(self):
		"""
		Return the binary content of a image decoding the URL string.		
		"""
		requestContent = self.getRequestContent()

		if requestContent <> '':
			textImageContent = self.__decodeImage(requestContent)
			return textImageContent
		else:
			raise InvalidTextImage('Text image not found')


class InvalidTextImage(Exception):
	"""
	Something went wrong parsing the request.
	"""
	__msg = ""

	def __init__(self, msg):
		self.__msg = msg

	def __str__(self):
		return sef.__msg
