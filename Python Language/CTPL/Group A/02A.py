fibo = int(input("Enter the term till you want the fibonacci: "))

a = 0
b = 1
i = 0
print(a)
print(b)
for i in range(fibo-1):
 res = a + b
 print(res)
 a = b
 b = res
