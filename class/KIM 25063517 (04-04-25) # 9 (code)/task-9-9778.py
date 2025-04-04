def f1(nums):
    count = [nums.count(i) for i in nums]
    return count.count(2) == 2 and count.count(1) == 4

def f2(nums):
    povt = [i for i in nums if nums.count(i) > 1]
    nepovt = [i for i in nums if nums.count(i) == 1]
    sr_nepovt = sum(nepovt) / len(nepovt)
    return povt[0] >= sr_nepovt

with open('09_9778.txt') as file:
    data = [list(map(int, i.split())) for i in file]

ans = []
count = 0
for i in data:
    count += 1
    if f1(i) and f2(i):
        ans.append(count)
print(min(ans))

# otvet: 34