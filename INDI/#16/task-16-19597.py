def f(n):
    if n < 15:
        return 4
    if n % 3  == 0:
        return f(2 * n // 3) + n - 1
    return f(n - 1) + 3

for n in range(-1000, 1000):
    if f(n) == 251:
        print(n)

# otvet: 96