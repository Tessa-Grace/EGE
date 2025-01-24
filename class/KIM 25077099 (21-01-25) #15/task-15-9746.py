def f(A):
    for x in range(0, 1000):
        for y in range(0, 1000):
            f = (x < A) or (y < A) or (x + 2 * y > 50)
            if not f:
                return False
    return True

for A in range(0, 1000):
    if f(A):
        print(A)
        break

# otvet: 17