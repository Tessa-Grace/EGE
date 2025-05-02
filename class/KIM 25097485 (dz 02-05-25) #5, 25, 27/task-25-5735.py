#___________________________________________
#                 1 способ
#____________________________________________
def st2(n):
    return (n & (n - 1)) == 0 and n != 1

def dividers(num):
    res = set()
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0 :
            res |= {i, num // i}

    st_2 = [i for i in res if st2(i)]
    not_st_2 = [i for i in res if not st2(i)]
    if len(st_2) >= 20:
        return sum(not_st_2) if not_st_2 else 0
    return 0

count = 0
for num in range(10 ** 6 + 1, 10 ** 9):
    res = dividers(num)
    if res:
        print(num, res)
        count += 1
        if count == 5:
            break

# otvet:
# 3145728 3145725
# 5242880 5242875
# выводит не все, пропускает то, где res == 0

#__________________________________________
#             2 способ
#__________________________________________

def dividers(num):
    res = set()
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0 :
            res |= {i, num // i}

    st_2 = [2 ** i for i in range(2, 500)]
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
for num in range(10 ** 6 + 1, 10 ** 9):
    res = dividers(num)
    if res:
        print(num, res)
        count += 1
        if count == 5:
            break