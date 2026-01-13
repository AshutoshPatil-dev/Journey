print("-----Arithmetic Calculator----")

print("1. Addition\n2. Substraction\n")

choice = int(input("Enter your choice: "))

match choice:
 case 1:
  a = int(input("Enter a number: "))
  b = int(input("Enter another number: "))
  print(f"Sum: {a+b}")
 case 2:
  a = int(input("Enter a number: "))
  b = int(input("Enter another number: "))
  print(f"Difference: {a-b}")
 case _:
    print("Invalid choice")
    
