ans = []
for x in range(1, 100_000):
    n = 3**2000 + 3**10 - x
    res = ''
    while n:
        res += str(n % 3)
        n //= 3
    if res.count('2') == 2000:
        ans.append(x)
print(min(ans))
