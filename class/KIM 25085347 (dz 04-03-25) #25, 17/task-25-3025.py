def dividers(num):
    res = set()
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            if i % 2 != 0:
                res |= {i}
            if num // i % 2 != 0:
                res |= {num // i}

    res = sorted(res)
    if len(res) >= 6:
        d = list(res)[-6]
        return d
    return 0

count = 0
for num in range(200_000_001, 10 ** 20):
    res = dividers(num)
    if res:
        print(num, res)
        count += 1
        if count == 5:
            break
# otvet:
# 200000003 48391
# 200000004 42123
# 200000005 5
# 200000008 5101
# 200000009 113443