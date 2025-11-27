from singleton_application import Singleton_application
from Singleton import ISingleton

name1 = Singleton_application("Nhat")
name2 = Singleton_application("Ti")

name1.process_name()
name2.process_name()
logger = ISingleton()

print(logger.show_logs())