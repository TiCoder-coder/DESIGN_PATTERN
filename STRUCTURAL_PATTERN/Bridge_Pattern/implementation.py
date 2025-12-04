from abc import ABCMeta, abstractmethod

# Định nghĩa các gửi (thực thi) các phương thức
class IMessage(metaclass=ABCMeta):
    @abstractmethod
    def send_messege(self, message: str):
        pass

class SMSMessage(IMessage):
    def send_messege(self, message: str):
        print(f"[SMS] {message}")

class EmailMessage(IMessage):
    def send_messege(self, message: str):
        print(f"[EMAIL] {message}")