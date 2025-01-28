from turtle import *

screensize(2000,2000)
tracer(0)
m = 10
lt(90)

for i in range(12):
    for i in range(8):
        fd(50 * m)
        rt(45)
    rt(30)

up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * m, y * m)
        dot(3, 'red')

done()

# otvet: 12