class ClassRoom:
    def __init__(self, name, capacity):
        self.name = name
        self.students = []
    
    def add_student(self, student):
        if len(self.students) < self.capacity:
            self.students.append(student)
            return True
        return False
    
    def __len__(self):
        return len(self.students)
    
    def __getitem__(self, index):
        return self.students[index]