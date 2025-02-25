#4828

k = 0
for x in range(200):
    for y in range(20):
        if y<3*x and 0<y<15 and y>(x-56)/4:
            k += 1
print(k)

#Otvet: 1160
