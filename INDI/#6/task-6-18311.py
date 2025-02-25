#18311

from turtle import *

tracer(0)
m = 10
lt(90)

for i in range(5):
    fd(15 * m)
    lt(90)
    fd(25 * m)
    lt(90)

up()
fd(4 * m)
lt(90)
fd(12 * m)
lt(90)

down()
for i in range(6):
    fd(38 * m)
    rt(90)
    fd(22 * m)
    rt(90)

up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * m, y * m)
        dot(3, 'white')
done()

#otvet: 34
