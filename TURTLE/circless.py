from turtle import *
s=Screen()

t=Turtle()
pencolor('blue')
pensize(4)
fillcolor('red')
speed('fastest')
for i in range(10,0,-1):
    begin_fill()
    circle(i*15)
    lt(25)
    end_fill()
goto(20,250)
mainloop()