from itertools import permutations

alph = '01234567'

count = 0
for val in permutations(alph, 6):
    val = ''.join(val)
    if val[0] != '0' and int(val, 8) % 5 == 0:
        for i in val:
            if i.count(i) == 1:
                val = val.replace('0', '*').replace('2', '*').replace('4', '*').replace('6', '*')
                val = val.replace('1', '!').replace('3', '!').replace('5', '!').replace('7', '!')
        if '**' not in val and '!!' not in val:
            count += 1


print(count)
# otvet: 208