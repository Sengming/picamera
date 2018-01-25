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
        
        # Connect the socket to the port where the server is listening
        self.__server_address = (ip, portNumber)


    def output(self, data):
        '''
        Prints out byte data to stdout for debug purposes
        '''
        if (self.__canOutputData):
            self.__sock.send(data)
        
    def allowOutput(self):
        self.__canOutputData = True
    
    def disableOutput(self):
        self.__canOutputData = False
        self.__sock.close()
    
    def __enter__(self):
        try:
            self.__sock.connect(self.__server_address)
        except socket.timeout:
            print('Unable to connect to remote socket.')
            
    def __exit__(self):
        self.__sock.close()
