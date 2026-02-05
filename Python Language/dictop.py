'''colour = {
    1 : "Orange",
    2 : "Red",
    3 : "Yellow",
    4 : "Purple",
    5 : "Pink"
    }
while 1:
    num = int(input("Enter a number: "))
    if num in range(1,len(colour)+1):
        print(colour[num])
    else:   
        print(f"Only numbers between 1 to {len(colour)}")
        print("Exiting")
        break

'''
'''
t = ("Hello" ,"Python", "Test", "Python")

print(t)

value = input("Enter the value you want to find index of: ")

print(f"Index of {value} is: {t.index(value)}")
print(f"Count of {value} is: {t.count(value)}")'''

t = ("Hello" ,"Python", "Test", "Python")
print(t)
value = input("Enter a value to append: ")
list_tuple = list(t)
list_tuple.append(value)
print(tuple(list_tuple))

value = input("Enter a value to remove: ")
list_tuple.remove(value)
print(tuple(list_tuple) 
