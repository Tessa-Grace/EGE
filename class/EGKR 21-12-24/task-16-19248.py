from sys import setrecursionlimit
setrecursionlimit(10000)

def F(n):
    if n < 5:
        return n
    if n >= 5:
        return 2 * n * F(n - 4)
print((F(13766) - 9 * F(13762))/F(13758))

# otvet: 757543052