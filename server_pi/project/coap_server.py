
#!/usr/bin/env python

# Copyright (c) Twisted Matrix Laboratories.
# See LICENSE for details.

from __future__ import print_function

from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor
global i
class EchoserverDatagramProtocol(DatagramProtocol):
    global i
    time=datetime.datetime.now().strftime("%Y%m%d-%H:%M:%S")
    strings = [
        "Data is being scanned from dynamoDB"
        "time": time
    ]
    i = len(strings)   
    def startProtocol(self):
        self.transport.connect('10.0.0.42', 8000)
        self.sendDatagram()
    
    def sendDatagram(self):
        global i
        for j in range(0,i):
            if len(self.strings):
                datagram = self.strings.pop(0)
                
                self.transport.write(datagram)
            else:
                reactor.stop()
            #print(datagram)
    #def datagramReceived(self, datagram, host):
     #   print('Datagram received: ', repr(datagram))
     #   self.sendDatagram()

def main():
    protocol = EchoserverDatagramProtocol()
    t = reactor.listenUDP(0, protocol)
    reactor.run()

if __name__ == '__main__':
    main()
