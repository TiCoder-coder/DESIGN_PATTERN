import time
from First_Object import First_Object

class Real_Object(First_Object):
    def __init__(self):
        print("Processing real object")
        print("Wait 3 seconds before next process")
        time.sleep(3)
    def request(self):
        return "Real object"