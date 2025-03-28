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
    m = sum(res)
    if is_prime(m):
        return 0
    return m

count = 0
for i in range(1_273_548, 10 ** 20):
    ans = dividers(i)
    if ans:
        print(i, ans)
        count += 1
        if count == 5:
            break
# otvet:
# 1273548 1698091
# 1273550 1095345
# 1273551 513968
# 1273552 1601263
# 1273553 5934