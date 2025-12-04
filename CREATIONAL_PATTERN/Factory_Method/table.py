from Interface_object import IObject

# Clas table ke thu tu class Interface_object va no se overide ham create_object
class Table(IObject):
    def __init__(self):
        self.name = "Chair"

    def create_object(self):
        return self.name
    