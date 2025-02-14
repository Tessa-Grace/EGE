from string import digits, ascii_uppercase

alph = digits + ascii_uppercase

def convert(num, sys):
    res = ''
    while num:
        res += alph[num % sys]
        num //= sys
    return res[::-1]

num = 3*15**1140 + 2*15**1025 + 15**923 + 3*15**85 + 2*15**74
num = convert(num, 15)
count = 0
maxx = 1
for i in range(len(num) - 1):
    num1, num2 = num[i:i+2]
    if num1 == num2:
        count += 1
        maxx = max(maxx, count)
    else:
        count = 0
print(maxx)

# otvet: 836

