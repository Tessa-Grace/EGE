def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []
for n in range(1, 10_000):
    r = convert(n, 6)
    if sum(map(int, r)) % 5 == 0:
        r = r.replace('0', '*')
        r = r.replace('3', '0')
        r = r.replace('*', '3')
        r += '11'
    else:
        r += '44'
        r = r[0] + '0' + '5' + r[3:]
    r = int(r, 6)
    if r > 1500:
        ans.append([r, -n])

ans.sort()
print(ans[:100])
print(abs(ans[0][1]))

# otvet: 71