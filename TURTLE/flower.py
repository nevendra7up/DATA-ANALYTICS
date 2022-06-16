from turtle import *
s=Screen()
t=Turtle()
t.speed('fastest')

t.penup()
t.goto(-40,40)
t.pendown()
t.lt(90)
t.fillcolor('Yellow')
t.begin_fill()
while(True):
    t.circle(-40,180)
    t.lt(90+30)
    if t.distance(-40,40)<1:
        break
t.end_fill()

t.penup()
t.goto(0,20)
t.pendown()

t.fillcolor('green')
t.begin_fill()
t.rt(90)
t.circle(-40)
t.end_fill()

t.penup()
t.goto(40.00,-98.56)
t.rt(70)
t.pendown()
t.pencolor('brown')
t.circle(-200,80)

print(t.pos())
mainloop()