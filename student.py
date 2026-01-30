from models.person import Person

class Student(Person):
    def __init__(self, name, age, personal_id, student_id):
        super().__init__(name,age, personal_id)
        self.student_id = student_id

    def __str__(self):
        return f"Namee: {self.name} age: {self.age} Student_id: {self.student_id}"