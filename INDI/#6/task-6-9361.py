from turtle import *

screensize(2000,2000)
tracer(0)
m = 50
lt(90)

lt(15)
for i in range(7):
    lt(30)
    fd(10 * m)
    lt(60)

up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * m, y * m)
        dot(3, 'red')

done()

# otvet: 98