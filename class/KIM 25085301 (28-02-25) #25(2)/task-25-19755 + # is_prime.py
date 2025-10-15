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
            if is_prime(i) and is_prime(num // i) and \
                    str(i).count('0') == 1 and str(num // i).count('0') == 1:
                res.add(i)
                res.add(num // i)
    return res

count = 0
for i in range(2_900_001, 10 ** 20):
    res = dividers(i)
    if len(res) == 2:
        print(i, max(res))
        count += 1
        if count == 5:
            break
# otvet:
# 2900021 27103
# 2900449 27107
# 2900519 4091
# 2900663 27109
# 2901809 5701
