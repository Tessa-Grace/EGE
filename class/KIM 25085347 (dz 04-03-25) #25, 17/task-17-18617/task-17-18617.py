with open('17_18617.txt') as file:
    data = [int(i) for i in file]

minn = min(data)
maxx = max(data)

ans = []
for i in range(len(data) - 1):
    num1, num2 = data[i:i + 2]

    u1_1 = num1 % 3 == maxx % 3
    u1_2 = num2 % 3 == maxx % 3

    u2_1 = num1 % 7 == minn % 7
    u2_2 = num2 % 7 == minn % 7

    if (u1_1 or u1_2) and (u2_1 or u2_2):
        ans.append(num1 + num2)
print(len(ans), max(ans))

# otvet: 1467 197700