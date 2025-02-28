def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            return False
    return True

count = 0
for i in range(600_001, 10 ** 20):
    if i % 6 == 0:
        if is_prime(i - 1) and is_prime(i + 1):
            print(i - 1, i + 1)
            count += 1
            if count == 6:
                break
# otvet:
# 600071 600073
# 600167 600169
# 600239 600241
# 600317 600319
# 600359 600361
# 600401 600403