with open('17_5882.txt') as file:
    data  = [int(i) for i in file]

minnn = []
for i in range(len(data) - 1):
    num1, num2 = data[i:i + 2]

    u1 = str(num1)[-1] == '3'
    u2 = str(num2)[-1] == '3'
    if u1 + u2 == 1:
        minnn.append(min(num1, num2))

minx4 = abs(min(minnn))
summ = sum(int(i) ** 2 for i in str(minx4))

ans = []
for i in data:
    if str(i).count('3') >= 1 and i >= summ:
        ans.append(i)
print(len(ans), min(ans))

# otvet: 893 237