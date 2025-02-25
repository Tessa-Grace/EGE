with open('17.txt') as file:
    data = [int(i) for i in file]

max_50 = max(i for i in data if str(i)[-2:] == '50')

ans = []
for i in range(len(data) - 2):
    num1, num2, num3 = data[i:i + 3]
    summ = num1 + num2 + num3

    u1 = len(str(abs(num1))) == 5 and num1 != num2 and num2 != num3 and num1 != num3
    u2 = len(str(abs(num2))) == 5 and num1 != num2 and num2 != num3 and num1 != num3
    u3 = len(str(abs(num3))) == 5 and num1 != num2 and num2 != num3 and num1 != num3

    f1 = u1 * u2 * u3 == 1
    f2 = summ <= max_50

    if f1 and f2:
        ans.append(summ)
print(len(ans), max(ans))

# otvet: 72 58037