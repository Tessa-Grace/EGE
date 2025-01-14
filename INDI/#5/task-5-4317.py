def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []
for n in range(1, 10000):
    r = convert(n, 5)
    if int(r[-1]) % 2 == 0:
        r = r + '2'
    else:
        r = '2' + r + '3'
    r = int(r, 5)
    if r < 1000:
        ans.append(n)
print(max(ans))

# otvet: 199