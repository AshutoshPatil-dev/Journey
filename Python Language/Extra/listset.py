'''list1 = [20,10,20,30]
print(f"Original list: {list1}")
print(f"New list: {list(set(list1))}")

list2 = ["Orange", "Red", "Orange", "Yellow"]
print(f"Original list: {list2}")
print(f"New list: {list(set(list2))}")
'''

students = {
    "Ashu" : [80,90],
    "Om" : [30,40],
    }

i = 0
for name, marks in students.items():
    total = sum(marks)
    avg = total / len(marks)
    print(f"Name: {name}\n Total Marks: {total}\n Average Marks: {avg}")
