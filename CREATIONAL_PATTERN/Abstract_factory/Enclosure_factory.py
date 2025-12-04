from abc import ABCMeta, abstractmethod

# Khởi tạo một Abstract Factory ban đầu cho enclosure
class IEnclosure:
    @staticmethod
    @abstractmethod
    def filed(self):
        pass