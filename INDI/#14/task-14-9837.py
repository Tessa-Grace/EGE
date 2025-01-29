from string import digits, ascii_uppercase

alph = digits + ascii_uppercase

ans = []
for x in alph[:23]:
    num1 = int('7' + x + '38596', 23)
    num2 = int('14' + x + '36', 23)
    num3 = int('61' + x + '7', 23)
    num = num1 + num2 + num3
    if num % 22 == 0:
        ans.append(num // 22)
print(min(ans))

# otvet: 47163321