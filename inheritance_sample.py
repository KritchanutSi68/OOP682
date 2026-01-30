class Person:
    def __init__(self, personal_id, name, age):
        self.personal_id = personal_id
        self.name = name
        self.age = age
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

class Student(Person):
    def __init__(self, personal_id, name, age, student_id):
        super().__init__(personal_id, name, age)
        self.student_id = student_id
    def __str__(self):
        return f"Student_ID"

class Staff(Person):
    def __init__(self, personal_id, name, age, staff_id):
        super().__init__(personal_id, name, age)
        self.staff_Id = staff_id

def main():
    student = Student(1234567890123, "Alice", 20, "s123")
    staff = Staff(1234567890123, "Bob", 35, "ST456")
    int(f"Student: {student.name}, Age: {student.age}, ")
    int(f"")

from model.person import Person
from model.student import Student



def get_person_info(person):
    print(isinstance(person, Person))
    return f"Name: {person.name}, Age: {person.age}"

get_person_info(student)
get_person_info(staff)

class Employee:
    pass

manager = Employee()