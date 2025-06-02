def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []
for n in range(1, 10_000):
    r = convert(n, 2)
    r += str(sum(map(int, r)) % 2)
    r += str(sum(map(int, r)) % 2)
    r = int(r, 2)
    if r > 253:
        ans.append(n)

print(min(ans))

# otvet: 64