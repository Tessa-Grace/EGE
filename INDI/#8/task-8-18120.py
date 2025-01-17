from itertools import product

alph = sorted('ПРЕСТОЛ')
gl = 'ЕО'

# ans = []
count = 0
for pos, val in enumerate(product(alph, repeat=5), start=1):
    val = ''.join(val)
    if val[-1] in gl and pos % 2 != 1 and \
            (val.count('П') + val.count('Р') + \
            val.count('С') + val.count('Т') + \
            val.count('Л')) <= 3:
        # или if sum([1 for i in val if i in sogl]) <= 3:
            # ans.append(pos)
        count += 1
print(count)

# otvet: 1776