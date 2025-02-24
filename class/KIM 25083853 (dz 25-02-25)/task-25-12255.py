# _________________________________________________
#                     1 METHOD
# _________________________________________________

# 1000000000000
# 120300456009
'''
from itertools import product

ans = []
for r in range(3):
    for z in product('0123456789', repeat=r):
        z = ''.join(z)
        for v1 in '0123456789':
            for v2 in '0123456789':
                for v3 in '0123456789':
                    num = int(f'12{v1}3{z}456{v2}{v3}9')
                    if num <= 10 ** 12 and num % 98591 == 0:
                        ans.append([num, num //98591])
ans = sorted(ans)
for i in ans:
    print(*i)
'''
# ___________________________________________________
#                     2 METHOD
# ___________________________________________________

from fnmatch import fnmatch

for i in range(98591, 10 ** 12, 98591):
    if fnmatch(str(i), '12?3*456??9') and i % 98591 == 0:
        print(i, i // 98591)

# otvet:
# 120313456439 1220329
# 120383456049 1221039
# 125351456539 1271429