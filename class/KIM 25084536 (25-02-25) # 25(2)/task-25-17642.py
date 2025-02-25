def dividers(num):
    res = set()
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            res |= {i, num //i}
    res = sorted(res)

    for i in res:
        if i % 10 == 9 and i != 9:
            return i
    return 0

count = 0
for i in range(800_001, 10 ** 20):
    res = dividers(i)
    if dividers(i):
        print(i, res)
        count += 1
        if count == 5:
            break

# otvet:
# 800001 309
# 800003 47059
# 800004 409
# 800006 269
# 800007 39