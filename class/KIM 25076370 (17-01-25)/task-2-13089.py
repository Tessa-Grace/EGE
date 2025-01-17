print('u w x y z')
for u in 0, 1:
    for w in 0, 1:
        for x in 0, 1:
            for y in 0, 1:
                for z in 0, 1:
                    f = ((z <= w) and (y == (not x))) <= (u == (y or z))
                    if not f:
                        print(u, w, x, y, z)
# u w x y z
# 0 0 0 1 0 |1
# 0 1 0 1 0 |2
# 0 1 0 1 1 |
# 0 1 1 0 1 |4
# 1 0 1 0 0 |3
# 1 1 1 0 0 |
# otvet: uywzx