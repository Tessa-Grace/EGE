# _________________________________________________
#                     1 METHOD
# _________________________________________________

# 10000000000
# *****12040

from itertools import product

ans = []
for r in range(6):
    for z in product('02468', repeat=r):
        z = ''.join(z)
        for v1 in '13579':
            for v2 in '13579':
                num = int(f'{z}12{v1}4{v2}')
                if num <= 10 ** 10 and num % 9231 == 0:
                    ans.append([num, num // 9231])
ans = sorted(ans)
for i in ans:
    print(*i)

# ___________________________________________________
#                     2 METHOD
# ___________________________________________________
'''
from fnmatch import fnmatch

for i in range(9231, 10 ** 10, 9231):
    if fnmatch(str(i), '*12?4?') and i % 9231 == 0:
        print(i, i // 9231)
'''
# otvet:
# 608812143 65953
# 2086012149 225979
# 4440212541 481011
# 6286412541 681011
# 8486012145 919295