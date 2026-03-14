r, c = map(int, input().split())

A = []
B = []

for i in range(r):
    A.append(list(map(int, input().split())))

for i in range(r):
    B.append(list(map(int, input().split())))

for i in range(r):
    for j in range(c):
        print(A[i][j] + B[i][j], end=" ")
    print()