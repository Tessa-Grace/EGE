from sys import setrecursionlimit
setrecursionlimit(10000)

def f(n):
    if n == 1:
        return 1
    if n > 1:
        return n ** 3 + f(n - 1)

print(f(2025) - f(2022))

# otvet: 24874421616