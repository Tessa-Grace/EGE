#13298

from itertools import product

alph = sorted('ПРИВЫЧКА')

arr = []
for i in product(alph, repeat=5):
    arr.append(''.join(i))

pos = 0
for i in range(len(arr)):
    if (i + 1) % 5 == 0:
        continue
    pos += 1
    for j in 'ИЫА':
        if j in arr[i]:
            break
    else:
        if len(arr[i]) == len(set(arr[i])):
            print(pos)
            break

# otvet: 4754