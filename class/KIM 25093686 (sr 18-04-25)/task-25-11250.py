from fnmatch import fnmatch

for i in range(7058, 10 ** 8, 7058):
    if fnmatch(str(i), '392*4?4*'):
        print(i, i // 7058)

# otvet:
# 3924248 556
# 39214248 5556
# 39242480 5560