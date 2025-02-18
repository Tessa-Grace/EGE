from itertools import product

alph = sorted('ШКОЛА')

for pos, val in enumerate(product(alph, repeat=5), start=1):
    val = ''.join(val)
    if val == 'ШАЛАШ':
        print(pos)

# otvet: 2555