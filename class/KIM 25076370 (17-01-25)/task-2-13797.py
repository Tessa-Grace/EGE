print('w x y z')
for w in 0, 1:
    for x in 0, 1:
        for y in 0, 1:
            for z in 0, 1:
                f = (not x and(z <= y) and not w) or ((z == w) and ((x or y) <= w))
                if f:
                    print(w, x, y, z)

# w x y z
# 0 0 1 0 +
# 0 0 1 1
# 1 0 0 1
# 1 0 1 1
# 1 1 0 1
# otvet: ywxz