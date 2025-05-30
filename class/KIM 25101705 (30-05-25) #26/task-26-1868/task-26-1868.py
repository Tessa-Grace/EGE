with open('26_1868.txt') as file:
    N = int(file.readline())
    places = [list(map(int, i.split())) for i in file]

places = sorted(places, key=lambda x: (-x[0], x[1]))

length = []
for place1, place2 in zip(places, places[1:]):
    if place1[0] == place2[0]:
        if place2[1] - place1[1] - 1 == 2:
            print(place1[0], place1[1] + 1)
            break
# подлянка от автора - надо в txt удалить две последних строки, тк пустые

# otvet: 8631 7311