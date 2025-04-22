from itertools import permutations

alph = 'ПАРИЖАНКА'

count = 0
for val in set(permutations(alph)):
    val = ''.join(val)

    for i in val:
        if i in 'АИ':
            val = val.replace(i, '!')

    ans = []
    for i in range(len(val) - 1):
        l1, l2 = val[i:i+2]
        if l1 == '!' and l2 == '!':
            ans.append(1)
    if sum(ans) == 1:
        count += 1

print(count)

# otvet: 28800