from abstraction import Message

# Định nghĩa lại các phương thức send cho từng class một cách thích hợp
class UserMessage(Message):
    def send(self, message: str):
        print("[Processing user messgae]")
        self.sender.send_messege(message)

class SystemMessage(Message):
    def send(self, message: str):
        print("[Processing system message]")
        self.sender.send_messege(message)