with open('26_3586.txt') as file:
    N = int(file.readline())
    trees = [list(map(int, i.split())) for i in file]

trees = sorted(trees, key=lambda x: (-x[0], x[1])) # ставим минус по убыванию первого элемента, и по возрастанию второго

length = []
for tree1, tree2 in zip(trees, trees[1:]):
    if tree1[0] == tree2[0]:
        length.append([tree2[1] - tree1[1] - 1, tree1[0]])

print(max(length))

# [7468, 4802], но записать надо наоборот, тк иначе макс искался бы не ряду, а не кол-ву мест свободных
# otvet: [4802, 7468]