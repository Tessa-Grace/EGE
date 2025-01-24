def f(A):
    for x in range(1, 10000):
        f = ((x % 12 == 0) <= (x % 42 != 0)) or ((x + A) >= 4096)
        if not f:
            return False
    return True

for A in range(1, 10000):
    if f(A):
        print(A)
        break

# otvet: 4012