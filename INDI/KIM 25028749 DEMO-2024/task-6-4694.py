from turtle import *

screensize(2000,2000)
tracer(0)
m = 40
lt(90)

for i in range(7):
    fd(10 * m)
    rt(120)
up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * m, y * m)
        dot(3, 'red')
done()

# otvet: 38