from fnmatch import fnmatch

def dividers(num):
    res = set()
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            res |= {i, num // i}
    res = sorted(res)
    if len(res) == 18:
        return res
    return 0


for i in range(1, 10 ** 7):
    if fnmatch(str(i), '12?*45'):
        res = dividers(i)
        if res:
            print(i, max(res))

# otvet:
# 1202445 400815
# 1234845 411615
# 1251045 417015
# 1259145 419715
# 1283445 427815
# 1299645 433215
