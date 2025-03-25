from math import *

ans = []
for x in range(0, 7):
    if (((7 - cos(4 * x))/ 2) ** 1.4) > ((-2) * cos(x)) and \
            0 <= x < (2 * pi):
        ans.append(x)
print(sum(ans))