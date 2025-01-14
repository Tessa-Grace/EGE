print('w x y z')
for w in range(2):
    for x in 0, 1:
        for y in [0, 1]:
            for z in (0, 1):
                f = not(w <= z)or (x <= y) or not x
                if not f:
                    print(w, x, y, z)

# w x y z
# 0 1 0 0
# 0 1 0 1
# 1 1 0 1
# otvet: wzyx