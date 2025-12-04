#Gợi lại tất cả các class và thực thi 

from Adaptee import Adaptee
from Adapter import Adapter

def client_code(target):
    print(f'Client calling {target.request()}')

if __name__ == "__main__":
    adaptee = Adaptee()
    adapter = Adapter(adaptee)

    client_code(adapter)
