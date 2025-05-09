from fnmatch import fnmatch

for i in range(2023, 10 ** 10, 2023):
    if fnmatch(str(i), '1?1?1?1*1'):
        if sum(map(int, str(i))) == 22:
            print(i)

# otvet:
# 19131511
# 1012141291
# 1319111311
# 1516111051