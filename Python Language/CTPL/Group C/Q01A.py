def rec(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*rec(n-1)

print(rec(int(input("Enter a number: "))))

