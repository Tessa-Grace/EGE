from itertools import product

with open('task-24-7600.py') as file:
    data = file.readline()

data = data.replace('Q', '*').replace('R', '!').replace('S', '-')

for p in product('*!-', repeat=2):
    data = data.replace('**', '* *')

data = data.split()

print(len(max(data, key=len)))

# otvet: 9