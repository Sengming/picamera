'''
Created on Jan 23, 2018

@author: root
'''
from abc import ABC, abstractmethod, ABCMeta

class IStreamSubscriber(ABC):
    __metaclass__ = ABCMeta
    '''Interface to enforce stream subscriber methods'''
    
    @abstractmethod
    def output(self, data):
        return
    
    @abstractmethod
    def allowOutput(self):
        return
    
    @abstractmethod
    def disableOutput(self):
        return