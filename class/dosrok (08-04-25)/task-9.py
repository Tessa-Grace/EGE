def f1(nums):
    count = [nums.count(i) for i in nums]
    return count.count(3) == 6 and count.count(1) == 1

def f2(nums):
    nepovt = [i for i in nums if nums.count(i) == 1]
    povt = [i for i in nums if nums.count(i) > 1]
    if max(povt) > max(nepovt):
        return True
    return False

with open('9.txt') as file:
    data = [list(map(int, i.split())) for i in file]

count = 0
for i in data:
    if f1(i) and f2(i):
        count += 1

print(count)

# otvet: 1