'''
Created on Jan 24, 2018

@author: root
'''
from IStreamSubscriber import IStreamSubscriber
import socket
        
class SocketSubscriber(IStreamSubscriber):
    '''
    classdocs
    '''
    def __init__(self, ip, portNumber):
        # Create a TCP/IP socket
        self.__sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         self.__sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.__canOutputData = True
        # Connect the socket to the port where the server is listening
        self.__server_address = (ip, portNumber)
#         print("Init called")

    def output(self, data):
        '''
        Prints out byte data to stdout for debug purposes
        '''
        if self.__canOutputData is True:
            self.__sock.send(data)
#             self.__sock.sendto(data, self.__server_address)
        
    def allowOutput(self):
        self.__canOutputData = True
    
    def disableOutput(self):
        self.__canOutputData = False
        self.__sock.close()
    
    def __enter__(self):
        try:
            self.__sock.connect(self.__server_address)
#             print("Enter called")
            return self
        except socket.timeout:
            print('Unable to connect to remote socket.')
            
    def __exit__(self, type, value, traceback):
#         print("Exit called")
        self.__sock.close()
