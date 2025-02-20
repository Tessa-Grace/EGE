#3163

with open('24_3163.txt') as file:
    data = file.readline()
data = data.replace('PR', '*')
data = data.replace('ST', '*')

ans = 0
for i in range(len(data)):
    count = 0
    count_zv = 0
    for j in range(i, len(data)):
        if data[j] == '*':
            count_zv += 1
        else:
            count += 1
        if count_zv == 2:
            break
    ans = max(ans, count)
print(ans)

# otvet: 4931 ошибка

