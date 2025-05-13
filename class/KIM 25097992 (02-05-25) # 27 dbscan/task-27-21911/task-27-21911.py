from math import dist

def centroid(cluster):
    distance = []
    for dot in cluster:
        sum_dist = 0
        for dot2 in cluster:
            sum_dist += dist(dot, dot2)
        distance.append([sum_dist, dot])
    return min(distance)[1]

with open('27_A_21911.txt') as file:
    data = [list(map(float, i.replace(',', '.').split())) for i in file]

eps = 2
clusters = []
while data:
    cluster = [data.pop()]
    for dot in cluster:
        for dot2 in data.copy():
            if dist(dot, dot2) < eps:
                data.remove(dot2)
                cluster.append(dot2)
    clusters.append(cluster)
print([len(cluster) for cluster in clusters])

centers = [centroid(cluster) for cluster in clusters]
px = sum(center[0] for center in centers) / len(centers)
py = sum(center[1] for center in centers) / len(centers)

print(int(px * 10000), int(py * 10000))

# A) [50, 50] <- кластеры
# otvet: 26216 24182

# B) [3334, 3333, 3333] <- кластеры
# otvet: 150891 63754