def dividers(num):
    res = set()
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            res |= {i, num // i}

    res = sorted(res)
    if len(res) >= 7:
        d = res[-7]
        if d > 0:
            return d
    return 0

count = 0
for num in range(400_000_001, 10 ** 20):
    res = dividers(num)
    if res:
        print(res)
        count += 1
        if count == 5:
            break
# otvet:
# 34
# 2962963
# 1793722
# 21052632
# 754717

# но как найти количество делителей?
