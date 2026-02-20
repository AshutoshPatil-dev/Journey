'''a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
c = int(input("Enter number 3: "))

if a>= b and a>= c:
    print(f"{a} is max")
elif b>= a and b>= c:
    print(f"{b} is max")
elif c>= a and c>= b:
    print(f"{c} is max")
else:
    print("Error")

#Or

print(max(a,b,c))'''

c = [int(input(f"Enter number {x+1} : ")) for x in range(3)]
print(max(c))