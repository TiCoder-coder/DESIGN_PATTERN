from abc import ABCMeta, abstractmethod

class IProduct(metaclass=ABCMeta):
    @abstractmethod
    def get_name(self):
        pass
    @abstractmethod
    def get_price(self):
        pass
    @abstractmethod
    def show_info(self, indent=0):
        pass