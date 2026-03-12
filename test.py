def sums(*s):
    t = 0
    for i in s:
        t += i
    return t, t / len(s)

num = list(map(int, input().split()))
s, avg = sums(*num)

print(f"Sum: {s}\nAvg: {avg}")