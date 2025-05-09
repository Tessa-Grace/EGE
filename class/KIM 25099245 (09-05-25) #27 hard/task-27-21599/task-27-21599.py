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

with open('27_A_21599.txt') as file:
    cluster1 = []
    cluster2 = []
    cluster3 = []
    for i in file:
        x, y = map(float, i.split())
        if y < -5:
            cluster1.append([x, y])
        elif y > x - 10:
            cluster2.append([x, y])
        else:
            cluster3.append([x, y])

center1 = centroid(cluster1)
center2 = centroid(cluster2)
center3 = centroid(cluster3)

ans_x = (center1[0] + center2[0] + center3[0]) / 3
ans_y = (center1[1] + center2[1] + center3[1]) / 3

print('A)', abs(int(ans_x * 10_000)), abs(int(ans_y * 10_000)))

#________________________________________________
#                    Chapter B
#________________________________________________

with open('27_B_21599.txt') as file:
    clusterB1 = []
    clusterB2 = []
    clusterB3 = []
    clusterB4 = []
    clusterB5 = []
    clusterB6 = []
    for i in file:
        x, y = map(float, i.split())
        if y < -2 * x - 26:
            clusterB1.append([x, y])
        if y > -2 * x - 26 and x < -10:
            clusterB2.append([x, y])
        if x > -10 and y > 2 * x + 12:
            clusterB3.append([x, y])
        if y < 2 * x + 12 and y > 3/4 * x:
            clusterB4.append([x, y])
        if y < 3/4 * x and y > -5:
            clusterB5.append([x, y])
        if y < -5:
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
# A) 178755 2896
# B) 37392 50998