with open('17_9786.txt') as file:
    data = [int(i) for i in file]

max_25 = max([i for i in data if str(i)[-2:] == '25'])
ans = []

for i in range(len(data) - 2):
    num1, num2, num3 = data[i:i + 3]
    u1 = len(str(abs(num1))) == 4
    u2 = len(str(abs(num2))) == 4
    u3 = len(str(abs(num3))) == 4

    summ = u1 + u2 + u3

    if summ <= 2 and num1 + num2 + num3 <= max_25:
        ans.append(num1 + num2 + num3)
print(len(ans), max(ans))

# otvet: 6315 84523
