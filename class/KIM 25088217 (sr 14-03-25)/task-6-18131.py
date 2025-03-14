from turtle import *

tracer(0)
m = 10
lt(90)

for i in range(9):
    fd(22 * m)
    rt(90)
    fd(6 * m)
    rt(90)

up()
fd(1 * m)
rt(90)
fd(5 * m)
lt(90)

down()
for i in range(9):
    fd(53 * m)
    rt(90)
    fd(75 * m)
    rt(90)

up()
for x in range(-20, 20):
    for y in range(-20, 25):
        goto(x * m, y * m)
        dot(3, 'red')
done()

# 2 * 22 = 44

# otvet: 44