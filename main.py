#!/usr/bin/python2.6
from core.server import TextImageServer

def main():
	"""
	Implementation of a simple server for generating images encoded as text.
	Author tom@0x101.com
	"""
	try:
		print 'starting webserver\n'
		server = TextImageServer(8080)
		server.start()
	except KeyboardInterrupt:
		print 'stopping webserver\n'
		server.stop()

if __name__ == '__main__':
	main()
