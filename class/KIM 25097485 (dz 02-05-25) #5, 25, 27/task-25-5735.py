def dividers(num):
    res = set()
    st_2 = [i ** 2 for i in range(500)]
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0 :
            res |= {i, num // i}

    sp_st_2 = []
    not_st_2 = []
    if len(res) > 20:
        for i in res:
            if i in st_2: sp_st_2.append(i)
            if i not in st_2: not_st_2.append(i)
        if len(sp_st_2) >= 20:
            return sum(not_st_2)
    return 0

count = 0
for num in range(10 ** 6, 10 ** 20):
    res = dividers(num)
    if res:
        print(num, res)
        count += 1
        if count == 5:
            break

# otvet: