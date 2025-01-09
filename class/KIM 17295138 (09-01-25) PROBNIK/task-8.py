from itertools import product
from string import ascii_uppercase

count = 0
for val in product(ascii_uppercase[:7], repeat=6):
    val = ''.join(val)
    if val[0] not in 'ae' and val[-1] not in 'ae':
        count += 1
print(count)

# otvet: 117649