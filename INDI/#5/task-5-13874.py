def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []
for n in range(1, 10000):
    r = convert(n, 4)
    if n % 3 == 0:
        r = r[-1] + r[1:-2] + r[0] + '1'
    else:
        r = r + str(n % 3)
    r = int(r, 4)
    if r <= 340:
        ans.append(r)
print(max(ans))

# otvet: 334
