def dividers(num):
    res = set()
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            res |= {i, num // i}
    res = sorted(res)

    if len(res) >= 2:
        M = min(res) + max(res)
        if M % 10 == 4:
            return M
    return 0

count = 0
for i in range(800_001, 10 ** 20):
    res = dividers(i)
    if res:
        print(i, res)
        count += 1
        if count == 5:
            break

# otvet:
# 800004 400004
# 800009 114294
# 800013 266674
# 800024 400014
# 800033 61554