class Person:
    def __ubut__(self, name, age, personal_id):
        self.name = name
        self.age = age
        self.personal_id = personal_id

        def __str__(self):
            return f"Name: {self.name} age: {self.age} Personal ID: {self.personal_id}"