# data = '5467+++8**867568976*+++0098765658'
# не подходят:
# ++
# **
# +*
# *+

with open('24-1.txt') as file:
    data = file.readline()

data = data.replace('++', ' ').replace('**', ' ')
data = data.replace('+*', ' ').replace('*+', ' ')

# если есть незначащие нули
for i in '0123456789':
    data = data.replace(f'+0{i}', f'+0 {i}')
    data = data.replace(f'*0{i}', f'*0 {i}')
    data = data.replace(f' 0{i}', f' 0 {i}')

data = data.split()
ans = 0
for i in data:
    st = i.strip('+').strip('*')
    if eval(st) == 0:
        ans = max(ans, len(st))

print(ans)

# otvet: 104
