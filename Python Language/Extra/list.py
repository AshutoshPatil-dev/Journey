nums = [1, 2, 3, 4, 5, 6]
count = 0

for x in nums:
    if x % 2 == 0:
        count = count + 1
print(count)
print(len(nums)) #Gives the length of the list, here it is 6