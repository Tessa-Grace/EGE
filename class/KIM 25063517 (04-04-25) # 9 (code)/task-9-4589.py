from itertools import *

def f1(nums):
    return max(nums) < sum(nums) - max(nums)

def f2(nums): # 1 2 3 4
    for i in permutations(nums):
        if sum(i[:2]) == sum(i[2:]):
            return True
    return False

# второй способ
def f3(nums):
    for i in combinations(nums, 2):
        if sum(i) == sum(nums) - sum(i):
            return True
    return False

# третий способ
def f4(nums): # 100 100 1 1
    return min(nums) + max(nums) == sum(nums) - min(nums) - max(nums)


with open('9_4589.txt') as file:
    data = [list(map(int, i.split())) for i in file]

count = 0
for i in data:
    if f1(i) and f2(i):
        count += 1
print(count)

# otvet: 104