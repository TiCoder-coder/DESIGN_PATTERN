from abc import ABCMeta, abstractmethod

# Khai bao mot class interface dung de khoi tao ban dau cho Factory method
class IObject(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def create_object():
        pass