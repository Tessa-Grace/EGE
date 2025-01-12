def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []
for n in range(1, 10000):
    r = convert(n, 3)
    r = r.replace('2', '*')
    r = r.replace('0', '2')
    r = r.replace('*', '0')
    r = int(r, 3)
    r = abs(n - r)
    if r == 378:
        ans.append(n)
print(min(ans))

# otvet: 553