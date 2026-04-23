class person:
    def __init__(self, name,age):
        self.name = name
        self.age = age
    
    def display_person(self):
        print(f"Name: {self.name} Age: {self.age}")

class employee(person):
    def __init__(self, name, age,emp_id,dep):
        super().__init__(name,age)
        self.emp_id = emp_id
        self.dep = dep

    def display_employee(self):
        print(f"Emp ID: {self.emp_id}, Department: {self.dep}")

class Manager(employee):
    def __init__(self, name, age, emp_id, dep, team_size):
        super().__init__(name,age,emp_id, dep)
        self.team_size = team_size

    def display_manager(self):
        print(f"Team Size: {self.team_size}")

        
manager = Manager("Alice", 25, "E101", "IT", 10)

manager.display_person()
manager.display_employee()
manager.display_manager()