def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []
for x in range(1, 2005):
    num = 4**163 * 5 + 12 ** 62 - x
    num = convert(num, 5)
    if num.count('1') < num.count('4'):
        ans.append(x)

print(max(ans))

# otvet: 2000