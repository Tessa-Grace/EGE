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
    clusterA1 = []
    clusterA2 = []
    clusterA3 = []
    for i in file:
        x, y = map(float, i.split())
        if 5 <= x <= 8 and 0 <= y <= 4.9:
            clusterA1.append([x, y])
        if 5 <= x <= 10 and 5 <= y <= 12:
            clusterA2.append([x, y])
        if 0 <= x <= 4.9 and 5 <= y <= 9:
            clusterA3.append([x, y])

centerA1 = centroid(clusterA1)
centerA2 = centroid(clusterA2)
centerA3 = centroid(clusterA3)

px = (centerA1[0] + centerA2[0] + centerA3[0]) / 3
py = (centerA1[1] + centerA2[1] + centerA3[1]) / 3


print(abs(int(px * 100_000)), abs(int(py * 100_000)))
#______________________________
with open('27B_19747.txt') as file:
    clusterB1 = []
    clusterB2 = []
    clusterB3 = []
    clusterB4 = []
    clusterB5 = []
    for i in file:
        x, y = map(float, i.split())
        if x < 10 and y < x:
            clusterB1.append([x, y])
        if x < 10 and y > x:
            clusterB2.append([x, y])
        if x > 10 and y < 10:
            clusterB3.append([x, y])
        if x > 10 and y < 10:
            clusterB4.append([x, y])
        else:
            clusterB5.append([x, y])

centerB1 = centroid(clusterB1)
centerB2 = centroid(clusterB2)
centerB3 = centroid(clusterB3)
centerB4 = centroid(clusterB2)
centerB5 = centroid(clusterB3)

px = (centerB1[0] + centerB2[0] + centerB3[0] + centerB4[0] + centerB5[0]) / 5
py = (centerB1[1] + centerB2[1] + centerB3[1] + centerB4[1] + centerB5[1]) / 5


print(abs(int(px * 100_000)), abs(int(py * 100_000)))

# A) 532496 533164
# B) ne znayu :(


#
# from math import dist
#
# def centroid(cluster):
#     dists = []
#     for dot in cluster:
#         sum_dist = 0
#         for dot2 in cluster:
#             sum_dist += dist(dot, dot2)
#         dists.append([sum_dist, dot])
#     return min(dists)[1]
#
# with open('27B_19747.txt') as file:
#     clusterB1 = []
#     clusterB2 = []
#     clusterB3 = []
#     clusterB4 = []
#     clusterB5 = []
#     for i in file:
#         x, y = map(float, i.split())
#         if x < 10 and y < x:
#             clusterB1.append([x, y])
#         elif x < 10 and y > x:
#             clusterB2.append([x, y])
#         elif x > 10 and y < 10:
#             clusterB3.append([x, y])
#         elif x > 10 and y > 10 and y < x:
#             clusterB4.append([x, y])
#         else:
#             clusterB5.append([x, y])
#
#
# centerB1 = centroid(clusterB1)
# centerB2 = centroid(clusterB2)
# centerB3 = centroid(clusterB3)
# centerB4 = centroid(clusterB4)
# centerB5 = centroid(clusterB5)
#
# px = (centerB1[0] + centerB2[0] + centerB3[0] + centerB4[0] + centerB5[0]) / 5
# py = (centerB1[1] + centerB2[1] + centerB3[1] + centerB4[1] + centerB5[1]) / 5
#
#
# print(abs(int(px * 100_000)), abs(int(py * 100_000)))
#
# # A) 532496 533164
# # B) ne znayu :(

