from past_file import Past
from Adaptee import Adaptee

# Khởi tạo class Adapter dùng để chuyển đổi class cũ thành class mong muốn
class Adapter(Past):
    def __init__(self, adaptee: Adaptee):
        self.adaptee = adaptee

    def request(self):
        old_request = self.adaptee.special_request()
        return f"Adapter convert {old_request}"