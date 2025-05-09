from math import dist

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

with open('27.13.A_19567.txt') as file:
    cluster1 = []
    cluster2 = []
    for i in file:
        x, y = map(float, i.split())
        if y < 0:
            cluster1.append([x, y])
        else:
            cluster2.append([x, y])

center1 = centroid(cluster1)
center2 = centroid(cluster2)

ans_x = (center1[0] + center2[0]) / 2
ans_y = (center1[1] + center2[1]) / 2

print('A)', abs(int(ans_x * 10_000)), abs(int(ans_y * 10_000)))

#________________________________________________
#                    Chapter B
#________________________________________________

with open('27.13.B_19567.txt') as file:
    clusterB1 = []
    clusterB2 = []
    clusterB3 = []
    clusterB4 = []
    clusterB5 = []
    clusterB6 = []
    for i in file:
        x, y = map(float, i.split())
        if y > x + 12:
            clusterB1.append([x, y])
        if y > 7 and y < x + 12 and y > x + 4:
            clusterB2.append([x, y])
        if y < x + 4 and y > 4:
            clusterB3.append([x, y])
        if y < 7 and y > x + 4 and y < x + 12:
            clusterB4.append([x, y])
        if y < 4 and y < x + 4 and y > x - 2:
            clusterB5.append([x, y])
        if y < 4 and y < x - 2:
            clusterB6.append([x, y])

centerB1 = centroid(clusterB1)
centerB2 = centroid(clusterB2)
centerB3 = centroid(clusterB3)
centerB4 = centroid(clusterB4)
centerB5 = centroid(clusterB5)
centerB6 = centroid(clusterB6)

ans_x = (centerB1[0] + centerB2[0] + centerB3[0]+ centerB4[0] + centerB5[0] + centerB6[0]) / 6
ans_y = (centerB1[1] + centerB2[1] + centerB3[1]+ centerB4[1] + centerB5[1] + centerB6[1]) / 6

print('B)', abs(int(ans_x * 10_000)), abs(int(ans_y * 10_000)))

# otvet:
# A) 10770 8264
# B) 3785 46909