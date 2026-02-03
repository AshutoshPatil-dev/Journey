#Program to display Fibonacci series up to n terms. 
fibo = int(input("Enter number of terms: "))

a = 0
b = 1

for i in range(fibo-1):
    print(a, end=" ")
    res = a + b
    a = b
    b = res
