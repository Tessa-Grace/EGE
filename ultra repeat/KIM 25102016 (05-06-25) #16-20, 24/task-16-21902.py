from sys import setrecursionlimit
setrecursionlimit(10000)

def f(n):
    if n >= 2025:
        return n
    if n < 2025:
        return n * 2 + f(n + 2)

print(f(82) - f(81))

# otvet: 1945