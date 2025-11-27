from Builder_factory import Factory_Builder
from Builder import Builder
class Buil_House(Builder):

    def __init__(self):
        self.house = Factory_Builder()
    
    def build_name(self, name):
        self.house.name = name
        return self


    def build_material(self, material):
        self.house.material = material
        return self

    def build_cost(self, cost):
        self.house.cost = cost
        return self


    def build_level(self, level):
        self.house.level = level
        return self


    def build(self):
        return self.house