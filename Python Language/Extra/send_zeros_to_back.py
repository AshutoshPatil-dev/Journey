l = [1,3,0,4]
count = 0
j = 0
for i in range(len(l)):
    if l[i] != 0:
        print(i)
        l[j] , l[i] = l[i], l[j]
        j += 1
print(l)