from Real_Object import Real_Object
from First_Object import First_Object
import time
from dotenv import load_dotenv
from decouple import config

load_dotenv("/home/voanhnhat/Documents/Design_Pattern/Proxy/Protection_Proxy/.env")
limit = config("limit")

class Proxy:

    def __init__(self):
        self.object = Real_Object()
        self.keyword = None
        self.limit = limit
        self.count = 0
    
    def implement(self):
        if int(self.count) <= int(self.limit):
            print("[SUCESS]")
            self.count += 1
            start = time.time()
            if self.keyword is None:
                print("Keyword is None, processing proxy keyword")
                self.keyword = self.object.request()
                print(f"[PROXY SUCESS] The keyword is: {self.keyword}")
            else:
                print("Keyword was existeds. Needn't process")
                return self.keyword
            end = time.time()
            process_time = round(end-start, 4)
            print(f"[SUCESS] Time processing: {process_time} senconds")
            
        else:
            return "[FAILED]Can not access. Limit request."
            