from abc import ABCMeta, abstractmethod

# Class interface ban đầu cho prototype dùng để định nghĩa phương thức abstract copy
# và phương thức này sẽ được overwrite lại ở class prototype để nó thực hiện đúng
# Chức năng
class IPrototype(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def copy():
        pass