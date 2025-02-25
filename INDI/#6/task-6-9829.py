#9829

from turtle import *

tracer(0)
m = 27

for i in range(3):
    rt(45)
    fd(10 * m)
    rt(45)

rt(315)
fd(10 * m)

for i in range(2):
    rt(90)
    fd(10 * m)

up()
for x in range(-20, 15):
    for y in range(-15, 10):
        goto(x * m, y * m)
        dot(3, 'red')
update()

#Otvet: 203