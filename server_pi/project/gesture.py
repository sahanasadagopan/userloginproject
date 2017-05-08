#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gesture.ui'
#The Libraries that need to be imported for execution of this file
from __future__ import print_function # Python 2/3 compatibility
import boto3
from PyQt4 import QtCore, QtGui
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import sys
import logging
import time
import getopt
import signal
import skywriter
import datetime
import json
from pygame import mixer
from gtts import gTTS
global k=0

# initialising the QT interface part 
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)
# Designing the QT UI Interface
class Ui_Form(object):
    def setupUi(self, Form):
    # Initialising the form and giving names and identity to all the buttons
    #,modules present in UI, declaring the shape and the characteristics of the UI
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(400, 300)
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 331, 241))
        self.groupBox.setAutoFillBackground(True)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gesture = QtGui.QLabel(self.groupBox)
        self.gesture.setGeometry(QtCore.QRect(10, 40, 61, 20))
        self.gesture.setAutoFillBackground(False)
        self.gesture.setObjectName(_fromUtf8("gesture"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 70, 141, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 110, 121, 61))
        self.label_2.setAutoFillBackground(False)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.comboBox = QtGui.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(140, 120, 85, 31))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):

    #loading the Form after the UI is created
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.groupBox.setTitle(_translate("Form", "Gesture sensor", None))
        self.gesture.setText(_translate("Form", "gesture", None))
        self.label.setText(_translate("Form", "Detection:Negative", None))
        self.label_2.setText(_translate("Form", "Gesture Type", None))
        self.comboBox.setItemText(0, _translate("Form", "Touch", None))
        self.comboBox.setItemText(1, _translate("Form", "Left Swipe", None))
        self.comboBox.setItemText(2, _translate("Form", "Right Swipe", None))
   #The User Guide Monika introduces itself. 
        tts = gTTS(text='Hi User, I am Monika. I will let you login without letting you type your credentials into the website', lang='en', slow=False)
        tts.save("hello.mp3")
        mixer.init()
        mixer.music.load('hello.mp3')
        mixer.music.play()
   # If condition where the function executes only if the touch sensor is touched
        @skywriter.tap()
        def tap(position):
            global k
            print('Tap!', position)
            
            self.label.setText("Detection:positive")
        # disable thewebsocket condition 
            useWebsocket = False
            host = "a3r2kfqjg515ls.iot.us-west-2.amazonaws.com"
            rootCAPath = "root-CA.crt"
            certificatePath = "finalProject.cert.pem"
            privateKeyPath = "finalProject.private.key"           
            #Configure logging
            logger = logging.getLogger("AWSIoTPythonSDK.core")
            logger.setLevel(logging.DEBUG)
            streamHandler = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            streamHandler.setFormatter(formatter)
            logger.addHandler(streamHandler)

            myAWSIoTMQTTClient = None
            if useWebsocket:
                
                myAWSIoTMQTTClient = AWSIoTMQTTClient("basicPubSub", useWebsocket=True)
                myAWSIoTMQTTClient.configureEndpoint(host, 443)
                myAWSIoTMQTTClient.configureCredentials(rootCAPath)
            else:
                myAWSIoTMQTTClient = AWSIoTMQTTClient("basicPubSub")
                myAWSIoTMQTTClient.configureEndpoint(host, 8883)
                myAWSIoTMQTTClient.configureCredentials(rootCAPath, privateKeyPath, certificatePath)

             # AWSIoTMQTTClient connection configuration
            myAWSIoTMQTTClient.configureAutoReconnectBackoffTime(1, 32, 20)
            myAWSIoTMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
            myAWSIoTMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
            myAWSIoTMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
            myAWSIoTMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec

            # Connect and subscribe to AWS IoT
            myAWSIoTMQTTClient.connect()
            # Where the Audio UI speaks and keeps the user informed
            tts = gTTS(text='see told ya sahana,Your data is being sent to the website', lang='en', slow=False)
            tts.save("hello.mp3")
            mixer.init()
            mixer.music.load('hello.mp3')
            mixer.music.play()

            # Publish to the same topic in a loop forever
            loopCount = 0
           # giving the payload and publishing to the topic
        
            timestamp =datetime.datetime.now().strftime("%Y%m%d-%H:%M:%S")
            json1={"name":"Sahana Sadagopan","username":"sasa2453@colorado.edu","password":"san","time of login":timestamp}
            myAWSIoTMQTTClient.publish("aws/things/userlogin",json.dumps(json1),1)
            loopCount += 1
            time.sleep(1)
        # The second function is defined here for right and left swipes
        @skywriter.flick()
        def flick(start,finish):
            print('Got a flick!', start, finish)
            self.label.setText("Detection:positive")
            # Below are the credentials that are needed to connect to the AWS IOT framework
            useWebsocket = False
            host = "a3r2********.iot.us-west-2.amazonaws.com"
            rootCAPath = "root-CA.crt"
            certificatePath = "finalProject.cert.pem"
            privateKeyPath = "finalProject.private.key"           
            #Configure logging
            logger = logging.getLogger("AWSIoTPythonSDK.core")
            logger.setLevel(logging.DEBUG)
            streamHandler = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            streamHandler.setFormatter(formatter)
            logger.addHandler(streamHandler)
## The aws client is initilaised and the websocket mode is disabled
            myAWSIoTMQTTClient = None
            if useWebsocket:
                
                myAWSIoTMQTTClient = AWSIoTMQTTClient("basicPubSub", useWebsocket=True)
                myAWSIoTMQTTClient.configureEndpoint(host, 443)
                myAWSIoTMQTTClient.configureCredentials(rootCAPath)
            else:
                myAWSIoTMQTTClient = AWSIoTMQTTClient("basicPubSub")
                myAWSIoTMQTTClient.configureEndpoint(host, 8883)
                myAWSIoTMQTTClient.configureCredentials(rootCAPath, privateKeyPath, certificatePath)

             # AWSIoTMQTTClient connection configuration
            myAWSIoTMQTTClient.configureAutoReconnectBackoffTime(1, 32, 20)
            myAWSIoTMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
            myAWSIoTMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
            myAWSIoTMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
            myAWSIoTMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec

            # Connect and subscribe to AWS IoT
            myAWSIoTMQTTClient.connect()
             # Where the Audio UI speaks and keeps the user informed
            tts = gTTS(text='see told ya Bruce,Your data is being sent to the website', lang='en', slow=False)
            tts.save("hello.mp3")
            mixer.init()
            mixer.music.load('hello.mp3')
            mixer.music.play()

            # Publish to the same topic in a loop forever
            loopCount = 0
           # The payload is being sent
           # The mode of QOS=1 in this case to atleast send the message once
        
            timestamp =datetime.datetime.now().strftime("%Y%m%d-%H:%M:%S")
            json1={"name":"Bruce ","username":"brmu234@colorado.edu","password":"bans","time of login":timestamp}
            myAWSIoTMQTTClient.publish("aws/things/userlogin",json.dumps(json1),1)
            loopCount += 1
            time.sleep(1)
        
    




if __name__ == "__main__":
    import sys
    #initilising the main and calling the qt UI loading functions 
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())





