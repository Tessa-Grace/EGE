from itertools import permutations

count = 0

for val in set(permutations('ХОЧУ В ВУЗ.')):
    val = ''.join(val)
    v = val.split()
    if len(v) == 3 and val[-1] == '.' and val[-2] != ' ' and all(word[0] != 'У' for word in v):
        count += 1
print(count - 1)

# otvet: 75599