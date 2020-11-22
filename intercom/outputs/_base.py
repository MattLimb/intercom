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
    def new(self, old_tag, new_tag, output_name):
        pass

    def same(self, old_tag, new_tag, output_name):
        pass
    
    @staticmethod
    def override(repo_name, old, new, output_name):
        pass

    @abstractstaticmethod
    def verify_config():
        pass
    
    @abstractmethod
    def __repr__(self):
        pass