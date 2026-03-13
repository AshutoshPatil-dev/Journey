a = int(input())
b = list(map(int, input().split()))

c = [x*x for x in b]

print(*c)
