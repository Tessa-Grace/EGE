# 14327


def convert(num, sys):
    if num == 0:
        return '0'
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []
for n in range(1, 10000):
    r = convert(n, 8)
    if n % 2 == 0:
        r = r + max(str(r))
    else:
        minn = int(min(r)) * 2
        r = r + convert(minn, 8)
    r = int(r, 8)
    if r < 313:
        ans.append(n)
print(max(ans))