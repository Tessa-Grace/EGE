from turtle import *

tracer(0)
m = 10
lt(90)

for i in range(4):
    fd(3 * m)
    lt(270)
    fd(5 * m)
    rt(90)

lt(270)

for i in range(3):
    fd(5 * m)
    rt(90)
    fd(3 * m)
    lt(270)

up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * m, y * m)
        dot(3, 'red')
done()

# 6 * 7 = 42
# otvet: 42