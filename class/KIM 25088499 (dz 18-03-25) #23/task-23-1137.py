from sys import setrecursionlimit
setrecursionlimit(100000)

def f(cur, fin):
    if cur == fin:
        return 1
    if int(cur, 2) > int(fin, 2):
        return 0
    return f(bin(int(cur, 2)+1)[2:], fin) + \
        f(cur + '0', fin) + \
        f(cur + '1', fin)

print(f('100', '11101'))

# otvet: 79