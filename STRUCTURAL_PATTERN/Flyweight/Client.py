# Thực thi các class

from Context import Context
from FlyweightFactory import FlyWeightFactory
context = Context("aaabbbccc")
print(context.output())
print(f"Len of context, if do not use flyweight: {len('aaabbbccc')}")
print(f"Len of context, if use flyweight: {FlyWeightFactory.countOfFlyweight()}")