from itertools import *

alph = sorted('ЕВЛАМПИЙ')

count = 0
for val in product(alph, repeat=18):
    val = ''.join(val)
    if val[:8] == 'ПИЛАЕВЛА' and \
            (val.count('Е') + val.count('А') + val.count('И')) == \
            (val.count('В') + val.count('Л') + val.count('М') + val.count('П') + val.count('Й')):
        count += 1
print(count)
