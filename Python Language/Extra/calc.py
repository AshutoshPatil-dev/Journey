print("-----Arithmetic Calculator----")

print("1. Addition\n2. Substraction\n")

choice = int(input("Enter your choice: "))
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
match choice:
 case 1:
  print(f"Sum: {a+b}")
 case 2:
  print(f"Difference: {a-b}")
 case _:
    print("Invalid choice")
    
