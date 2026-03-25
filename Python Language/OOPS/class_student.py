class student:
    # def __init__(self):
    #     self.name = ""
    #     self.roll = 0
    #     self.marks1 = 0
    #     self.marks2 = 0

    def inputs(self):
        self.name = input("Enter your name: ")
        self.roll = int(input("Enter your Roll Number: "))
        self.marks1 = int(input("Enter your marks for subject 1: "))
        self.marks2 = int(input("Enter your marks for subject 2: "))
        print()

    def printing(self):
        print(self.name)
        print(self.roll)
        print(self.marks1)
        print(self.marks2)
        print()


s1 = student()
s1.printing()

'''
num = int(input("Enter number of students: "))
s = []
for i in range(num):
    print(f"Enter details of Student No. {i+1}")
    obj = student()
    obj.inputs()
    s.append(obj)

for i in range(num):
    print(f"Student No. {i+1}")
    s[i].printing()

for i in range(num):
    print(id(s[i]))
'''