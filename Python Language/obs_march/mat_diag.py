a = int(input())
mat = []
for i in range(a):
    l = list(map(int, input().split()))
    mat.append(l)
    
sum = 0

for i in range(a):
    sum += mat[i][i]

print(sum)