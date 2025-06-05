from sys import setrecursionlimit
setrecursionlimit(10000)

def f(n):
    if 1 <= n < 13:
        return 13
    if n >= 13 and n % 5 != 0:
        return 13 - f(n - 1)
    if n >= 13 and n % 5 == 0:
        return 13 + f(n - 1)

print(f(3013))

# otvet: -7800