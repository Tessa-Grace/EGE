from sys import setrecursionlimit
setrecursionlimit(10000)

def f(n):
    if n <= 11:
        return n
    if n >= 11 and n % 2 == 0:
        return 2 * n - 3 + f(n - 2)
    if n >= 11 and n % 2 != 0:
        return 3 * n - 4 + f(n - 3)

print(f(5500) - f(5497))

# otvet: 16492