from string import printable

ans = []
for x in printable[:25]:
    num1 = int('A4' + x + '7F2', 25)
    num2 = int('N' + x + 'G5' + x + 'H', 25)
    num3 = int('74' + x + 'M26', 25)
    num = num1 + num2 + num3
    if num % 24 == 0:
        ans.append(num // 24)
print(max(ans))

# otvet: 16751575