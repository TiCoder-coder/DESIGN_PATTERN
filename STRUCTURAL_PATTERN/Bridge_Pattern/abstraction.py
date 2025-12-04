from implementation import IMessage, SMSMessage, EmailMessage
from abc import ABCMeta, abstractmethod

# Định nghĩa một class Message ban đâu và phương thức send
#  phương thức này sẽ được overwrire lại ở refined_abstraction.py
class Message(metaclass=ABCMeta):
    def __init__(self, sender: IMessage):
        self.sender = sender

    @abstractmethod
    def send(self, message: str):
        pass