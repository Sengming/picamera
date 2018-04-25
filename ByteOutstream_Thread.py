'''
Created on Jan 23, 2018

@author: root
'''
import threading
from time import sleep


class ByteOutstream(threading.Thread):
    '''Reads the byte stream sent and broadcasts to subscribers'''
    def __init__(self, stream):
        threading.Thread.__init__(self)
        self.__subscribers = []
        self.__stream = stream

    def run(self):
        while True:
#             sleep(0.05)
            output = self.__stream.read()
            for subscriber in self.__subscribers:
                subscriber.output(output)
#             self.__subscribers[0].output(output)
                    
    def subscribe(self, subscriber):
        self.__subscribers.append(subscriber)
        
        
#         print "Starting " + self.name
#         print_time(self.name, 5, self.counter)
#         print "Exiting " + self.name