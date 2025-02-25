from fnmatch import fnmatch
from math import gcd

for i in range(7777, 10 ** 10, 7777):
    if fnmatch(str(i), '12*567?') and i % 7777 == 0 and (gcd(i) + 1) % 2 != 0:
        #print(gcd(i), lcm(i))
        print(i, i // 7777)

# print:
# 121025674 15562
# 1209805674 155562
# 1220895676 156988
# 1231985678 158414
# 1265395670 162710
# 1276485672 164136
# 1287575674 165562
# 1298665676 166988