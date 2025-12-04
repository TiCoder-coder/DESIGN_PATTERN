from abc import ABCMeta, abstractmethod

# Khởi tạo một Abstract Factory ban đầu cho animal
class IAnimal:
    @staticmethod
    @abstractmethod
    def talk(self):
        pass