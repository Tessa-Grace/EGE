from math import dist

def centroid(cluster):
    dists = []
    for dot in cluster:
        sum_dist = 0
        for dot2 in cluster:
            sum_dist += dist(dot, dot2)
        dists.append([sum_dist, dot])
    return min(dists)[1]

with open('27A_19747.txt') as file:
    clusterB1 = []
    clusterB2 = []
    clusterB3 = []
    for i in file:
        x, y = map(float, i.split())
        if 5 <= x <= 8 and 0 <= y <= 4.9:
            clusterB1.append([x, y])
        if 5 <= x <= 10 and 5 <= y <= 12:
            clusterB2.append([x, y])
        if 0 <= x <= 4.9 and 5 <= y <= 9:
            clusterB3.append([x, y])

centerB1 = centroid(clusterB1)
centerB2 = centroid(clusterB2)
centerB3 = centroid(clusterB3)

px = (centerB1[0] + centerB2[0] + centerB3[0]) / 3
py = (centerB1[1] + centerB2[1] + centerB3[1]) / 3


print(abs(int(px * 100_000)), abs(int(py * 100_000)))

# A) 532496 533164
# B) ne znayu :(
