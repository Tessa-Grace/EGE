def f(A):
    for x in range(90, 101):
        f = (x & 79 != 0) and ((x & 31 == 0) <= (x & A != 0))
        if not f:
            return False
    return True

for A in range(0, 1000):
    if f(A):
        print(A)
        break

# otvet: 32