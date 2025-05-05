from math import dist

def centroid(cluster):
    dists = []
    for dot in cluster:
        sum_dist = 0
        for dot2 in cluster:
            sum_dist += dist(dot, dot2)
        dists.append([sum_dist, dot])
    return min(dists)[1]

with open('27A_18623.txt') as file:
    data = [list(map(float, i.replace(',', '.').split())) for i in file]

clusters = []
eps = 1
while data:
    cluster = [data.pop()]
    for dot in cluster:
        for dot2 in data:
            if dist(dot, dot2) < eps:
                cluster.append(dot2)
                data.remove(dot2)
    clusters.append(cluster)
print([len(cluster) for cluster in clusters])

centers = [centroid(cluster) for cluster in clusters]
px = sum(center[0] for center in centers) / len(centers)
py = sum(center[1] for center in centers) / len(centers)

print(int(px * 100_000), int(py * 100_000))

# otvet:
# [250, 250] - кластеры
# 398800 348577
# [3333, 3333, 3333] - кластеры
# 596884 400991
