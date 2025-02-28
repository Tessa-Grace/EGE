with open('17_12450.txt') as file:
    data = [int(i) for i in file]

min_52 = min(i for i in data if i % 52 == 0)

ans = []
for i in range(len(data) - 2):
    num1, num2, num3 = data[i: i + 3]

    u1 = num1 % 113
    u2 = num2 % 113
    u3 = num3 % 113

    if (u1 + u2 + u3) == min_52:
        ans.append(num1 + num2 + num3)

print(len(ans), max(ans))
# otvet: 7 77457