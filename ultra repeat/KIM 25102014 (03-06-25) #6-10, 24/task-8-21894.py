from itertools import product

chet = '02468'
nechet = '13579'

count = 0
for val in product('0123456789', repeat=4):
    val = ''.join(val)
    if val[0] != '0' and len(val) == len(set(val)):
        for i in chet:
            val = val.replace(i, '*')
        for i in nechet:
            val = val.replace(i, '!')
        if '**' not in val and '!!' not in val:
            count += 1
print(count)

# otvet: 720