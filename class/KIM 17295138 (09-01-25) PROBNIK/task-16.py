from sys import setrecursionlimit
setrecursionlimit(10000)

def f(n):
    if n <= 6:
        return n
    if n > 6:
        return 2 * n + 3 + f(n - 1)
print(f(6188) - f(6185))

# otvet: 37131