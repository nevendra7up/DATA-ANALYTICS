from turtle import *
s=getscreen()
t=Turtle()
t.pencolor('blue')
t.speed('fastest')

t.penup()
t.goto(0,-50)
t.pendown()

t.circle(50)
t.lt(90)

for i in range(24):
    t.penup()
    t.goto(0,0)
    t.pendown()
    t.lt(15)
    t.fd(50)

t.penup()
t.goto(-200,50)
t.pendown()

t.pencolor('black')
t.rt(90)
t.fd(400)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(400)
t.rt(90)
t.fd(100)

t.penup()
t.goto(-200,150)
t.pendown()
t.fillcolor('Orange')
t.begin_fill()
t.rt(90)
t.fd(400)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(400)
t.rt(90)
t.fd(100)
t.end_fill()

t.penup()
t.goto(-200,-50)
t.pendown()
t.fillcolor('Green')
t.begin_fill()
t.rt(90)
t.fd(400)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(400)
t.rt(90)
t.fd(100)
t.end_fill()





mainloop()

