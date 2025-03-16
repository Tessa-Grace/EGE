from sys import setrecursionlimit
setrecursionlimit(100000)

def f(cur, fin):
    if cur == fin:
        return 1
    if cur > fin:
        return 0
    return f(cur + 1, fin) + \
        f(int(str(cur) + '0'), fin) + \
        f(int(str(cur) + '1'), fin)

print(f(100, 11101))

# otvet: 4687 MISTAKE