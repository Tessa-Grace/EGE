from math import dist # сразу формула евклидова расстояния

#________________________________________________
#                    Chapter А
#________________________________________________
def centroid(cluster):
    distance = []
    for dot in cluster:
        sum_dist = 0
        for dot2 in cluster:
            sum_dist += dist(dot, dot2)
        distance.append([sum_dist, dot])
    return min(distance)[1]

with open('27_A_17882.txt') as file:
    cluster1 = []
    cluster2 = []
    for i in file:
        x, y = map(float, i.split())
        if x < 1:
            cluster1.append([x, y])
        else:
            cluster2.append([x, y])

center1 = centroid(cluster1)
center2 = centroid(cluster2)

ans_x = (center1[0] + center2[0]) / 2 # ищем среднее арифметическое
ans_y = (center1[1] + center2[1]) / 2

print('A)', int(ans_x * 10_000), int(ans_y * 10_000))

# otvet: 10738 10738

#________________________________________________
#                    Chapter B
#________________________________________________

with open('27_B_17882.txt') as file:
    clusterB1 = []
    clusterB2 = []
    clusterB3 = []
    for i in file:
        x, y = map(float, i.split())
        if y < 4:
            clusterB1.append([x, y])
        elif 4 <= y <= 6.5: # x < 5
            clusterB2.append([x, y])
        else:
            clusterB3.append([x, y])

centerB1 = centroid(clusterB1)
centerB2 = centroid(clusterB2)
centerB3 = centroid(clusterB3)

ans_Bx = (centerB1[0] + centerB2[0] + centerB3[0]) / 3 # ищем среднее арифметическое
ans_By = (centerB1[1] + centerB2[1] + centerB3[1]) / 3

print('B)', int(ans_Bx * 10_000), int(ans_By * 10_000))