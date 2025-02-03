def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []
for x in range(1, 2006):
    num = 43**56 + 113**841 - x
    res = convert(num, 4)
    num = str(num)
    chet = res.count('0') + res.count('2')
    nechet = res.count('1') + res.count('3')
    if chet % 2 == 0 and nechet % 2 == 0 and res.count('2')<= 712:
        ans.append(x)
print(max(ans))

# otvet: 2003