from itertools import *

count = 0
for val in set(permutations('АССЕМБЛЕР', 9)):
    val = ''.join(val)
    summ = 0
    for i in range(len(val)):
        if val[i] == 'А' or val[i] == 'Е':
            summ += i + 1
    if summ == 9:
        count += 1
print(count)

# otvet: 3240