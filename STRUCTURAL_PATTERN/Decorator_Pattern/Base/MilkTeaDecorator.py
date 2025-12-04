from .IMilkTea import IMilkTea
from abc import ABCMeta, abstractmethod
class MilkTeaDecorator(IMilkTea):
    def __init__(self, inner: IMilkTea):
        self.milkTea = inner

    def Cost(self):
        return self.milkTea.Cost()
