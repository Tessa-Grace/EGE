def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []
for n in range(1, 10_000):
    r = convert(n, 3)
    if n % 3 == 0:
        r += r[:3]
    else:
        r += convert((sum(map(int, r)) * 5), 3)
    r = int(r, 3)
    if r > 2500 and r % 2 != 0:
        ans.append(r)
print(min(ans))

# otvet: 2521