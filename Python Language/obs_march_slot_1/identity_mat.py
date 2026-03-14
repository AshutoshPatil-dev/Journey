n = int(input())

mat = []
for i in range(n):
    mat.append(list(map(int, input().split())))

identity = True

for i in range(n):
    for j in range(n):
        if i == j:
            if mat[i][j] != 1:
                identity = False
        else:
            if mat[i][j] != 0:
                identity = False

if identity:
    print("Identity Matrix")
else:
    print("Not an Identity Matrix")