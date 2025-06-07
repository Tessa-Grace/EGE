from re import finditer

with open('24_21908.txt') as file:
    st = file.readline()

pattern = r'[1-9ABCD][0-9ACBD]+[02468AC]'
res = [len(i.group()) for i in finditer(pattern, st)]
print(max(res))