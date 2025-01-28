from turtle import *

screensize(2000,2000)
tracer(0)
m = 30
lt(90)

for i in range(7):
    fd(20 * m)
    rt(240)
    fd(10 * m)
    rt(240)
    fd(20 * m)
    rt(120)
    fd(10 * m)
    rt(120)


up()
for x in range(-20, 30):
    for y in range(-20, 30):
        goto(x * m, y * m)
        dot(3, 'red')

done()

# otvet: 76