from abc import ABCMeta, abstractmethod

class IPrototype(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def copy():
        pass