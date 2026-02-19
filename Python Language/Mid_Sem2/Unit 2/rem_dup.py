a = [1,2,2,3,4,4,5]
l = []
for i in a:
    if i not in l:
        l.append(i)
print(l)
