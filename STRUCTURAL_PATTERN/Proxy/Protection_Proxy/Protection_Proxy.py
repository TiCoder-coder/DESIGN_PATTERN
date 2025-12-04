from Real_Object import Real_Object
from First_Object import First_Object
import time
from dotenv import load_dotenv
from decouple import config

load_dotenv("/home/voanhnhat/Documents/Design_Pattern/Proxy/Protection_Proxy/.env")
password = config("password")

class Proxy:

    def __init__(self):
        self.object = Real_Object()
        self.keyword = None
    
    def implement(self):
        user_password = str(input("Enter the password: "))
        if user_password == password:
            print("[LOGGING SUCESS]")
            if self.keyword is None:
                print("Keyword is None, processing proxy keyword")
                self.keyword = self.object.request()
                print(f"[PROXY SUCESS] The keyword is: {self.keyword}")
            else:
                print("Keyword was existeds. Needn't process")
                return self.keyword
        else:
            return "[FAILED]Can not access. Error password."
            