def f1(nums):
    count = [nums.count(i) for i in nums]
    return count.count(3) == 3 and count.count(1) == 4

def f2(nums):
    nepovt = [i for i in nums if nums.count(i) == 1]
    povt = [i for i in nums if nums.count(i) > 1]
    sr_nepovt = sum(nepovt) / len(nepovt)
    sr_povt = sum(povt) / len(povt)
    if sr_nepovt <= sr_povt:
        return True

with open('9_9740.txt') as file:
    data = [list(map(int, i.split())) for i in file]

count = 0
for i in data:
    if f1(i) and f2(i):
        count += 1
print(count)

# otvet: 36