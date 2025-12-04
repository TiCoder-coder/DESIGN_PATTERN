from Real_Object import Real_Object
class Proxy:

    def __init__(self):
        self.object = Real_Object()
        self.keyword = None # Bien luu tru cache
    
    def implement(self):
        if self.keyword is None:
            print("[CAN NOT PROCESS] Data is none")
            print("[PROCESSING CREATE DATA]")
            self.keyword = self.object.request()
        else:
            print("[OK PROCESSING] Had data")
        return self.keyword
        