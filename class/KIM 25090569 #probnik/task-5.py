def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []
for n in range(1, 10000):
    r = convert(n, 4)
    if sum(map(int, r)) % 2 == 0:
        r = r + r[-2:]
    else:
        r = '2' + r + '0'
    r = int(r, 4)
    if r > 120 and r % 2 == 0:
        ans.append(r)

print(min(ans))

# otvet: 136