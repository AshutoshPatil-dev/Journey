a = input()
count = 0
s = set()
for i in a:
    if a.count(i) >= 2 and i not in s:
        count += 1
        s.add(i)
print(count)