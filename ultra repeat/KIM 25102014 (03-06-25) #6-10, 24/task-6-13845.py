#13845

from turtle import *

tracer(0)
m = 25
lt(90)
screensize(2000*2000)

up()
for i in range(10):
    rt(120)
    fd(10 * m)
    
down()
for i in range(7):
    fd(15 * m)
    rt(90)

for i in range(5):
    rt(60)
    fd(20 * m)
    rt(30)

up()
for x in range(-30, 20):
    for y in range(-30, 5):
        goto(x * m, y * m)
        dot(3, 'red')
update()

#Otvet: 74