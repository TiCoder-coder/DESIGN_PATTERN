from Builder_factory import Factory_Builder
from Builder import Builder

# class này nó sẽ overwrite lại các phương thức trong 
# Builder.py cho phù hợp để xây dựng một căn nhà
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