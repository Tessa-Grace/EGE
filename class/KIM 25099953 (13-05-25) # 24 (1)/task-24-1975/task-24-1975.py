# Если в условии задания просят, чтобы какие-то символы не стояли рядом,
# то разделяем их по пробелам (при этом символы удалять нельзя)

with open('24_1975.txt') as file:
    data = file.readline()

while 'PP' in data:
    data = data.replace('PP', 'P P')

data = data.split()
print(len(max(data, key=len)))

# otvet: 188