def dividers(num):
    res = set()
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            res |= {i, num // i}

    res = sorted(res)
    if len(res) >= 2:
        m = sum(res[-2:])
        if m % 10000 == 1214:
            return m
    return 0

for n in range(112_500_000, 112_550_001):
    res = dividers(n)
    if res:
        print(n)
# otvet:
# 112508413
# 112520369
# 112523549
# 112534952



