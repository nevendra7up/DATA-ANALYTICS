from turtle import *
import math as m
s=getscreen()
pensize(2)
speed('fastest')

penup()
goto(0,-200)
pendown()

circle(200)

penup()
goto(-200,0)
lt(45)
fd(200*m.sin(m.pi/4))
rt(45)
pendown()

circle(20)

penup()
goto(200,0)
lt(135)
fd(200*m.sin(m.pi/4))
rt(135)
pendown()

circle(20)

penup()
goto(0,50)
pendown()
rt(90)
fd(100)

penup()
goto(0,-125)
pendown()

lt(90)
circle(125,55)

penup()
goto(0,-125)
pendown()

lt(120)
circle(-125,55)


mainloop()