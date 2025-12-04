from Interface_prototype import IPrototype

# Class Prototype sẽ khởi tạo các thuộc tính cần thiết và một phương thức copy
# dùng để copy lại thuộc tính cũ nếu client tạo một object mới mà chỉ khác
# object cũ vài thuộc tính
class Prototype(IPrototype):
    def __init__(self, studentId, name, age, classes):
        self.studentId = studentId
        self.name = name
        self.age = age
        self.classes = classes
    
    def copy(self):
        return type(self)(
            self.studentId,
            self.name,
            self.age,
            self.classes
        )
    def __str__(self):
        return f"I am a student. My name is {self.name} and student id is {self.studentId}. I am {self.age} years old and study in class {self.classes}"
    