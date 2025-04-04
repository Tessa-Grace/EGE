from fnmatch import fnmatch

for i in range(2023, 10 ** 9, 2023):
    if fnmatch(str(i), '20*23'):
        summ = sum(map(int, str(i)))
        if summ % 7 == 0 and summ < 20:
            print(i)
# otvet:
# 2023
# 204323
# 2025023
# 20232023
# 202302023