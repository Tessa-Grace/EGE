from itertools import *

alph = '01234'

ans = []
for val in product(alph, repeat=6):
    val = ''.join(val)
    if val[0] == '3' and int(val, 5) % 2 == 0:
        if val not in ans:
            ans.append(val)
print(len(ans))

#otvet: 1562