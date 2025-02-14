with open('17_19249.txt') as file:
    data = [int(i) for i in file]

max_43 = max(i for i in data if len(str(abs(i))) == 5 and str(i)[-2:] == '43')

ans = []
for i in range(len(data) - 2):
    num1, num2, num3 = data[i:i + 3]
    u1 = len(str(abs(num1))) == 5 and str(num1)[-2:] == '43'
    u2 = len(str(abs(num2))) == 5 and str(num2)[-2:] == '43'
    u3 = len(str(abs(num3))) == 5 and str(num3)[-2:] == '43'
    if (u1 or u2 or u3) and (num1 ** 2 + num2 ** 2 + num3 ** 2) <= max_43 ** 2:
        ans.append(num1 ** 2 + num2 ** 2 + num3 ** 2)
print(len(ans), min(ans))

# otvet: 92 838850571