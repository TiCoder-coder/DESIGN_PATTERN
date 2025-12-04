from abc import ABCMeta, abstractmethod

class First_Object(metaclass=ABCMeta):
    def request(self):
        raise NotImplementedError