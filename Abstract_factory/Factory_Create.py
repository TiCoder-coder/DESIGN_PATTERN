from Animal_factory import IAnimal
from Enclosure_factory import IEnclosure
from abc import abstractmethod

class ICreate():
    @staticmethod
    @abstractmethod
    def create_Animal(self) -> IAnimal:
        return "Create animal success"
    
    @staticmethod
    @abstractmethod
    def create_Enclosure(self) -> IEnclosure:
        return "Create enclosure success"

