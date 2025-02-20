#17625

from turtle import *

tracer(0)
m = 10
lt(90)

for i in range(10):
    fd(22 * m)
    rt(90)
    fd(16 * m)
    rt(90)

up()
fd(1 * m)
rt(90)
fd(1 * m)
lt(90)

down()
for i in range(10):
    fd(72 * m)
    rt(90)
    fd(79 * m)
    rt(90)

up()
for x in range(-10, 30):
    for y in range(-10, 30):
        goto(x * m, y * m)
        dot(3, 'red')
update()

#Otvet: 72