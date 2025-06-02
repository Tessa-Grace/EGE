with open('24_11813.txt') as file:
    data = file.readline()

gl = 'AEIOU'
sogl = 'BCDFGHJKLMNPQRSTVWXZ'

for i in gl:
    data = data.replace(i, '*')

for i in sogl:
    data = data.replace(i, '!')

data = data.replace('**', '* *')
data = data.replace('!!', '! !')

data = data.split()

print(len(max(data, key=len)))

# otvet: 25