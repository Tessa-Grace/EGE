def is_prime(num):
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
            if is_prime(num): res.add(i)
            if is_prime(num // i): res.add(num // i)
    res = sorted(res)

    if len(res) >= 1:
        s = sum(res)
        if s != 0 and s % 145 == 0:
            return s
    return 0

count = 0
for i in range(32_500_000, 10 ** 20):
    res = dividers(i)
    if res:
        print(i, res)
        count += 1
        if count == 7:
            break

# otvet: TO FINISH