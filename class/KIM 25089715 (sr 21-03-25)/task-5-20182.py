def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []
for n in range(1, 10000):
    r = convert(n, 3)
    if sum(map(int, r)) % 2 == 0:
        r = '12' + r[2:] + '0'
    else:
        r = '10' + r[2:] + '2'
    r = int(r, 3)
    if r > 105:
        ans.append(n)
print(min(ans))

# otvet: 28
