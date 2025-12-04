from Interface_object import IObject

# Class Chair se ke thu tu class IObject va khoi overide lai ham create_object
class Chair(IObject):
    def __init__(self):
        self.name = "Chair"
    
    def create_object(self):
        return self.name