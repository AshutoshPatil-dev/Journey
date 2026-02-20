n = int(input("Enter a number: "))

if n == 1:
    print("Not prime")
else:
    for i in range(2,n):
        if n % 2 == 0:
            print("It's not prime")
            break
    else:
        print("It is prime")