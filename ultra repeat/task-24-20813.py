from re import finditer

with open('txt/24_20813.txt') as file:
    st = file.readline()

num = r'([1-9][0-9]*|[0])'
pattern = fr'{num}([-*]{num})+'
res = [len(i.group()) for i in finditer(pattern, st)]
print(max(res))