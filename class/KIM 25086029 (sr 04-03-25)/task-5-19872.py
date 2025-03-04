def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []
for n in range(1, 10000):
    r = convert(n, 7)
    if n % 2 == 0:
        r = '52' + r + '1'
    else:
        r = r[-1] + r[1:-1] + r[0] + '15'
    r = int(r)
    if n <= 1000:
        if len(str(r)) == 4:
            ans.append(n)
print(max(ans))

# otvet: 721