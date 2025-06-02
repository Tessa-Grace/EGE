from turtle import *

screensize(2000,2000)
tracer(0)
lt(90)
m = 50

rt(270)
for i in range(2):
    fd(8 * m)
    rt(120)

rt(120)
for i in range(2):
    rt(120)
    fd(3 * m)
    rt(240)

rt(240)
for i in range(2):
    fd(14 * m)
    rt(120)

up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * m, y * m)
        dot(3, 'white')

done()

# s = (a*h)/2
# s = (12*14)/2 = 84

# otvet: 84