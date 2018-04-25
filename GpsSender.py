'''
Created on Jan 27, 2018

@author: root
'''
import threading
from time import sleep
from queue import Queue
import socket
import sys
import serial

class GpsSender(threading.Thread):
    '''
    classdocs
    '''
    def __init__(self, outputQueue):
        '''
        Constructor
        '''
        threading.Thread.__init__(self)
        self.__outputQueue = outputQueue
        self.__sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__server_address = ('104.199.128.49', 8083)
        self.__sock.connect(self.__server_address)
        
    def run(self):
        threading.Thread.run(self)
        
class GpsReader(threading.Thread):
    
    def __init__(self, serialPort, outputQueue):
        threading.Thread.__init__(self)
        self.__serialPort = serialPort
        self.__outputQueue = outputQueue
        powerOnGps = 'AT+CGNSPWR=1\r\n'
        gpsString = 'AT+CGNSURC=2\r\n'
        #Give the GSM module enough time to power on
        sleep(15)
        serialPort.write(gpsString.encode(encoding='utf_8', errors='strict'))
        sleep(5)
        serialPort.write(powerOnGps.encode(encoding='utf_8', errors='strict'))
        self.__sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__server_address = ('104.199.128.49', 8083)
        self.__sock.connect(self.__server_address)
        
    def run(self):
        bytesToSend = bytes()
        # Look for linefeed
        mychar = b'\x0A'
        while True:
#             self.__sock.send(self.__serialPort.read(94))
            data = self.__serialPort.read()
            num = sys.stdout.buffer.write(data)
            print(num)
            if data == mychar:
                self.__sock.send(bytesToSend)
                bytesToSend = bytes()
                print("It's equals!")
#                 sleep(2)
            else:
                bytesToSend += data
                print(bytesToSend)
#             self.__sock.send(b'1100')

#             print(self.__serialPort.read(94).decode('utf_8'))
#             sleep(2)
            
        
    
    