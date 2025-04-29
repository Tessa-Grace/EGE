from fnmatch import fnmatch

for i in range(86513, 10 ** 12, 86513):
     if fnmatch(str(i), '17*46??8'):
         if sum(map(int, str(i))) ** .5 % 1 == 0: # sum(map(int, str(i))) ** .5 == int(sum(map(int, str(i))) ** .5)
# sqrt(sum(map(int, str(i)))) == isqrt(sum(map(int, str(i))))
            print(i, i // 86513)
# otvet:
# 170083346818 1965986
# 173010946738 1999826
# 175769846308 2031716
# 177402346618 2050586
# 177965546248 2057096
# 178697446228 2065556