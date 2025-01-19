with open('26_4604.txt') as file:
    N = int(file.readline())
    size = [int(i) for i in file]

size = sorted(size, reverse=True)

count = 1
cur = size[0]
for i in size:
    if cur - i >= 3:
        cur = i
        count += 1
print(count, cur)
