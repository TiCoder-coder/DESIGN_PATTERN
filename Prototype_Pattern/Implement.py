from Interface_prototype import IPrototype
from prototype import Prototype

prototypes = Prototype("student123", "nhat", "10", "10")
student = prototypes.copy()
print(student)