def is_prime(num): # определение простого числа
    if num < 2:
        return False
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            return False
    return True

def dividers(num):
    res = set()
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            if is_prime(i): res.add(i)
            if is_prime(num // i): res.add(num // i)

            # 30 -> [2, 3, 5]
            #       [15, 10, 6]
    res = sorted(res)
    if len(res) > 1:
        m = min(res) + max(res)
        if m > 2000 and m % 10 == 8:
            return m
    return 0

count = 0
for i in range(1_200_001, 10 ** 20):
    res = dividers(i)
    if res:
        print(i, res)
        count += 1
        if count == 5:
            break
# otvet:
# 1200005 2248
# 1200011 2388
# 1200037 17978
# 1200067 109108
# 1200197 2598
