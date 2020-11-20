from abc import ABCMeta, abstractmethod, abstractstaticmethod

class BaseOutput(metaclass=ABCMeta):
    @property
    @abstractmethod
    def name():
        pass
    
    @abstractmethod
    def __init__(self, config, repo):
        pass
    
    @abstractmethod
    def run(self, old_tag, new_tag):
        pass

    @abstractmethod
    def __repr__(self):
        pass