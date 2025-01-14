print('a b c d')
for a in 0, 1:
    for b in 0, 1:
        for c in 0, 1:
            for d in 0, 1:
                f = (not a and not b) or (b == c) or d
                if f == 0:
                    print(a, b, c, d)
# a b c d
# 0 1 0 0
# 1 0 1 0
# 1 1 0 0
#otvet: cdba