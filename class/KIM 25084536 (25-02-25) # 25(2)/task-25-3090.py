def is_prime(num): # функция проверки числа на простоту
    if num == 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def dividers(num):
    res = set()
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            res |= {i, num // i}
    res = sorted(res)

    P = [i for i in res if is_prime(i)]
    E = [i for i in res if i % 2 == 0]
    M = abs(sum(P) - sum(E))
    if len(P) == len(E):
        return M
    return 0

count = 0
for i in range(100_000_001, 10 ** 20):
    res = dividers(i)
    if res:
        print(i, res)
        count += 1
        if count == 5:
            break
# otvet:
# 100000034 50000017
# 100000042 50000021
# 100000094 50000047
# 100000118 50000059
# 100000126 50000063