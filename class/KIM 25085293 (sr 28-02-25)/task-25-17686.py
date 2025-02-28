def dividers(num):
    res = set()
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            res |= {i, num // i}
    res = sorted(res)

    for i in res:
        if i % 10 == 7 and i != 7:
            return i
    return 0

count = 0
for i in range(700_001, 10 ** 20):
    res = dividers(i)
    if res:
        print(i, res)
        count += 1
        if count == 5:
            break

# otvet:
# 700002 27
# 700003 37
# 700005 6087
# 700007 77
# 700008 29167