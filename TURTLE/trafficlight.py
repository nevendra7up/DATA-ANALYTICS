from turtle import *
s=Screen()

s.setup(500,500)
#speed('fastest')

penup()
goto(0,-100)
pendown()

fillcolor('black')
begin_fill()
fd(50)
lt(90)
fd(300)
lt(90)
fd(100)
lt(90)
fd(300)
lt(90)
fd(50)
end_fill()

penup()
goto(0,0)
pendown()

pencolor('black')
pensize(2)
fillcolor('yellow')
begin_fill()
circle(50)
end_fill()

penup()
goto(0,100)
pendown()

pencolor('black')
pensize(2)
fillcolor('red')
begin_fill()
circle(50)
end_fill()

penup()
goto(0,-100)
pendown()

pencolor('black')
pensize(2)
fillcolor('green')
begin_fill()
circle(50)
end_fill()

rt(90)
fd(200)




mainloop()
