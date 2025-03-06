from sys import setrecursionlimit
setrecursionlimit(10000)

def f(n):
    if n == 1:
        return 1
    if n > 1:
        return n + f(n - 1)

count = 0

for n in range(1, 101):
    x = f(2023) // f(n)
    if x % 2 == 0:
        count += 1
print(count)

# otvet: 50