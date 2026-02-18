a = [1,2,2,3,4,4,5]
s = set()
l = []
for i in a:
    if i not in s:
        l.append(i)
        s.add(i)
print(l)
