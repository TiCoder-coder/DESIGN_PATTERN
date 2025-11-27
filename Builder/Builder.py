from Builder_factory import Factory_Builder
from abc import ABCMeta, abstractmethod

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

    @abstractmethod
    def build(self):
        pass