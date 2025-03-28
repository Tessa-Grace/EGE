def dividers(num):
    res = set()
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            res |= {i, num // i}

    res = sorted(res)
    if len(res) > 2:
        s = res[-1] + res[-2] + res[-3]
        if s % 2022 == 0 and s != num:
            return s
    return 0
count = 0
for i in range(1, 1_200_001)[::-1]:
    res = dividers(i)
    if res:
        print(i, res)
        count += 1
        if count == 5:
            break
# otvet:
# 1089858 1089858
# 1091880 1182870 +
# 1093902 1093902
# 1097946 1097946
# 1106034 1106034
# 1110078 1110078
# 1114122 1114122
# 1116144 1209156 +
# 1118166 1118166
# 1126254 1126254
# 1130298 1130298
# 1134342 1134342
# 1138386 1138386
# 1140408 1235442 +
# 1146474 1146474
# 1150518 1150518
# 1154562 1154562
# 1158606 1158606
# 1164672 1261728 +
# 1166694 1166694
# 1170738 1170738
# 1174782 1174782
# 1178826 1178826
# 1186914 1186914
# 1188936 1288014 +
# 1190958 1190958
# 1195002 1195002
# 1199046 1199046