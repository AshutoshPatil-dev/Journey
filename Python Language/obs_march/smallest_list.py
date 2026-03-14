a = int(input())
b = list(map(int, input().split()))
smallest = b[0]
for i in b:
  if i < smallest:
    smallest = i
print(smallest)
