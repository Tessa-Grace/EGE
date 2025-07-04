from math import dist

def centroid(cluster):
    dists = []
    for dot in cluster:
        sum_dists = 0
        for dot2 in cluster:
            sum_dists += dist(dot, dot2)
        dists.append([sum_dists, dot])
    return max(dists)[1]

with open('27.19.B_20497.txt') as file:
    data = [list(map(float, i.replace(',', '.').split())) for i in file]

clusters = []
eps = 4.5 # <- ищем мин расстояние от каждой возможной аномалии до точки из кластера
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

print(abs(int(px * 10_000)), abs(int(py * 10_000)))

# otvet:
# [286, 296, 302] <- кластеры eps 0.5
# A) 13258 2656
# [1985, 2132, 1915, 1948, 2004] <- кластеры eps = 4.5
# B) 209434 474989