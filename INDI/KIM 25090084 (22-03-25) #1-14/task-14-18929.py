def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []
for x in range(2025):
    num = 9**2024 + 9**1987 - x
    num = convert(num, 9)
    if num.count('8') == 1984:
        ans.append(x)
print(max(ans))

# print: 2017