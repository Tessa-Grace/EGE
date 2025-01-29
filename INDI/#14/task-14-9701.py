from string import digits, ascii_uppercase

alph = digits + ascii_uppercase

ans = []
for x in alph[:17]:
    num1 = int('12346' + x + '17', 17)
    num2 = int('7' + x + '171', 17)
    num = num1 + num2
    if num % 16 == 0:
        ans.append(num // 16)
print(min(ans))

# otvet: 28990177