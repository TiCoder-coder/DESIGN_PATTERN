from Interface_object import IObject
from chair import Chair
from table import Table

class Create_Object:
    @staticmethod
    def creeate_object(object):
        if object == "chair":
            return Chair()
        if object == "table":
            return Table()

Object = Create_Object.creeate_object("chair")
print(Object.name)