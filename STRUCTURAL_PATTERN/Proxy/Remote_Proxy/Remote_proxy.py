from Real_Object import Real_Object
from First_Object import First_Object

class Proxy:

    def __init__(self):
        self.object = Real_Object()
    
    def implement(self):
        self.object = self.object.request()
        print(f"[PROXY SUCESS] The keyword is: {self.object}")
        return self.object

        