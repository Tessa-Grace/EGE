from string import digits, ascii_uppercase

alph = digits + ascii_uppercase

ans = []
for x in alph[:19]:
    num1 = int('98' + x + '79641', 19)
    num2 = int('36' + x + '14', 19)
    num3 = int('73' + x + '4', 19)
    num = num1 + num2 + num3
    if num % 18 == 0:
        ans.append(num // 18)
print(max(ans))

# otvet: 470402599