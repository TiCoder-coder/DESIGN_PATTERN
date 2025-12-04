# Gọi lại các phương thức và thực thi

from abstraction import EmailMessage, SMSMessage
from refined_abstraction import UserMessage, SystemMessage

if __name__ == "__main__":
    print(f"[PROCESSING 1]")
    email_message = EmailMessage()
    user = UserMessage(email_message)
    user.send("Hello")
    system = SystemMessage(email_message)
    system.send("Hi")
    print(f"[PROCESSING 2]")
    sms_message = SMSMessage()
    user1 = UserMessage(sms_message)
    user1.send("What's your name?")
    system1 = SystemMessage(sms_message)
    system1.send("My name is robotic")
    
