from turtle import *
import random
s=Screen()
t=Turtle()
s.setup(500,500)
colors=['orange','green','blue','purple']
speed('fastest')
for i in range(50):
    x=random.randint(-200,200)
    y=random.randint(-200,200)
    penup()
    goto(x,y)
    pendown()
    pensize(random.randint(3,4))
    pencolor(colors[random.randint(0,3)])
    radius=random.randint(5,30)
    fillcolor('yellow')
    begin_fill()
    for i in range(6):
        circle(radius)
        left(60)
    end_fill()


mainloop()
