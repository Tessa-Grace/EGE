def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []
for x in range(1, 2031):
    num = convert(3**100 - x, 3)
    if num.count('0') == 1:
        ans.append(x)
print(max(ans))

# otvet: 1823