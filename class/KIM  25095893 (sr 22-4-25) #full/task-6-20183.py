from turtle import *
tracer(0)
lt(90)
m = 10

for i in range(7):
    fd(9 * m)
    rt(90)
    fd(16 * m)
    rt(90)

up()
fd(3 * m)
rt(90)
fd(4 * m)
lt(90)

down()
for i in range(4):
    fd(7 * m)
    rt(90)
    fd(13 * m)
    rt(90)

up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * m, y * m)
        dot(3, 'white')
done()

# otvet: 6 * 12 = 72
