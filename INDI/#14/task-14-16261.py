from string import digits, ascii_uppercase

alph = digits + ascii_uppercase

ans = []
for x in alph[:21]:
    for y in alph[:21]:
        num1 = int('943697' + x +'21', 21)
        num2 = int('2' + y + '9253', 21)
        num = num1 + num2
        if num % 20 == 0:
            ans.append([int(x, 36) - int(y, 36), num // 20])
print(max(ans))

# [18, 17395098353]
# otvet: 17395098353