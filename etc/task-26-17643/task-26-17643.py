with open('26_17643.txt') as file:
    N = file.readline()
    goods = {}
    midd = 0
    length = 0
    for i in file:
        art, price, stat = map(int, i.split())
        midd += price
        length += 1
            if art not in goods:
                goods[art] = [price, 0, 0]
            if stat:
                goods[art][1] += 1
            else:
                goods[art][2] += 1

midd /= length
goods2 = []
for art, info in goods.items():
    if info[0] > midd:
        goods2.append([art, goods[art], True])
    else:
        goods2.append([art, goods[art], False])

goods = sorted(goods2, key=lambda x: (-x[4], -x[3], -x[1], -x[2]))
print(goods[0], goods[0][1] * goods[0][3])

# NOT FINISHED
