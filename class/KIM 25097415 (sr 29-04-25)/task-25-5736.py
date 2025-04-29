def dividers(num):
    res = set()
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            res |= {i, num // i}
    res = sorted(res)
    if res:
        if res[-1] % 7 == 0:
            return res[-1]
    return False

count = 0
for i in range(10 ** 9, 10 ** 20):
    if str(i) == str(i)[::-1]:
        res = dividers(i)
        if res:
            print(i, res)
            count += 1
            if count == 5:
                break

# otvet:
# 1001771001 333923667
# 1002002001 334000667
# 1003003001 143286143
# 1004774001 334924667
# 1005005001 335001667