def dividers(num):
    res = set()
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0 and i % 2 != 0:
            res |= {i, num // i}

    res = sorted(res)
    if len(res) > 5:
        d = list(res)[-6]
        return d
    return 0

count = 0
for i in range(200_000_000, 10 ** 20):
    res = dividers(i)
    if res:
        print(i, res)
        count += 1
        if count == 5:
            break

# otvet:
# 200000000 3125
# 200000003 48391 +
# 200000004 90212
# 200000005 5     +
# 200000008 39208