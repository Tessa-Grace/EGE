from itertools import *

def f1(nums):
    return max(nums) < sum(nums) - max(nums)

def f2(nums):
    count = [nums.count(i) for i in nums]
    return count.count(2) == 2 and count.count(1) == 2

with open('9_4614.txt') as file:
    data = [list(map(int, i.split())) for i in file]

count = 0
for i in data:
    if f1(i) and f2(i):
        count += 1
print(count)

# otvet: 133