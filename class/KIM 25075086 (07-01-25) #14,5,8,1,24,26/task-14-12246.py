#12246

num = 2*729**333 + 2*243**334 - 81**335 + 2*27**336 - 2*9**337 - 338
res = ''
while num:
    res += str(num % 9)
    num //= 9
res = res[::-1]
print(res.count('0'))

#otvet: 328 oshibka!!!