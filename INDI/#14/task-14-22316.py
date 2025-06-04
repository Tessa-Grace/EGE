from string import printable
def convert(num, sys):
    r = ''
    while num:
        r += printable[num % sys]
        num //= sys
    return r[::-1]

ans = []
for x in range(33, 2034):
    num = convert(78**378 + 5**x - 7**61 - 5*x, 19)
    ans.append([num.count('7'), x])
print(max(ans))

# [79, 1888] <-  79-кол-во 7, а 1888-х
# otvet: 1888
