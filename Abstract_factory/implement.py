from Factory_Create import ICreate
from create_Zoo_Animal_Have_2_Legs import create_zoo_2_leg
from create_Zoo_Animal_Have_4_Legs import create_zoo_4_leg

def Implement(zoo: ICreate):
    animal = zoo.create_Animal()
    enclosure = zoo.create_Enclosure()

    print(animal.talk())
    print(enclosure.filed())

if __name__ == "__main__":
    print("ZOO FOR ANIMAL WITH 2 LEGS")
    Implement(create_zoo_2_leg())
    print("ZOO FOR ANIMAL WITH 4 LEGS")
    Implement(create_zoo_4_leg())
