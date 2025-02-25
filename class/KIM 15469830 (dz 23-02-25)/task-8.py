from itertools import product

alph = sorted(set('КАЛЕЙДОСКОП'), reverse=True) # надо множество из-за повторяющихся букв + в обратном порядке

ans = []
for pos, val in enumerate(product(alph, repeat=6), start=0): # начало с 0, а не с 1
    val = ''.join(val)
    if pos % 2 == 0 and val[0] == 'К' and val.count('Й') >= 2 and \
        'С' not in val and 'Е' not in val:
        ans.append(pos)
print(ans[0])

# otvet: 243698