import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web

class WSHandler(tornado.websocket.WebSocketHandler):
	def check_origin(self, origin):
		return True

	def open(self):
		print ('user is connected.\n')
	def on_message(self,message):
		print ('recieved message:%s\n'%message)
		self.write_message(message + 'OK')
	def on_close(self):
		print ('connection closed \n')

application = tornado.web.Application([(r'/ws',WSHandler)])


if __name__ == "__main__":
	http_server = tornado.httpserver.HTTPServer(application)
	http_server.listen(8080)
	tornado.ioloop.IOLoop.instance().start()
