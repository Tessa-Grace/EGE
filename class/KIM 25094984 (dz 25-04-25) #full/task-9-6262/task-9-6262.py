def f1(nums):
    return len(set(nums)) < 6

def f2(nums):
    nechet = [i for i in nums if i % 2 != 0]
    return len(nechet) == 3

with open('9_6262.txt') as file:
    data = [list(map(int, i.split())) for i in file]

count = 0
for i in data:
    if f1 != f2:
        count += 1
print(count)

# MISTAKE