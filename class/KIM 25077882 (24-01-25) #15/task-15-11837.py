def f(A):
    for x in range(0, 1000):
        for y in range(0, 1000):
            f = ((x**2 + y**2) > 1024 - x) or (y < ((-2) * x ) + A)
            if not f:
                return False
    return True


for A in range(0, 1000):
    if f(A):
        print(A)
        break

# otvet: 71