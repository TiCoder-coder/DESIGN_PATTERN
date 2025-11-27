from Animal_factory import IAnimal
from Enclosure_factory import IEnclosure
from Enlosure_Big_Size import EnclosureBigSize
from FourLegsAnimal import FourLegsAnimal
from Factory_Create import ICreate

class create_zoo_4_leg(ICreate):
    def create_Animal(self) -> IAnimal:
        return FourLegsAnimal()
    
    def create_Enclosure(self) -> IEnclosure:
        return EnclosureBigSize()
    