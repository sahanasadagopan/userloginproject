#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'gesture.ui'
#
# Created: Thu Mar 30 22:52:28 2017
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!
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
k=0
from gtts import gTTS
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(400, 300)
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(39, 39, 211, 141))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gesture = QtGui.QLabel(self.groupBox)
        self.gesture.setGeometry(QtCore.QRect(10, 30, 61, 20))
        self.gesture.setObjectName(_fromUtf8("gesture"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 70, 141, 21))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.groupBox.setTitle(_translate("Form", "Gesture sensor", None))
        self.gesture.setText(_translate("Form", "gesture", None))
        self.label.setText(_translate("Form", "Detection:Negative", None))
        tts = gTTS(text='Hi User, I am Monika. I will let you login without letting you type your credentials into the website', lang='en', slow=False)
        tts.save("hello.mp3")
        mixer.init()
        mixer.music.load('hello.mp3')
        mixer.music.play()
        @skywriter.tap()
        def tap(position):
            global k
            print('Tap!', position)
            
            self.label.setText("Detection:positive")
            
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

            tts = gTTS(text='see told ya,Your data is being sent to the website', lang='en', slow=False)
            tts.save("hello.mp3")
            mixer.init()
            mixer.music.load('hello.mp3')
            mixer.music.play()

            # Publish to the same topic in a loop forever
            loopCount = 0
            while True:
        
                timestamp =datetime.datetime.now().strftime("%Y%m%d-%H:%M:%S")
                json1={"username":"sasa2453@colorado.edu","password":"san","time of login":timestamp}
                myAWSIoTMQTTClient.publish("aws/things/userlogin",json.dumps(json1),1)
                loopCount += 1
                time.sleep(1)     

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())



