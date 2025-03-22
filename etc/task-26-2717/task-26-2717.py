from itertools import groupby

with open('26_2717.txt') as file:
    N = file.readline()
    data = [list(map(int, i.split())) for i in file]

data = sorted(data)
for row, places in groupby(data, key=lambda x: x[0]):
    places = list(places)
    if len(places) >= 5:
        for i in range(len(places) - 4):
            places_5 = places[i:i + 5]
            if places_5[-1][1] - places_5[0][1] <= 12:
                for j in range(4):
                    if places_5[j + 1][1] - places_5[j][1] > 3:
                        break
                else:
                    print(places_5)
# otvet: [1234, 38468]

