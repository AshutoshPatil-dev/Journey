r = int(input("Enter rows: "))
c = int(input("Enter columns: "))

# input and print matrix
matrix = []
for i in range(r):
    row = []
    for j in range(c):
        row.append(int(input(f"Enter element [{i}][{j}]: ")))
    matrix.append(row)
    
print("Matrix:")
for i in matrix:
    print(i)

#Transpose
def tran():
    t = []
    for i in range(c):
        row = []
        for j in range(r):
            row.append(matrix[j][i])
        t.append(row)

    print("\nTransspose:")
    for i in t:
        print(i)



def sy():
    if r != c:
        print("\nMatrix is not symmetric.")
    else:
        sym = True
        for i in range(r):
            for j in range(c):
                if matrix[i][j] != matrix[j][i]:
                    sym = False
                    break


        if sym:
            print("\nIt's symmetric.")
        else:
            print("\nIt ain't symmetric boi..")

tran()
sy()