#Just some operations in sets
def setop():
    set1 = {10,20,30,40,40,50}
    set2 = {50, 60, 30, 60, "Hello"}
    set3 = {10,20}
    print(set1 | set2)
    print(set1 &  set2)
    print(set1 - set2)
    print(set1 ^ set2)
    print(set3.issubset(set1))
    print(set1.issuperset(set3))

#Removing same elements from a set
def simrev():
    l1 = [10,10]
    r = set(l1)
    print(list(r))

#Finding the specified element in a set
def finde():
    s1 = {1,2,3,4,5}
    num = int(input("Enter the element to find: "))
    for i in s1:
        if num == i:
            print(f"{num} is in s1")
            
#
def dictop():
    student = {
        "Name" : "Ashu",
        "Marks" : 80,
        "Marks" : 18,
        "Name" : "Ashutosh"
        }

    student["Student"] = "Maths"
    student["Marks"] = 19

    del student["Name"]
    print(student)

dictionary()
