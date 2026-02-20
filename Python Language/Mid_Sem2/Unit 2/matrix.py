r = int(input("Enter the No. of rows: "))
c = int(input("Enter the No. of columns: "))

matrix = []

for i in range(r):
    row = []
    for j in range(c):
        a = int(input(f"Enter the element [{i}][{j}]: "))
        row.append(a)
    matrix.append(row)

for i in matrix:
    print(i)


def tran():
    t = []
    print("\nTranspose:")
    for i in range(c):
        row = []
        for j in range(r):
            row.append(matrix[j][i])
        t.append(row)
    for i in t:
        print(i)

def sys():
    if r != c:
        print("Not symmetric")
    else:
        sys = True
        for i in range(r):
            for j in range(c):
                if matrix[i][j] != matrix[j][i]:
                    sys = False
        if sys:
            print("Symmetric")
        else:
            print("Not symmetric")

tran()
print()
sys()