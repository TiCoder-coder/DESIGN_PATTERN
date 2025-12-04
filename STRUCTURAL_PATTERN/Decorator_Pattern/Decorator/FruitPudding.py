from Base.MilkTeaDecorator import MilkTeaDecorator
from Base.IMilkTea import IMilkTea

class FruitPudding(MilkTeaDecorator):
    def __init__(self, inner: IMilkTea):
        super().__init__(inner)
        self.inner = inner
    def Cost(self):
        return 2.5 + float(self.inner.Cost())