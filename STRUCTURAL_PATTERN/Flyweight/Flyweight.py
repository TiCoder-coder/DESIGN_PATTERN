from IFlyweight import IFLyweight

# Khởi tạo một class FlyWeight class này sẽ kế 
# thừa từ class IFlyweight và thêm các thuộc tính
class Flyweight(IFLyweight):
    def __init__(self, code: str):
        self.code = code # Khởi tạo một thuộc tính là code

        