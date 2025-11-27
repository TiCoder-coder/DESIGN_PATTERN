from abc import ABCMeta, abstractmethod

class IAnimal:
    @staticmethod
    @abstractmethod
    def talk(self):
        pass