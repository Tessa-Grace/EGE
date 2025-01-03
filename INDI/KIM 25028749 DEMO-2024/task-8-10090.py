from itertools import permutations

count = 0
for val in permutations('01234567', 5):
    val = ''.join(val)
    if val[0] != '0' and len(val) == len(set(val)) and val.count('1') == 0:
        val = val.replace('0', '*').replace('2', '*').replace('4', '*').replace('6', '*')
        val = val.replace('1', '!').replace('3', '!').replace('5', '!').replace('7', '!')
        if '**' not in val and '!!' not in val:
            count += 1
print(count)

# otvet: 504

