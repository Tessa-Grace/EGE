from fnmatch import fnmatch

for i in range(6437, 10 **10, 6437):
    if fnmatch(str(i), '1?3*5*954'):
        print(i, i //6437)
# otvet:
# 1035339954 160842
# 1537425954 238842
# 1730535954 268842
# 1833527954 284842
# 1936519954 300842