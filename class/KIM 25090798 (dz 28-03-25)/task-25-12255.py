from fnmatch import fnmatch

for i in range(98591, 10**12, 98591):
    if fnmatch(str(i), '12?3*456??9'):
        print(i, i // 98591)

# otvet:
# 120313456439 1220329
# 120383456049 1221039
# 125351456539 1271429
