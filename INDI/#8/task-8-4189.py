from itertools import *

ans = []
for pos, val in enumerate(product(sorted('БАТЫР'), repeat=5), start=1):
    val = ''.join(val)
    if val.count('Ы') == 0 and 'АА' not in val:
        ans.append(pos)
print(ans[0])

# otvet: 131