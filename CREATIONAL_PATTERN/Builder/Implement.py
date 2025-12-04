# Gọi lại các hàm và thực thi

from House_builder import Buil_House
from Builder import Builder
class Implement:
    def __init__(self, builder: Builder):
        self.builder = builder

    def build_full_house(self):
        return(
            self.builder
            .build_name("House Level 4")
            .build_material("Concrete")
            .build_cost("100 USD")
            .build_level("4")
            .build()
        )
    
    

builder = Buil_House()
implement = Implement(builder)

house = implement.build_full_house()
print(house)
