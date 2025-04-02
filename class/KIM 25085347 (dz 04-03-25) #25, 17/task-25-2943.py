def dividers(num):
    res = set()
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            res |= {i, num // i}
    res = sorted(res)

    if len(res) > 1:
        m = min(res) + max(res)
        if m % 10 == 4:
            return m
    return 0

count = 0
for i in range(220_000, 10 ** 20):
    res = dividers(i)
    if res:
        print(i, res)
        count += 1
        if count == 5:
            break
# otvet:
# 220004 110004
# 220023 73344
# 220024 110014
# 220033 20014
# 220043 1044