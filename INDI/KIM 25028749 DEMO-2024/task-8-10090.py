from itertools import product

count = 0
for val in product('01234567', repeat=8):
    val = ''.join(val)
    if val[0] != '0' and val[0] != val[1] != val[2] != val[3] != val[4] != val[5]:
        val = val.replace('0', '*').replace('2', '*').replace('4', '*').replace('6', '*')
        val = val.replace('1', '!').replace('3', '!').replace('5', '!').replace('7', '!')
        if '**!!' not in val and '!!**' not in val:
            count += 1
print(count)

# otvet: 4264624