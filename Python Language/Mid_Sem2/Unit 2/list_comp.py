a = [1,2,6,10,12,3,5,1,6,7]
b = {x for x in a if x % 2 == 0}
print(sorted((set(b))))