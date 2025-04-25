from turtle import *

tracer(0)
lt(90)
m = 30

for i in range(15):
    fd(4 * m)
    rt(60)

up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * m, y * m)
        dot(3, 'red')
done()

# otvet: 5 * 6 + 8 = 38