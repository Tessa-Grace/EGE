from string import digits, ascii_uppercase

alph = digits + ascii_uppercase

ans = []
for x in alph[:22]:
    num1 = int('18' + x + '89957', 22)
    num2 = int('80' + x + '33', 22)
    num3 = int('521' + x + '6', 22)
    num = num1 + num2 + num3
    if num % 21 == 0:
        ans.append(num // 21)
print(min(ans))

# otvet: 162947670