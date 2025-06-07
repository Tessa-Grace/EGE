from re import finditer

with open('24_17878.txt') as file:
    st = file.readline()

num = r'([1-9][0-9]*|[0])'
pattern = fr'{num}([-*]{num})+'
res = [len(i.group()) for i in finditer(pattern, st)]
print(max(res))