n = int(input())

mat = []
for i in range(n):
    mat.append(list(map(int, input().split())))

for i in range(n):
     mat[i][i] = 0

for i in mat:
     print(*i)      