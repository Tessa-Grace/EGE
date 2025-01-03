from turtle import *

screensize(2000, 2000)
tracer(0)
m = 10
lt(90)

for i in range(2):
    fd(8 * m)
    rt(90)
    fd(18 * m)
    rt(90)
up()
fd(4 * m)
rt(90)
fd(10 * m)
lt(90)

down()
for i in range(2):
    fd(17 * m)
    rt(90)
    fd(7 * m)
    rt(90)

up()
for x in range(-20, 20):
    for y in range(-20, 25):
        goto(x * m, y * m)
        dot(3, 'red')
done()

# 8*18 + 9*19 + 5*8 = 355
# otvet: 355