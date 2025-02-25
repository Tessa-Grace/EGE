def dividers(num):
    res = set()
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            res |= {i, num // i}
    res = sorted(res)
    for i in res:
        if str(i)[-1] == '8' and i != 8: # или первая проверка i % 10 == 8
            return i
    return 0

count = 0
for i in range(500001, 10 ** 20): # левая граница по условию, а правая по максимуму
    res = dividers(i)
    if res:
        print(i, res)
        count += 1
        if count == 5:
            break
# otvet:
# 500002 178
# 500004 18
# 500016 48
# 500018 58
# 500020 4348

