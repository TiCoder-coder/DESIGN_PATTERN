from Animal_factory import IAnimal
from Enclosure_factory import IEnclosure
from TwoLegsAnimal import TwoLegsAnimal
from Enclosure_Small_Size import EnclosureSmallSize
from Factory_Create import ICreate

class create_zoo_2_leg(ICreate):
    def create_Animal(self) -> IAnimal:
        return TwoLegsAnimal()
    def create_Enclosure(self) -> IEnclosure:
        return EnclosureSmallSize()