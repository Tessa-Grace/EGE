def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []
for n in range(1, 10000):
    r = convert(n, 3)
    if sum(map(int, r)) % 3 == 0:
        r = '20' + r
    else:
        r = '10' + r
    r = int(r, 3)
    if r < 100:
        ans.append(n)
print(max(ans))

# otvet: 18