# Following modules are needed
# Following websocket is created with the tornado Library of python
import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
from pygame import mixer
k=0
from gtts import gTTS
#The websocket Class is initialised
class WSHandler(tornado.websocket.WebSocketHandler):
	def check_origin(self, origin):
		return True
        # The functiuon is executred if the websocket is connected to the client
	def open(self):
		print ('user is connected.\n')
        # The audio UI tells the user that the client is connected to the server
		tts = gTTS(text='Your website is connected now', lang='en', slow=False)
                tts.save("hello.mp3")
                mixer.init()
                mixer.music.load('hello.mp3')
                mixer.music.play()
	# The message is displayed if anything specifically is sent from the server to the client	
                       
	def on_message(self,message):
		print ('recieved message:%s\n'%message)
		self.write_message(message + 'OK')
        # The Function is executed when the connection is closed
	def on_close(self):
		print ('connection closed \n')
              # The audio UI notifies the user when the connection is closed
		tts = gTTS(text='Your website is closed now', lang='en', slow=False)
                tts.save("hello.mp3")
                mixer.init()
                mixer.music.load('hello.mp3')
                mixer.music.play()
# when the hanndler is launches the Webserver
application = tornado.web.Application([(r'/ws',WSHandler)])


if __name__ == "__main__":
        # initilises and starts the websocket 
	http_server = tornado.httpserver.HTTPServer(application)
	# the server is listening to any request made to the port 8080
	http_server.listen(8080)
	# keeps loop[ing around until the server is manually stopped
	tornado.ioloop.IOLoop.instance().start()
	
        
