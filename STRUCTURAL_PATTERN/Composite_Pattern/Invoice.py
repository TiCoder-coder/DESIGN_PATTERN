from IProduct import IProduct

class Invoice(IProduct):
    def __init__(self, name):
        self.name = name
        self.category = []

    def add(self, component: IProduct):
        self.category.append(component)

    def remove(self, component: IProduct):
        self.category.remove(component)
    
    def get_name(self):
        return self.name

    def get_price(self):
        total = 0
        for item in self.category:
            total += item.get_price()
        return total
    def show_info(self, indent=0):
        print("" *indent + f"Invoice: {self.name}")
        for item in self.category:
            item.show_info(indent + 4)