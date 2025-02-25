# _________________________________________________
#                     1 METHOD
# _________________________________________________

# 10000000000
# 0136******

from itertools import product

ans = []
for r in range(7):
    for z in product('13579', repeat=r):
        z = ''.join(z)
        for v in '2468':
            num = int(f'{v}136{z}')
            if num <= 10 ** 10 and num % 53191 == 0:
                ans.append([num, num // 53191])
ans = sorted(ans)
for i in ans:
    print(*i)
# выдает только 6136379715 115365
# ___________________________________________________
#                     2 METHOD
# ___________________________________________________

from fnmatch import fnmatch

for i in range(53191, 10 ** 10, 53191):
    if fnmatch(str(i), '?136*') and str(i)[0] in '2468' and \
            str(i)[-1] in '13579' and i % 53191 == 0:
        print(i, i // 53191)

# otvet:
# 8136574079 152969
# 8136680461 152971
# 8136786843 152973
# 8136893225 152975
# 8136999607 152977