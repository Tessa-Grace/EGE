from itertools import *

def f1(nums):
    cnt = [nums.count(i) for i in nums]
    return cnt.count(1) == 5

def f2(nums):
    nums.sort()
    return sum(nums[-2:]) <= sum(nums) - sum(nums[-2:])

with open('9_21895.txt') as file:
    data = [list(map(int, i.split())) for i in file]

count = 0
for i in data:
    if f1(i) and f2(i):
        count += 1
print(count)

# otvet: 1922