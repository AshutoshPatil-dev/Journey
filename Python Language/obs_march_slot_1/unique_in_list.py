n = int(input())
nums = list(map(int, input().split()))

unique = []

for i in nums:
    if i not in unique:
        unique.append(i)

for i in unique:
    print(i, end=" ")