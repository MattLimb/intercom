from abc import ABCMeta, abstractmethod, abstractstaticmethod

__author__ = "Matt Limb <matt.limb17@gmail.com>"

class BaseSource(metaclass=ABCMeta):
    @abstractmethod
    def get_latest(self):
        pass

    @abstractstaticmethod
    def verify_config():
        pass

    @abstractmethod
    def __repr__(self):
        pass