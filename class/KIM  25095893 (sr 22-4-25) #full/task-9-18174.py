def f1(nums):
    count = [nums.count(i) for i in nums]
    return count.count(2) == 2 and count.count(1) == 4

def f2(nums):
    minus = [i for i in nums if i < 0]
    plus = [i for i in nums if i > 0]
    return abs(sum(minus)) > sum(plus)

with open('9_18174.txt') as file:
    data = [list(map(int, i.split())) for i in file]

count = 0
for i in data:
    if f1(i) and f2(i):
        count += 1
print(count)

# otvet: 44