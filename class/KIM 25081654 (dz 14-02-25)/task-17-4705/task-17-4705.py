with open('17_4705.txt') as file:
    data = [int(i) for i in file]

max_3 = max(i for i in data if str(i)[-1] == '3')

ans = []
for i in range(len(data) - 1):
    num1, num2 = data[i:i+2]
    u1 = str(num1)[-1] == '3'
    u2 = str(num2)[-1] == '3'
    if u1 + u2 == 1 and (num1 ** 2 + num2 ** 2) >= max_3 ** 2:
        ans.append(num1 ** 2 + num2 ** 2)
print(len(ans), max(ans))

# otvet: 180 190360573