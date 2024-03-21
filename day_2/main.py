class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # dunder method
    def __str__(self):
        return f"<Student(name={self.name}, age={self.age})>"

    def __gt__(self, other):
        return self.age > other.age



student_1 = Student('Bach', 28)
student_2 = Student('Quynh', 26)

print (student_1.name)
print (student_1.age)
print (student_1)

print (student_2 > student_1)