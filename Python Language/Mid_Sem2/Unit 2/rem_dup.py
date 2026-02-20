a = [11,11,11,11,11,2,12,1,2,2,3,4]
r = []
for i in a:
    if i not in r:
        r.append(i)

print(r)