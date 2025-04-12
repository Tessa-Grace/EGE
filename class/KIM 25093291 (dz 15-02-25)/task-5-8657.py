def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []
for n in range(1, 10000):
    r = convert(n, 3)
    if n % 5 == 0:
        r += r[-3:]
    else:
        r += convert((n % 5)* 5, 3)
    r = int(r, 3)
    if r < 5496:
        ans.append(n)
print(max(ans))

# otvet: 606