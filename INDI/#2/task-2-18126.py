# 18126

print('w x y z')
for w in 0, 1:
    for x in 0, 1:
        for y in 0, 1:
            for z in 0, 1:
                F = ((z == x) <= w) and (w <= (y and x))
                if F == 1:
                    print(w, x, y, z)

# otvet: yzxw