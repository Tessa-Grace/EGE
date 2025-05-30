with open('26_4205.txt') as file:
    N = int(file.readline())
    trees = [list(map(int, i.split())) for i in file] # поступаем всегда так, когда в строке несколько чисел разбитых пробелом
    #в лист оборачиваем, тк map выдает неудобный тип данных

trees = sorted(trees, key=lambda x: (-x[0], x[1])) # ставим минус по убыванию первого элемента, и по возрастанию второго
for i in range(N - 1):
    tree1, tree2 = trees[i:i+2]
    if tree1[0] == tree2[0]:
        if tree2[1] - tree1[1] -1 == 13:
            print(tree1[0], tree1[1] + 1)
            break

# otvet: 59966 50449