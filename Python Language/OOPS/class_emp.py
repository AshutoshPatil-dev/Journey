class emp:
    def __init__(self,name,emp_id,salary):
        self.name = name
        self.id = emp_id
        self.salary = salary
    def inputs(self):
        self.id = int(input("Enter your employee ID: "))
        self.name = input("Enter your name: ")
        self.salary = int(input("Enter the salary: "))
        
    def __del__(self):
        print("An object was deleted raaaaaaaaaaaaaaa")
    
    def printing(self):
        print(self.name)
        print(self.id)
        print(self.salary)

a = emp("Ashutosh",7568,78)
a.printing()

