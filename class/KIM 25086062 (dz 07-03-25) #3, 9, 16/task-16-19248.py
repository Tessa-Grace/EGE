from sys import setrecursionlimit
setrecursionlimit(10000)

def f(n):
    if n < 5:
        return n
    if n >= 5:
        return 2 * n * f(n - 4)

print((f(13766) - 9 * f(13762)) // f(13758))

# otvet: 757543052