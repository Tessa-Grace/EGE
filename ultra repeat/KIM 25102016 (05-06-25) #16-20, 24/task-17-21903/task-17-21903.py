with open('17_21903.txt') as file:
    data = [int(i) for i in file]

minn = min(i for i in data if len(str(abs(i))) == 3 and str(i)[-2:] == '15')

ans = []
for i in range(len(data)-2):
    num1, num2, num3 = data[i:i + 3]

    u1 = (min(num1, num2, num3) * max(num1, num2, num3)) > minn ** 2
    u2 = (num1 == abs(num1) and num2 == abs(num2) and num3 == abs(num3)) or ((num1 < 0 and num2 < 0 and num3 < 0))

    if u1 and u2:
        ans.append(min(num1, num2, num3) * max(num1, num2, num3))

print(len(ans), min(ans))

# otvet: 3507 863808