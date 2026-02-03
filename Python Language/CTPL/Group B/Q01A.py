number = [10,20,30,40]
some = ["Hello", "Bye"]
print(f"Original list: {number}")

number.append(50) # Adds a element to the end
print(f"After append 50: {number}")

number.remove(40) #Removes a given value
print(f"After removing 40: {number}")

number.insert(1,"Hello") # 1 is the index and after comma is the value
print(f"After inserting Hello in 1st Index: {number}")

number.extend(some) #Adds the "some" list to "number" list
print(number)

number.pop(2) # No value in pop means it will remove the last index
print(number)

number.clear() # Clears the whole list
print(number)

print(some) #Checking if 2nd list still exists

some[0] = "Yo" #Replacing a index and adding another value
print(some)
