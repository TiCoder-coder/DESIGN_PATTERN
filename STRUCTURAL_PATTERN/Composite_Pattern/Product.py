from IProduct import IProduct

class Product(IProduct):
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def get_name(self):
        return self.name
    
    def get_price(self):
        return self.price
    
    def show_info(self, indent=0):
        print(f"The product {self.name} has price is {self.price} VND")