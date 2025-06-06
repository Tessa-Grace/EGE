with open('17_21595.txt') as file:
    data = [int(i) for i in file]

sp = [i for i in data if len(str(abs(i))) == 4 and str(i)[-1] == '3']
sp_2 = len(sp) ** 2

ans = []
for i in range(len(data)-2):
    num1, num2, num3 = data[i:i + 3]

    u1 = num1 + num2 + num3 - min(num1, num2, num3) > sp_2
    u2 = (num1 == abs(num1) and num2 == abs(num2) and num3 == abs(num3)) or ((num1 < 0 and num2 < 0 and num3 < 0))

    if u1 and u2:
        ans.append(num1 + num2 + num3)

print(len(ans), max(ans))

# otvet: