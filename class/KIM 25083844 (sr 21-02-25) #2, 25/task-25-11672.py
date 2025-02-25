from fnmatch import fnmatch

for i in range(21025, 10 ** 10, 21015):
    if fnmatch(str(i), '12*34?5'):
        line = str(i)
        for j in line:
            line = line.replace('0', '*').replace('2', '*').replace('4', '*').replace('6', '*').replace('8', '*')
            line = line.replace('1', '!').replace('3', '!').replace('5', '!').replace('7', '!').replace('9', '!')
        if i % 21025 == 0 and line.count('*') == line.count('!'):
            print(i, i // 21025)
