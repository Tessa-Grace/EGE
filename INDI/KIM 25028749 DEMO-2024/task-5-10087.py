def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []
for n in range(1,10000):
    r = convert(n, 2)
    if n % 3 == 0:
        r = r + r[-3:]
    else:
        r = r + convert((n % 3) * 3, 2)
    r = int(r, 2)
    if r > 151:
        ans.append(r)
print(min(ans))

# otvet: 163