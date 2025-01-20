from itertools import permutations

alph = 'ЛЕВИОСА'
gl = 'ЕИОА'
sogl = 'ЛВС'

count = 0
for val in permutations(alph, 7):
    val = ''.join(val)
    if val[0] not in gl and val[3] not in sogl:
        count += 1
print(count)

# otvet: 1440