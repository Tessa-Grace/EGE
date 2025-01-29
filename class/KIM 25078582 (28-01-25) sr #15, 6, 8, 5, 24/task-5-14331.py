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
        r += '212'
    else:
        r += convert(sum(map(int, r)) * 2, 3)
    r = int(r, 3)
    if r > 490:
        ans.append(r)
print(min(ans))

# otvet: 512