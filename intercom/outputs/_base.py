from abc import ABCMeta, abstractmethod, abstractstaticmethod

__author__ = "Matt Limb <matt.limb17@gmail.com>"

class BaseOutput(metaclass=ABCMeta):
    @property
    @abstractmethod
    def name():
        pass
    
    @abstractmethod
    def __init__(self, config, repo):
        pass
    
    @abstractmethod
    def new(self, old_tag, new_tag):
        pass

    def same(self, old_tag, new_tag):
        pass
    
    @abstractmethod
    def __repr__(self):
        pass