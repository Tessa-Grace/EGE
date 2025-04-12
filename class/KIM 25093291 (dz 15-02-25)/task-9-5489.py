from itertools import *

def f1(nums):
    count = [nums.count(i) for i in nums]
    return count.count(1) == 5

def f2(nums):
    chet = [i for i in nums if i % 2 == 0]
    nechet = [i for i in nums if i % 2 != 0]
    return len(chet) > len(nechet)

def f3(nums):
    chet = sum(i for i in nums if i % 2 == 0)
    nechet = sum(i for i in nums if i % 2 != 0)
    return chet < nechet

with open('9_5489.txt') as file:
    data = [list(map(int, i.split())) for i in file]

count = 0
for i in data:
    if f1(i) and f2(i) and f3(i):
        count += 1
print(count)

# otvet: 241