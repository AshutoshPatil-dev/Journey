def aw(*a,**b):
    return a, b

a = list(map(int, input("Enter few numbers with spaces: ").split()))
a,b = aw(*a, Name=input("Enter your name: "), City=input("Enter your city: "))

print(*a)
print(b)