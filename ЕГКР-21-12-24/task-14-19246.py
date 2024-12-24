from string import digits,ascii_lowercase

alph = digits + ascii_lowercase

def convert(num, sys):
    r = ''
    while num:
        r += alph[num % sys]
        num //= sys
    return r[::-1]

ans = []
for x in alph[:25]:
    num1 = '11353' + x + '12'
    num2 = '135'+ x + '21'
    num = int(num1, 25) + int(num2, 25)
    if num %  24 == 0:
        res = num // 24
        ans.append(res)
print(max(ans))