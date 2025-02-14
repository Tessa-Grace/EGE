from itertools import product, repeat

alph = '0123456789'

count = 0
for val in product(alph, repeat=6):
    val = ''.join(val)
    if val[0] != '0' and int(val) % 4 == 0:
        cnt = sum(val.count(i) for i in val)
        if cnt == 6:
            for i in val:
                val = val.replace('0', '*').replace('2', '*').replace('4', '*').replace('6', '*').replace('8', '*')
            if '**' not in val:
                count += 1
print(count)

# otvet: 7440