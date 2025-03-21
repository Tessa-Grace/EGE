from itertools import product, repeat

count = 0
for val in product('0123456789AB', repeat=6):
    val = ''.join(val)
    if val[0] != '0' and val.count('B') == 1:
        val = val.replace('0', '*').replace('2', '*').replace('4', '*').replace('6', '*').replace('8', '*').replace('A', '*')
        val = val.replace('1', '!').replace('3', '!').replace('5', '!').replace('7', '!').replace('9', '!').replace('B','!')
        if val.count('*') == val.count('!'):
            count += 1
print(count)

# otvet: 297000