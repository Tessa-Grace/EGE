def f(A):
    for x in range(1, 1000):
        f = ((A % x == 0) <= (x == A) or (x == 1))
        if not f:
            return False
    return True

count = 0
for A in range(1, 11112):
    if f(A):
        count += 1
print(count)

# otvet: 1346