from sys import setrecursionlimit
setrecursionlimit(10000)

def f(n):
    if n < 20:
        return n
    if n >= 20:
        return (n - 6) * f(n - 7)

print((f(47872) - 290 * f(47865)) / f(47858))

# otvet: 2276939784