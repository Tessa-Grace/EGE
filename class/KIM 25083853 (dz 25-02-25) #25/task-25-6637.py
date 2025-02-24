# _________________________________________________
#                     1 METHOD
# _________________________________________________

# 10000000000
# 1021390000

from itertools import product

ans = []
for r in range(5):
    for z in product('0123456789', repeat=r):
        z = ''.join(z)
        for v in '0123456789':
            num = int(f'1{v}2139{z}4')
            if num <= 10 ** 10 and num % 3052 == 0:
                ans.append([num, num // 3052])
ans = sorted(ans)
for i in ans:
    print(*i)

# ___________________________________________________
#                     2 METHOD
# ___________________________________________________

from fnmatch import fnmatch

for i in range(3052, 10 ** 10, 3052):
    if fnmatch(str(i), '1?2139*4'):
        if i % 3052 == 0:
            print(i, i // 3052)

# otvet:
# 1421398804 465727
# 1521397584 498492
# 1621396364 531257
# 1721395144 564022
# 1821393924 596787
# 1921392704 629552