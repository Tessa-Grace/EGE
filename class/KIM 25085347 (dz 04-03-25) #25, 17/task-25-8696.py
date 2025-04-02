def is_prime(num):
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            return False
    return True

def dividers(num):
    res = set()
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            res |= {i, num // i}

    res = sorted(res)
    if len(res) > 1:
        m = sum(res)
        if is_prime(m % 100_000):
            return m
count = 0
for i in range(1_273_547, 10 ** 20):
    res = dividers(i)
    if res:
        print(i, res)
        count += 1
        if count == 5:
            break
# otvet:
# 1273566 1637537
# 1273570 1139869
# 1273578 1287317
# 1273582 651769
# 1273590 2225609

