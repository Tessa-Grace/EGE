from itertools import product, repeat

alph = 'ЯСНОВИДЕЦ'
gl = 'ЯОИЕ'
sogl = 'СНВДЦ'

count = 0
for val in product(alph, repeat=5):
    val = ''.join(val)
    if val[0] in sogl and val[-1] in gl and \
        val.count(val[0]) == 1 and val.count(val[-1]) == 1:
        count += 1

print(count)

# otvet: 6860