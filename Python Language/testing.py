from math_utils.basics.add import addition
import math
import random
import os
from time import sleep
from datetime import datetime
import statistics
print(addition(1,5))
print(math.sqrt(3))

print(os.getcwd())
print(os.listdir())

a = datetime.now()
print(a)

for i in range(10,0,-1):
    print(i)
else:
    print("Boom")

data = [1,2,3]

print(f"Mean: {statistics.mean(data)}")