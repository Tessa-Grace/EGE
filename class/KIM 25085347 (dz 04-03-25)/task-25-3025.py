def dividers(num):
    res = set()
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:    # проверка: является ли i делителем
            if i % 2 != 0:  # проверка i на нечетность
                res |= {i}
            if num // i % 2 != 0: # проверка результата деления num на i на нечетность
                res |= {num // i}

    res = sorted(res)
    if len(res) > 5:
        d = list(res)[-6]
        return d
    return 0

count = 0
for i in range(200_000_000, 10 ** 20):
    res = dividers(i)
    if res:
        print(i, res)
        count += 1
        if count == 5:
            break

# otvet:
# 200000000 125
# 200000003 48391
# 200000004 42123
# 200000005 5
# 200000008 5101