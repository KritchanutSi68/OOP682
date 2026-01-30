class Staff(Person):
    def __init__(self, personal_id, name, age, staff_id):
        super().__init__(personal_id, name, age)
        self.staff_Id = staff_id
    
    def __str__(self):
        return f"Staff"{self.personal_id}
