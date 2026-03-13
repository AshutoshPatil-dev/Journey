r,c = list(map(int, input().split()))

mat1 = []
mat2 = []

for i in range(r):
    m1 = list(map(int, input().split()))
    mat1.append(m1)
    
for i in range(r):
    m2 = list(map(int, input().split()))
    mat2.append(m2)
    
sub = []
for i in range(r):
    row = []
    for j in range(c):
      row.append(mat1[i][j] - mat2[i][j])
    sub.append(row)
    
for i in sub:
    print(*i)
    