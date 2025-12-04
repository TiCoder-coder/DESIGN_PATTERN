from First_Object import First_Object

class Real_Object(First_Object):
    def __init__(self):
        print("Processing real object")
    def request(self):
        return "Real object"