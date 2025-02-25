#13841

from turtle import *

tracer(0)
m = 23
lt(90)

down()
fd(10 * m)
for i in range(4):
    rt(180)
    circle(2*m, -180)
bk(10*m)
for i in range(4):
    circle(2*m, -180)
    rt(180)

up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * m, y * m)
        dot(3, 'red')
update()

#Otvet: 183