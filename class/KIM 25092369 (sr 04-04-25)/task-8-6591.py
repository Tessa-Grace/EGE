from itertools import product

alph = '0123456'


count = 0
for val in product(alph, repeat=5):
    val = ''.join(val)
    if val[0] != '0' and val.count('6') == 1:
        chet = []
        nechet = []
        for i in val:
            if int(i) % 2 == 0:
                chet.append(i)
            else:
                nechet.append(i)
        if sum(map(int, chet)) < sum(map(int, nechet)):
            count += 1
print(count)

# otvet: 1390
