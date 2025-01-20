from itertools import product

alph = sorted(set('МАРИНА'))

ans = []
for val in product(alph, repeat=5):
    val = ''.join(val)
    ans.append(val)
ans.sort()
print(ans.index('НАИРИ') + 1)

# otvet: 1922
