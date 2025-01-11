def f1(line):
    return line.count(min(line)) == 1

def f2(line):
    return len(line) != len(set(line))

def f3(line):
    povt = [i for i in line if line.count(i) > 1]
    return min(line) + max(line) < sum(povt)

with open('09_10910.txt') as file:
    arr = [list(map(int, i.split())) for i in file]

count = 0
for i in arr:
    if all([f1(i), f2(i), f3(i)]):
        count += 1
print(count)