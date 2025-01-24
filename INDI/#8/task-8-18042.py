from itertools import *

sogl = 'ЛСТР'
count = 0
for val in product(sorted('ЛЮСТРА'), repeat=5):
    val = ''.join(val)
    if val.count('Ю') <= 2 and val[-1] not in sogl:
        count += 1
print(count)

# otvet: 2400