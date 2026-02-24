def mat1():
    global r1,c1
    r1 = int(input("Enter No. of rows for Matrix 1: "))
    c1 = int(input("Enter No. of columns for Matrix 1: "))
    matrix1 = []
    for i in range(r1):
        row = []
        for j in range(c1): 
            col = int(input(f"Enter the element [{i}][{j}]: "))
            row.append(col)
        matrix1.append(row)
    return matrix1

def mat2():
    global r2,c2
    r2 = int(input("Enter No. of rows for Matrix 2: "))
    c2 = int(input("Enter No. of columns for Matrix 2: "))
    matrix2 = []
    for i in range(r2): 
        row = []
        for j in range(c2): 
            col = int(input(f"Enter the element [{i}][{j}]: "))
            row.append(col)
        matrix2.append(row)
    return matrix2

def mat_add(matrix1,matrix2):
    sum = []
    if r1 == r2 and c1 == c2:
        for i in range(r1):
            row = []
            for j in range(c1):
                row.append(matrix1[i][j] + matrix2[i][j])
            sum.append(row)
        return sum


def mat_sub(matrix1,matrix2):
    sub = []
    if r1 == r2 and c1 == c2:
        for i in range(r1):
            row = []
            for j in range(c1):
                row.append(matrix1[i][j] - matrix2[i][j])
            sub.append(row)
        return sub

def trans(matrix1):
    global tran
    tran = []
    for i in range(c1):
        row = []
        for j in range(r1):
            row.append(matrix1[j][i])
        tran.append(row)
    return tran
        
print("Addition: ")
for i in mat_add(mat1(),mat2()):
    print(i)

print("Subtraction: ")
for i in mat_sub(mat1(),mat2()):
    print(i)

print("Transpose of matrix 1:")
for i in trans(mat1()):
    print(i)