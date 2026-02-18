a = int(input("Enter a number to check for prime: "))
if a <= 1:
    print(False)
else:
    for i in range(2, a):
        if a % i == 0:
            print(False)
            break
    else:
        print(True)