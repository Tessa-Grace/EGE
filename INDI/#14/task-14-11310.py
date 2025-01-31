from string import digits, ascii_uppercase

alph = digits + ascii_uppercase

ans = []
for x in alph[:24]:
    num1 = int('4M' + x + 'F', 24)
    num2 = int('265AFDN' + x, 24)
    num3 = int('N4' + x + '931B3L', 24)
    num4 = int('NG' + x + '4F', 24)
    num5 = int('FKJB5' + x + 'IK', 24)
    num = num1 + num2 + num3 + num4 + num5
    if num % 23 == 0:
        ans.append(num // 23)
print(min(ans))

# otvet: 114549282042
