from fnmatch import fnmatch

def div(num):
    res = set()
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            res |= {i, num // i}

    res_24 = []
    for i in res:
        if fnmatch(str(i), '4*'):
            res_24.append(i)
    return res_24


for num in range(10 ** 6):
    res = div(num)
    if len(res) == 24:
        print(num, max(res))

# otvet: 997920 498960