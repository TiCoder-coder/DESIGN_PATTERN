from Invoice import Invoice
from IProduct import IProduct
from Product import Product


if __name__ == "__main__":
    product1 = Product("chair", 100)
    product2 = Product("table", 200)
    category = Invoice("Object")
    category.add(product1)
    category.add(product2)
    name = product1.get_name()
    print(name)
    product1.get_price
    info = category.show_info()
