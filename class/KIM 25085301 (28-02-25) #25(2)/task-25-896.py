def is_prime(num):
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            return False
    return True

pos = 0
for i in range(194441, 196501):
    if is_prime(i) and i % 100 == 93:
        pos += 1
        print(pos, i)
# otvet:
# 1 195193
# 2 195493
# 3 195593
# 4 195893
# 5 196193