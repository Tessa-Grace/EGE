from math import dist

def centroid(cluster):
    dists = []
    for dot in cluster:
        sum_dist = 0
        for dot2 in cluster:
            sum_dist += dist(dot, dot2)
        dists.append([sum_dist, len(cluster), dot])
    return min(dists)


with open('27_B_21932.txt') as file:
    data = [list(map(float, i.split())) for i in file]

clusters = []
eps = 1
while data:
    cluster = [data.pop()]
    for dot in cluster:
        for dot2 in data.copy():
            if dist(dot, dot2) < eps:
                cluster.append(dot2)
                data.remove(dot2)
    clusters.append(cluster)
print([len(cluster) for cluster in clusters])

centers = [centroid(cluster) for cluster in clusters]
min_x = min([center for center in centers], key=lambda x: x[1])[2][0]
max_y = max([center for center in centers], key=lambda x: x[1])[2][1]

print(int(min_x * 10_000), int(max_y * 10_000))


# A) [137, 100] <- кластеры
# otvet: 32865 70666

# B) [102, 439, 98] <- кластеры
# otvet: 144062 61170