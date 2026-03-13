a = {"I", "V", "X", "L", "C", "D", "M"}

b = input()
valid = True
for i in b:
    if i not in a:
        print("NO")
        break
else:
    print("YES")
