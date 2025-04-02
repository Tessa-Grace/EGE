def dividers(num):
    res = set()
    for num in range(2, int(num ** .5) + 1):
        if num % i == 0:
            res |= {i, num // i}

    res = sorted(res)
    if len(res) >= 2:
        m = max(res) - min(res)
        if str(m)[-1] == '6':
            return m
    return 0

count = 0
for i in range(300_001, 10 ** 20):
    ans = dividers(i)
    if ans:
        print(i, ans)
        count += 1
        if count == 5:
            break

