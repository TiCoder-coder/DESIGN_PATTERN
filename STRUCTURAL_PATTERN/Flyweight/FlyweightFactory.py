from Flyweight import Flyweight

# Khởi tạo class Flyweight chính 
class FlyWeightFactory():
    _flyweight = {} # Dùng để lưu trữ các kí tự (không trùng lặp)


    # Lấy các kí tự và lưu trữ chúng (không trùng lặp)
    @classmethod
    def get_flyweight(cls, code: str) -> Flyweight:
        if not code in cls._flyweight: # Kiểm tra trùng lặp
            cls._flyweight[code] = Flyweight(code)
        return cls._flyweight[code]
    
    # Đếm xem flyweight lưu trữ bao nhiêu kí tự
    @classmethod
    def countOfFlyweight(cls) -> int:
        return len(cls._flyweight)
    
