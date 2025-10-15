from re import finditer

with open('24_18239.txt') as file:
    st = file.readline()

num = r'([1-9][0-9]*|[0])'
pattern = fr'{num}([-*]{num})+'
res = [str(i.group()) for i in finditer(pattern, st)]
res = [str(i) for i in res if eval(i) > -20_000]
res = [len(str(i)) for i in res]
print(res)
