from functools import reduce
n = [1,2,3]
l = reduce(lambda x,y: x+y, n)
print(l)