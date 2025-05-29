from re import *
with open('24_21421.txt') as f:
    st = f.readline()

pattern  = r'[1-9AB][0-9AB]*[02468A]'
m = [i.group() for i in finditer(pattern, st)]
print(len(max(m, key=len)))

# otvet: 19