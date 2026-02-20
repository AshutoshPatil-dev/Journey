r = int(input("Enter No. of rows: "))
c = int(input("Enter No. of columns: "))

matrix = []
for i in range(r):
    row = []
    for j in range(c):
        a = int(input(f"Enter element [{i}][{j}]: "))
        row.append(a)
    matrix.append(row)

for i in matrix:
    print(i)

def tran():
    t = []
    for i in range(c):
        row = []
        for j in range(r):
            row.append(matrix[j][i])
        t.append(row)
    for i in t:
        print(i)

def sym():
    if r != c:
        print("Not symmetric")
    else:
        sys = True
        for i in range(r):
            for j in range(c):
                if matrix[i][j] != matrix[j][i]:
                    sys = False
        
        if sys:
            print("You are symmetric")
        else:
            print("Not symmetric")

tran()
sym()
