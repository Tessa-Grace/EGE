#8150

from turtle import *

tracer(0)
m = 15
lt(90)

for i in range(2):
    fd(5 * m)
    rt(90)
    fd(15 * m)
    rt(90)
    
up()
fd((-7) * m)
rt(90)
fd(12 * m)
lt(90)

down()
for i in range(2):
    fd(65 * m)
    rt(90)
    fd(120 * m)
    rt(90)

up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * m, y * m)
        dot(3, 'white')
update()

#Otvet: 16