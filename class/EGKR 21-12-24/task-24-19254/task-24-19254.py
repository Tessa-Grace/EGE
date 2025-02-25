with open('24_19254.txt') as file:
    data = file.readline()

data = data.split('FSRQ')

ans = 0
for i in range(len(data) - 80):
    ans = max(ans, len('FSRQ'.join(data[i:i+83])))
print(ans)

#otvet: 2407 ОШИБКА!
'''
Предлагают такое решение (переписала немного под себя):

with open('24_19254.txt') as file:
    data = file.readline()
count, length, maxx = 0, 0, 0

for i in range(3, len(data)):
    if data[i-3] + data[i-2] + data[i-1] + data[i] == 'FSRQ':
        count += 1
    while count > 80:
        if data[i] + data[i+1] + data[i+2] + data[i+3] == 'FSRQ':
            count -= 1
        length += 1
    if count == 80:
        maxx = max(maxx, i-length+1)
print(maxx)

#otvet: 2379
'''