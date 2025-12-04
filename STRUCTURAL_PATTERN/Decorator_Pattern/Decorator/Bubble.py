from Base.MilkTeaDecorator import MilkTeaDecorator
from Base.IMilkTea import IMilkTea

class Bubble(MilkTeaDecorator):
    def __init__(self, inner: IMilkTea):
        super().__init__(inner)
        self.inner = inner
    def Cost(self):
        return 1 + float(self.inner.Cost())