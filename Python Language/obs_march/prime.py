a = int(input())
l = list(map(int, input().split()))
count = 0
for i in l:
    prime = True
    if i <=1:
        continue
    for j in range(2, int(i**0.5) +1):
        if i % j == 0:
            prime = False
            break
    if prime:
        count += 1
        
print(count)

