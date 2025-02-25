with open('17_4597.txt') as file:
    data = [int(i) for i in file]

minn = min(data)
ans = []
for i in range(len(data)-1):
    num1, num2 = data[i], data[i + 1]

    u1 = num1 % 117 == minn
    u2 = num2 % 117 == minn

    f1 = u1 + u2 > 0

    if f1:
        ans.append(num1 + num2)

print(len(ans), max(ans))

# otvet: 175 173738