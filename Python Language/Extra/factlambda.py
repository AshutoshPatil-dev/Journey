from functools import reduce
def fact():
    a = [1,2,3]
    l = reduce(lambda x,y : x*y, a)
    print(l)
fact()

def even():
    n = [1,2,3,4]
    l = list(filter(lambda x: x % 2 == 0, n))
    print(l)

even()

def sum():
    n = [1,2,3]
    l = reduce(lambda x,y: x+y, n)
    print(l)

sum()