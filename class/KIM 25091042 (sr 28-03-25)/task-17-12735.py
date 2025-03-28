with open('17_12735.txt') as file:
    data = [int(i) for i in file]

max_9 = max(i for i in data if str(i)[-2:] == '09')

ans = []
for i in range(len(data) - 2):
    num1, num2, num3 = data[i:i + 3]

    u1 = num1 % 7 == 0
    u2 = num2 % 7 == 0
    u3 = num3 % 7 == 0

    if u1 + u2 + u3 == 2:
        ans.append(num1 * num2 * num3)

print(len(ans), min(ans))

# otvet: 348 8820