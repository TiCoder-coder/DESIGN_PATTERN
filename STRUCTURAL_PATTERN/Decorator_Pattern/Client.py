from Decorator.BlackSugar import BlackSugar
from Decorator.Bubble import Bubble
from Decorator.EggPudding import EggPudding
from Decorator.FruitPudding import FruitPudding
from Decorator.WhiteBubble import WhiteBuble
from Base.MilkTea import MilkTea
inner = MilkTea()
orderMilkTea = BlackSugar(Bubble(EggPudding(FruitPudding(WhiteBuble(inner)))))
orderMilkTea2 = BlackSugar(EggPudding(FruitPudding(WhiteBuble(inner))))

print(f"The price for orderMilkTea is: {orderMilkTea.Cost()}")
print(f"The price for orderMilkTea2 is: {orderMilkTea2.Cost()}")