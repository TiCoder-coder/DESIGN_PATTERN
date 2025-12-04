from Real_Object import Real_Object
from First_Object import First_Object

class Proxy:

    def __init__(self):
        self.object = Real_Object()
        self.keyword = None
    
    def implement(self):
        if self.keyword is None:
            print("Keyword is None, processing proxy keyword")
            self.keyword = self.object.request()
            print(f"[PROXY SUCESS] The keyword is: {self.keyword}")
        else:
            print("Keyword was existeds. Needn't process")
            return self.keyword
        