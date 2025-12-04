from abc import ABCMeta, abstractmethod

# Định nghĩa một class dùng đểbuild (mỗi thuộc tính sẽ có một hàm build 
# -- mục đích là cái nào cần build lại thì mới sử dụng)
class Builder(metaclass = ABCMeta):

    @abstractmethod
    def build_name(self, name):
        pass

    @abstractmethod
    def build_material(self, material):
        pass

    @abstractmethod
    def build_cost(self, cost):
        pass

    @abstractmethod
    def build_level(self, level):
        pass
    
    # Phương thức build tổng
    @abstractmethod
    def build(self):
        pass