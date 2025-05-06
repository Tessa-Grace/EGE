#______________A part

import turtle as t

def dist(dot1, dot2):
    return max(abs(dot1[0]- dot2[0]), abs(dot1[1] - dot2[1]))

def centroid(cluster):
    dists = []
    for dot in cluster:
        sum_dists = 0
        for dot2 in cluster:
            sum_dists += dist(dot, dot2)
        dists.append([sum_dists, dot])
    return min(dists)[1]

with open('27.3.A_19891.txt') as file:
    cluster_A1 = []
    cluster_A2 = []
    for i in file:
        x, y = map(float, i.split())
        if x < 3:
            cluster_A1.append([x, y])
        else:
            cluster_A2.append([x, y])

# t.tracer(0)
# m = 50
# t.up()
# colors = ['red', 'blue']
# clusters = [cluster_A1, cluster_A2]
# for cluster, color inzip(clusters, colors):
#     for dot in cluster:
#         t.goto(dot[0] * m, dot[1] * m)
#         t.dot(3, color)
# t.update()
# t.done()

centers= [centroid(cluster) for cluster in [cluster_A1, cluster_A2]]
px = sum(center[0] for center in centers) / len(centers)
py = sum(center[1] for center in centers) / len(centers)

print('A)', int(px * 10000), int(py * 10000))

#_______________B PART
with open('27.3.B_19891.txt') as file:
    cluster_A1 = []
    cluster_A2 = []
    cluster_A3 = []
    cluster_A4 = []
    for i in file:
        x, y = map(float, i.split())
        if y < -2: cluster_A1.append([x, y])
        elif x < 1: cluster_A2.append([x, y])
        elif y < 2: cluster_A3.append([x, y])
        else: cluster_A4.append([x, y])

centers = [centroid(cluster) for cluster in [cluster_A1, cluster_A2, cluster_A3, cluster_A4]]
px = sum(center[0] for center in centers) / len(centers)
py = sum(center[1] for center in centers) / len(centers)

print('B)', int(px * 10000), int(py * 10000))
#otvet
# A) 31889 4751
# B) 23102 4049