from functools import reduce
    
l = lambda a: 1 if a == 1 else a*l(a-1)
print(l(4))


j = lambda a: a**2
print(j(int(input("Enter a number: "))))
      


n = [1,2,3,4]
l = list(filter(lambda x: x % 2 == 0, n))
print(l)

n = [1,2,3,4]
l = list(filter(lambda x: x % 2 != 0, n))
print(l)            

