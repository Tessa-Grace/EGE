from math import dist

def centroid(cluster):
    dists = []
    for dot in cluster:
        sum_dists = 0
        for dot2 in cluster:
            sum_dists += dist(dot, dot2)
        dists.append([sum_dists, dot])
    return min(dists)[1]

with open('27B_18056.txt') as file:
    data = [list(map(float, i.replace(',', '.').split())) for i in file]

clusters = []
eps = 0.4
while data:
    cluster = [data.pop()]
    for dot in cluster:
        for dot2 in data.copy():
            if dist(dot, dot2) < eps:
                cluster.append(dot2)
                data.remove(dot2)
    if len(cluster) > 10:
        clusters.append(cluster)
print([len(cluster) for cluster in clusters])

centers = [centroid(cluster) for cluster in clusters]
px = sum(center[0] for center in centers) / len(centers)
py = sum(center[1] for center in centers) / len(centers)

print(abs(int(px * 100_000)), abs(int(py * 100_000)))

# otvet:
# [47, 43] <- кластеры
# 43744 47901
# [3330, 3328, 3329] <- кластеры
# 99895 100091
