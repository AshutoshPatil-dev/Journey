nums = [34,5,90,56,656,53,34]

largest = nums[0]

for x in nums:
    if x > largest:
        largest = x
print(largest)