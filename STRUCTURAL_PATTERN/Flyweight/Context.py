from FlyweightFactory import FlyWeightFactory

# Khơi tạo một Context - class này sẽ nhận chuỗi từ client và đưa 
# cho FlyweightFactory để nó lưu trữ (chỉ lưu trữ 1 lần)
class Context():
    def __init__(self, codes: str) -> str:
        self.codes = list(codes)

    def output(self):
        ret = ""
        for code in self.codes:
            ret = ret + FlyWeightFactory.get_flyweight(code).code

        return ret
