from string import digits,ascii_lowercase

alph = digits + ascii_lowercase

ans = []
for x in alph[:25]:
    num1 = '11353' + x + '12'
    num2 = '135'+ x + '21'
    num = int(num1, 25) + int(num2, 25)
    if num %  24 == 0:
        res = num // 24
        ans.append(res)
print(max(ans))

# otvet: 266249847