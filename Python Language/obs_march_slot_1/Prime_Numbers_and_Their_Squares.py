n = int(input())
nums = list(map(int, input().split()))

found = False

for x in nums:
    if x > 1:
        prime = True
        for i in range(2, x):
            if x % i == 0:
                prime = False
                break
        
        if prime:
            print(x * x, end=" ")
            found = True

if not found:
    print(-1)
